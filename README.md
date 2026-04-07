# Comic Auto Sign-in 漫画平台自动签到

[![GitHub License](https://img.shields.io/github/license/muzimu217/comic-auto-signin)](https://github.com/muzimu217/comic-auto-signin/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/muzimu217/comic-auto-signin)](https://github.com/muzimu217/comic-auto-signin/stargazers)

基于 GitHub Actions 的漫画平台自动签到工具，支持多账号配置。

## ✨ 功能特性

- ✅ 支持 Pica（哔咔漫画）和 JM（禁漫天堂）两个平台
- ✅ 支持每个平台配置多个账号
- ✅ 每天自动签到（北京时间 8:30）
- ✅ 支持代理配置
- ✅ 支持手动触发运行
- ✅ 完全免费，基于 GitHub Actions

## 🚀 快速开始

### 1. Fork 本仓库

点击右上角 Fork 按钮，将仓库复制到你的账号下

### 2. 配置账号信息

进入你的仓库 **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

添加名为 `ACCOUNTS_CONFIG` 的 Secret，值为 JSON 格式：

```json
{
  "pica": [
    {"user": "pica账号1", "password": "pica密码1"},
    {"user": "pica账号2", "password": "pica密码2"}
  ],
  "jm": [
    {"user": "jm账号1", "password": "jm密码1"},
    {"user": "jm账号2", "password": "jm密码2"}
  ],
  "proxy": ""
}
```

**配置说明：**
- `pica`: Pica 平台账号列表（可配置多个或留空数组 `[]`）
- `jm`: JM 平台账号列表（可配置多个或留空数组 `[]`）
- `proxy`: 代理地址（可选，不需要可以设为空字符串 `""` 或删除该字段）

### 3. 启用 GitHub Actions

进入 **Actions** 页面，启用 Workflows，然后手动运行一次测试

## 📝 配置示例

### 示例 1：多账号配置

```json
{
  "pica": [
    {"user": "user1@example.com", "password": "pass1"},
    {"user": "user2@example.com", "password": "pass2"}
  ],
  "jm": [
    {"user": "jmuser1", "password": "pass1"},
    {"user": "jmuser2", "password": "pass2"}
  ]
}
```

### 示例 2：仅 Pica 平台

```json
{
  "pica": [
    {"user": "your_email@example.com", "password": "your_password"}
  ],
  "jm": []
}
```

### 示例 3：仅 JM 平台

```json
{
  "pica": [],
  "jm": [
    {"user": "your_username", "password": "your_password"}
  ]
}
```

### 示例 4：使用代理

```json
{
  "pica": [
    {"user": "your_email@example.com", "password": "your_password"}
  ],
  "jm": [
    {"user": "your_username", "password": "your_password"}
  ],
  "proxy": "127.0.0.1:7890"
}
```

## ⏰ 定时任务

- **自动运行时间**：每天 UTC 0:30（北京时间 8:30）
- **手动触发**：Actions → Comics Daily Sign-in → Run workflow

## 🔧 本地运行

```bash
# 克隆仓库
git clone https://github.com/muzimu217/comic-auto-signin.git
cd comic-auto-signin

# 安装依赖
pip install -r requirements.txt

# 设置环境变量
export ACCOUNTS_CONFIG='{"pica":[{"user":"your_user","password":"your_pass"}],"jm":[{"user":"your_user","password":"your_pass"}]}'

# 运行
python main.py
```

## ❓ 常见问题

**Q: 如何添加 GitHub Secret？**  
A: 仓库页面 → Settings → Secrets and variables → Actions → New repository secret

**Q: 如何验证配置是否正确？**  
A: 进入 Actions 页面，手动触发一次 workflow，查看运行日志

**Q: 支持几个账号？**  
A: 理论上无限制，建议每个平台不超过 10 个账号

**Q: 代理如何配置？**  
A: 格式为 `IP:端口`，例如 `127.0.0.1:7890`。不需要代理可以设为空字符串或删除该字段

**Q: Pica 签到显示 fail 是什么意思？**  
A: 表示今天已经签到过了，不是错误

**Q: 会不会泄露我的账号信息？**  
A: 不会。账号信息存储在 GitHub Secrets 中，加密保存，日志中也不会显示密码

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源

## 🙏 致谢

感谢原项目 [RahabHub/ComicsPuncher](https://github.com/RahabHub/ComicsPuncher) 提供的基础代码

## ⚠️ 免责声明

本工具仅供学习交流使用，请遵守相关平台的使用条款。使用本工具产生的任何后果由使用者自行承担。

---

如果这个项目对你有帮助，欢迎 ⭐ Star 支持一下！
