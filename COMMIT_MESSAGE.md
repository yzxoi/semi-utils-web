feat: Transform Semi-Utils into web application with Streamlit

## 🌐 Major Changes

### ✨ New Features
- **Web Application**: Complete Streamlit-based web interface
- **Online Processing**: No installation required, browser-based usage
- **Batch Processing**: Support for multiple image uploads
- **Real-time Preview**: Instant image preview after upload
- **Progress Tracking**: Real-time processing progress display
- **Flexible Download**: Single file or batch ZIP download
- **Responsive Design**: Mobile, tablet, and desktop compatible

### 🗑️ Removed Components
- Desktop-specific executables (`main.py`, `main.spec`, `build_win_pkg.spec`)
- Installation scripts (`install.ps1`, `install.sh`, `start.applescript`)
- Video generation functionality (`gen_video.py`)
- Windows icon file (`logo.ico`)
- Temporary and output directories
- File-based logging system

### 🔧 Technical Improvements
- **Streamlit Integration**: Modern web framework for data apps
- **Modular Architecture**: Reused existing core business logic
- **Error Handling**: Comprehensive exception handling and user feedback
- **Memory Management**: Automatic cleanup of temporary files
- **Cross-platform**: Works on Windows, macOS, and Linux

### 📚 Documentation Updates
- **README.md**: Complete rewrite focusing on web version
- **DEPLOYMENT.md**: Streamlined deployment guide
- **NOTICE**: Proper attribution for Apache-2.0 compliance
- **.gitignore**: Updated for web development workflow

### 🚀 Deployment Ready
- **Streamlit Cloud**: Primary deployment platform
- **Heroku**: Alternative deployment option
- **Railway**: Cloud deployment support
- **GitHub Actions**: Automated testing workflow

## 📋 File Structure

```
semi-utils/
├── app.py                    # 🌟 Streamlit main application
├── run_web.py               # 🚀 Simplified launcher
├── test_web.py              # 🧪 Comprehensive test suite
├── requirements.txt         # 📦 Updated dependencies
├── config.yaml              # ⚙️ Configuration file
├── .streamlit/              # ⚙️ Streamlit configuration
├── .github/workflows/       # 🔄 GitHub Actions
├── entity/                  # 🔧 Core business logic
├── enums/                   # 📋 Enum definitions
├── fonts/                   # 🔤 Font files
├── logos/                   # 🏷️ Logo files
├── images/                  # 🖼️ Example images
├── README.md                # 📖 Main documentation
├── DEPLOYMENT.md            # 🚀 Deployment guide
├── NOTICE                   # 📄 Attribution notice
└── LICENSE                  # 📄 Apache-2.0 license
```

## 🔗 License Compliance

- **Apache-2.0 License**: Maintained from original project
- **NOTICE File**: Proper attribution to original author @leslievan
- **Third-party Components**: All dependencies properly documented
- **Original Project**: Based on https://github.com/leslievan/semi-utils

## 🎯 Benefits

### For Users
- **No Installation**: Direct browser access
- **Cross-platform**: Works on any device
- **Instant Sharing**: Public URL after deployment
- **Collaboration**: Multiple users can access simultaneously
- **Auto-updates**: Code updates automatically deploy

### For Developers
- **Code Reuse**: Leveraged existing image processing logic
- **Maintainable**: Clean, modular code structure
- **Extensible**: Easy to add new features and layouts
- **Performance**: Optimized for web environment
- **Security**: File validation and cleanup mechanisms

## 🧪 Testing

All tests pass (5/5):
- ✅ Module imports
- ✅ File structure validation
- ✅ Configuration loading
- ✅ Layout processor verification
- ✅ Application import test

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python test_web.py

# Start application
python run_web.py
# or
streamlit run app.py
```

## 📞 Support

- **Documentation**: Comprehensive README and deployment guides
- **Issues**: GitHub Issues for bug reports
- **Contributions**: Pull requests welcome
- **License**: Apache-2.0 compliant

---

**🎉 Semi-Utils is now a modern, web-based image watermarking tool!** 