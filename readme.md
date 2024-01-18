# Nether AI

這是一個使用 Discord.py 建立的 AI 機器人，調用 Google Bard Gemini API 以達到完整對話功能，可以自行訓練適合自己的機器人並支持多輪對話！

## 功能

- 你專屬的AI助手
- 提供所有Gemini功能
- 提供遊戲資訊
- 高可自訂能力
- 你想的到的AI功能他都有！

## 安裝

1. 執行以下Git指令以克隆此儲存庫：
```shell
$ git clone https://github.com/510208/ai_bot.git
```
2. 安裝Python 3.11 (推薦3.11版本，以防止Bug)
3. 安裝依賴項：`pip install -r requirements.txt`
4. 設定您的機器人 Token 在 `config.json`
5. 設定 Gemini API Key，詳細設定方法如下(`config.json`)請自行建立：
```json
{
    "gemini_api_key": "Gemini 的API金鑰",
    "discord_api_key": "Discord 機器人的Token"
}
```
6. 運行 `main.py`

## 基本設定

我沒有寫夠多的`config.json`功能，請自己進到原始檔案裏面改，請前往 [初始化教學](docs/initialization.md)

## 使用

Mention 機器人，就可開始聊天了

## 訓練機器人

如果你希望可以訓練這個機器人，請開啟`aibot.py`，找到`def reset_history():`這一行底下應該長這樣：
```python
def reset_history():
    # 設定歷史紀錄檔案名稱，使用當前時間作為檔名
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f'history_{current_time}.json'
    
    default_history = {
        # 一大串東西...
    }

    # 以下省略
```
看到底下的`default_history = { ... }`，找到`你現在是一位Minecraft伺服器的管理員，是個活潑善於社交的國中女生，繁體中文與英文是你的專長，並且身為一個少女，講話時常使用一些網路語言，如XD、QAQ等；但你完全不了解簡體字，無法回應任何使用簡體字的訊息。你管理的伺服器名為...`，這是我對自己機器人的人設設定，請把它改成自己的人設設定，記得斷行的地方用`\n`取代。

然後重新啟動機器人，重啟後於 [被設定做為唯一聊天頻道](#專用頻道) 的頻道執行指令`!reset`重設聊天紀錄，再次聊天就會使用正確的人設執行！

## 機器人指令清單

請檢閱此說明文件以查詢指令清單： [指令清單文件](docs/command.md)

## 貢獻

歡迎任何形式的貢獻！請先開啟一個問題，然後提交一個拉取請求。

## 授權

此項目使用 GNU v3 授權。請參見 `LICENSE` 文件以獲取更多資訊。
