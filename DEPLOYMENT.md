# 🚀 部署指南

## 快速部署到 Streamlit Cloud

### 步骤 1: 准备 GitHub 仓库

1. **Fork 本仓库**
   - 访问 [semi-utils](https://github.com/leslievan/semi-utils)
   - 点击右上角的 "Fork" 按钮
   - 选择你的 GitHub 账号

2. **克隆到本地** (可选)
   ```bash
   git clone https://github.com/你的用户名/semi-utils.git
   cd semi-utils
   ```

### 步骤 2: 部署到 Streamlit Cloud

1. **注册 Streamlit Cloud**
   - 访问 [share.streamlit.io](https://share.streamlit.io)
   - 点击 "Sign in with GitHub"
   - 授权访问你的 GitHub 账号

2. **创建新应用**
   - 点击 "New app"
   - 填写以下信息：
     - **Repository**: 选择你 fork 的 semi-utils 仓库
     - **Branch**: `main` 或 `master`
     - **Main file path**: `app.py`
     - **App URL**: 可以自定义 (可选)

3. **点击 "Deploy"**
   - 等待部署完成 (通常需要 1-2 分钟)
   - 部署成功后你会看到一个公开的 URL

### 步骤 3: 分享你的应用

- 复制生成的 URL (例如: `https://your-app-name.streamlit.app`)
- 分享给其他人使用

## 其他部署平台

### Heroku 部署

1. **安装 Heroku CLI**
   ```bash
   # macOS
   brew install heroku/brew/heroku
   ```

2. **创建 Heroku 应用**
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **设置构建包**
   ```bash
   heroku buildpacks:set heroku/python
   ```

4. **部署**
   ```bash
   git add .
   git commit -m "Add web version"
   git push heroku main
   ```

### Railway 部署

1. **注册 Railway**
   - 访问 [railway.app](https://railway.app)
   - 使用 GitHub 账号登录

2. **连接仓库**
   - 点击 "New Project"
   - 选择 "Deploy from GitHub repo"
   - 选择你的 semi-utils 仓库

3. **自动部署**
   - Railway 会自动检测并部署 Streamlit 应用
   - 等待部署完成

## 本地开发

### 环境设置

1. **安装 Python 3.8+**
   ```bash
   # 使用 pyenv (推荐)
   pyenv install 3.8.20
   pyenv local 3.8.20
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **运行应用**
   ```bash
   # 方法 1: 使用启动脚本
   python run_web.py
   
   # 方法 2: 直接运行
   streamlit run app.py
   ```

4. **访问应用**
   - 打开浏览器访问: http://localhost:8501

### 开发模式

```bash
# 启用开发模式
streamlit run app.py --server.runOnSave true
```

## 故障排除

### 常见问题

1. **导入错误**
   ```bash
   # 确保所有依赖已安装
   pip install -r requirements.txt
   ```

2. **字体文件缺失**
   ```bash
   # 确保 fonts/ 目录存在
   ls fonts/
   ```

3. **Logo 文件缺失**
   ```bash
   # 确保 logos/ 目录存在
   ls logos/
   ```

### 日志查看

```bash
# Streamlit Cloud
# 在应用页面查看 "View app logs"

# Heroku
heroku logs --tail

# Railway
# 在 Railway 控制台查看日志
```

## 自定义配置

### 修改默认设置

编辑 `config.yaml` 文件:

```yaml
layout:
  type: watermark_right_logo  # 默认布局
  logo_enable: true          # 默认启用 Logo
  logo_position: right       # Logo 位置

global:
  white_margin:
    enable: false            # 默认不启用白边
    width: 3
  shadow:
    enable: false            # 默认不启用阴影
```

### 添加自定义 Logo

1. **添加 Logo 文件**
   ```bash
   # 将你的 Logo 文件放到 logos/ 目录
   cp your_logo.png logos/
   ```

2. **更新配置**
   ```yaml
   logo:
     makes:
       your_brand:
         id: YOUR_BRAND
         path: ./logos/your_logo.png
   ```

## 支持

如果遇到问题，请：

1. 查看 [README.md](README.md)
2. 检查 [常见问题](#故障排除)
3. 提交 GitHub Issue
4. 联系维护者 