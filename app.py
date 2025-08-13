import streamlit as st
import os
import tempfile
import zipfile
from pathlib import Path
from PIL import Image
import io
import base64

# Import existing modules
from entity.config import Config
from entity.image_container import ImageContainer
from entity.image_processor import *
from init import layout_items_dict, config

# Page configuration
st.set_page_config(
    page_title="Semi-Utils 图片水印工具",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        color: #1f77b4;
    }
    .upload-section {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .config-section {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin: 1rem 0;
    }
    .stButton > button {
        width: 100%;
        height: 3rem;
        font-size: 1.1rem;
    }
    .download-section {
        background-color: #e8f5e8;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #4caf50;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def create_download_link(file_path, file_name):
    """Create a download link for files"""
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}">下载 {file_name}</a>'
    return href

def process_single_image(image_file, config_instance, layout_processor):
    """Process a single image with watermark"""
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
            tmp_file.write(image_file.getvalue())
            tmp_path = tmp_file.name
        
        # Create image container
        container = ImageContainer(Path(tmp_path))
        
        # Process image
        layout_processor.process(container)
        
        # Save processed image
        output_path = f"processed_{image_file.name}"
        container.save(output_path)
        container.close()
        
        # Clean up temp file
        os.unlink(tmp_path)
        
        return output_path
    except Exception as e:
        st.error(f"处理图片时出错: {str(e)}")
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">🖼️ Semi-Utils 图片水印工具</h1>', unsafe_allow_html=True)
    st.markdown("### 在线批量添加水印、处理照片像素比、图像色彩和质量的工具")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ 配置设置")
        
        # Layout selection
        st.subheader("布局选择")
        layout_options = {item.name: item.value for item in layout_items_dict.values()}
        selected_layout = st.selectbox(
            "选择水印布局",
            options=list(layout_options.keys()),
            index=list(layout_options.keys()).index("normal(Logo 居右)")
        )
        
        # Get the processor for selected layout
        layout_processor = layout_items_dict[layout_options[selected_layout]].processor
        
        # Logo settings (only for watermark layouts)
        if 'watermark' in layout_options[selected_layout]:
            st.subheader("Logo 设置")
            logo_enable = st.checkbox("启用 Logo", value=config.has_logo_enabled())
            if logo_enable:
                logo_position = st.radio("Logo 位置", ["left", "right"], 
                                       index=0 if config.is_logo_left() else 1)
                config._data['layout']['logo_enable'] = True
                config._data['layout']['logo_position'] = logo_position
            else:
                config._data['layout']['logo_enable'] = False
        
        # Global settings
        st.subheader("全局设置")
        white_margin_enable = st.checkbox("启用白边", value=config.has_white_margin_enabled())
        if white_margin_enable:
            white_margin_width = st.slider("白边宽度 (%)", 1, 30, config.get_white_margin_width())
            config._data['global']['white_margin']['enable'] = True
            config._data['global']['white_margin']['width'] = white_margin_width
        else:
            config._data['global']['white_margin']['enable'] = False
            
        shadow_enable = st.checkbox("启用阴影", value=config.has_shadow_enabled())
        config._data['global']['shadow']['enable'] = shadow_enable
        
        # Font settings
        st.subheader("字体设置")
        font_size = st.selectbox("字体大小", [1, 2, 3], index=config._data['base']['font_size']-1)
        bold_font_size = st.selectbox("粗体字体大小", [1, 2, 3], index=config._data['base']['bold_font_size']-1)
        config._data['base']['font_size'] = font_size
        config._data['base']['bold_font_size'] = bold_font_size
        
        # Quality setting
        quality = st.slider("输出质量", 50, 100, config.get_quality())
        config._data['base']['quality'] = quality
    
    # Main content area
    
    st.header("📁 上传图片")
    
    uploaded_files = st.file_uploader(
        "选择要处理的图片文件",
        type=['jpg', 'jpeg', 'png', 'bmp', 'tiff'],
        accept_multiple_files=True,
        help="支持 JPG, PNG, BMP, TIFF 格式"
    )
    
    if uploaded_files:
        st.success(f"已上传 {len(uploaded_files)} 张图片")
        
        # Show preview of uploaded images
        st.subheader("📸 图片预览")
        preview_cols = st.columns(min(3, len(uploaded_files)))
        for idx, file in enumerate(uploaded_files):
            with preview_cols[idx % 3]:
                image = Image.open(file)
                st.image(image, caption=file.name, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Process button
    if uploaded_files:
        st.markdown("---")
        if st.button("🚀 开始处理图片", type="primary"):
            with st.spinner("正在处理图片..."):
                processed_files = []
                
                # Create progress bar
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for idx, file in enumerate(uploaded_files):
                    status_text.text(f"正在处理: {file.name}")
                    
                    # Process the image
                    output_path = process_single_image(file, config, layout_processor)
                    if output_path:
                        processed_files.append((output_path, file.name))
                    
                    # Update progress
                    progress_bar.progress((idx + 1) / len(uploaded_files))
                
                status_text.text("处理完成!")
                
                # Show results
                if processed_files:
                    
                    st.header("✅ 处理完成")
                    st.success(f"成功处理 {len(processed_files)} 张图片")
                    
                    # Show processed images preview
                    st.subheader("📸 处理结果预览")
                    preview_cols = st.columns(min(3, len(processed_files)))
                    for idx, (file_path, original_name) in enumerate(processed_files):
                        with preview_cols[idx % 3]:
                            image = Image.open(file_path)
                            st.image(image, caption=f"处理后: {original_name}", use_container_width=True)
                    
                    # Download options
                    st.subheader("📥 下载选项")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**单个文件下载:**")
                        for file_path, original_name in processed_files:
                            st.markdown(create_download_link(file_path, f"processed_{original_name}"), 
                                      unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown("**批量下载:**")
                        # Create zip file
                        zip_path = "processed_images.zip"
                        with zipfile.ZipFile(zip_path, 'w') as zipf:
                            for file_path, original_name in processed_files:
                                zipf.write(file_path, f"processed_{original_name}")
                        
                        st.markdown(create_download_link(zip_path, "processed_images.zip"), 
                                  unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Clean up temporary files
                    for file_path, _ in processed_files:
                        try:
                            os.remove(file_path)
                        except:
                            pass
                    try:
                        os.remove(zip_path)
                    except:
                        pass

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>🖼️ Semi-Utils 图片水印工具 | 基于 Streamlit 构建</p>
        <p>支持批量处理、多种布局、自定义配置</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 