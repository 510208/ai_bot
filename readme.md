# Nether AI

這是一個使用 Discord.py 建立的 AI 機器人，調用 Google Bard Gemini API 以達到完整對話功能，可以自行訓練適合自己的機器人並支持多輪對話！

## 功能

- 你專屬的AI助手
- 提供所有Gemini功能
- 提供遊戲資訊
- 高可自訂能力
- 你想的到的AI功能他都有！

## 安裝

1. 克隆此存儲庫
2. 安裝依賴項：`pip install -r requirements.txt`
3. 設定您的機器人 Token 在 `config.json`
4. 設定 Gemini API Key，詳細設定方法如下：
```json
{
    "gemini_api_key": "Gemini 的API金鑰",
    "discord_api_key": "Discord 機器人的Token"
}
```
5. 運行 `main.py`

## 使用

Mention 機器人，就可開始聊天了

## 貢獻

歡迎任何形式的貢獻！請先開啟一個問題，然後提交一個拉取請求。

## 授權

此項目使用 GNU v3 授權。請參見 `LICENSE` 文件以獲取更多資訊。