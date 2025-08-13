#!/usr/bin/env python3
"""
Semi-Utils Web Application Runner
"""

import subprocess
import sys
import os

def main():
    """Run the Streamlit web application"""
    try:
        # Check if streamlit is installed
        import streamlit
        print("🚀 启动 Semi-Utils Web 应用...")
        print("📱 应用将在浏览器中打开")
        print("🔗 本地地址: http://localhost:8501")
        print("⏹️  按 Ctrl+C 停止应用")
        print("-" * 50)
        
        # Run streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "0.0.0.0"
        ])
        
    except ImportError:
        print("❌ 错误: 未安装 Streamlit")
        print("请运行: pip install streamlit")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 应用已停止")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 