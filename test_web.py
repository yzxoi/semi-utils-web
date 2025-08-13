#!/usr/bin/env python3
"""
测试 Semi-Utils Web 应用功能
"""

import os
import sys
from pathlib import Path

def test_imports():
    """测试所有必要的模块导入"""
    print("🔍 测试模块导入...")
    
    try:
        import streamlit
        print("✅ Streamlit 导入成功")
    except ImportError as e:
        print(f"❌ Streamlit 导入失败: {e}")
        return False
    
    try:
        from entity.config import Config
        print("✅ Config 导入成功")
    except ImportError as e:
        print(f"❌ Config 导入失败: {e}")
        return False
    
    try:
        from entity.image_container import ImageContainer
        print("✅ ImageContainer 导入成功")
    except ImportError as e:
        print(f"❌ ImageContainer 导入失败: {e}")
        return False
    
    try:
        from entity.image_processor import WatermarkProcessor
        print("✅ WatermarkProcessor 导入成功")
    except ImportError as e:
        print(f"❌ WatermarkProcessor 导入失败: {e}")
        return False
    
    try:
        from init import layout_items_dict, config
        print("✅ 布局配置导入成功")
    except ImportError as e:
        print(f"❌ 布局配置导入失败: {e}")
        return False
    
    return True

def test_files():
    """测试必要文件是否存在"""
    print("\n📁 测试文件结构...")
    
    required_files = [
        "app.py",
        "config.yaml",
        "requirements.txt",
        "run_web.py"
    ]
    
    required_dirs = [
        "entity",
        "enums", 
        "fonts",
        "logos"
    ]
    
    all_good = True
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} 存在")
        else:
            print(f"❌ {file} 缺失")
            all_good = False
    
    for dir in required_dirs:
        if os.path.isdir(dir):
            print(f"✅ {dir}/ 目录存在")
        else:
            print(f"❌ {dir}/ 目录缺失")
            all_good = False
    
    return all_good

def test_config():
    """测试配置文件"""
    print("\n⚙️ 测试配置文件...")
    
    try:
        from entity.config import Config
        config = Config('config.yaml')
        print("✅ 配置文件加载成功")
        
        # 测试基本配置
        print(f"   - 输入目录: {config.get_input_dir()}")
        print(f"   - 输出目录: {config.get_output_dir()}")
        print(f"   - 布局类型: {config.get_layout_type()}")
        print(f"   - Logo 启用: {config.has_logo_enabled()}")
        
        return True
    except Exception as e:
        print(f"❌ 配置文件测试失败: {e}")
        return False

def test_layouts():
    """测试布局处理器"""
    print("\n🎨 测试布局处理器...")
    
    try:
        from init import layout_items_dict
        
        print(f"✅ 找到 {len(layout_items_dict)} 个布局")
        
        for name, item in layout_items_dict.items():
            print(f"   - {item.name}: {item.value}")
        
        return True
    except Exception as e:
        print(f"❌ 布局处理器测试失败: {e}")
        return False

def test_app_import():
    """测试应用导入"""
    print("\n🚀 测试应用导入...")
    
    try:
        import app
        print("✅ 应用模块导入成功")
        return True
    except Exception as e:
        print(f"❌ 应用模块导入失败: {e}")
        return False

def main():
    """主测试函数"""
    print("🧪 Semi-Utils Web 应用测试")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_files,
        test_config,
        test_layouts,
        test_app_import
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！应用可以正常运行。")
        print("\n🚀 启动应用:")
        print("   python run_web.py")
        print("   或")
        print("   streamlit run app.py")
        return True
    else:
        print("❌ 部分测试失败，请检查错误信息。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 