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

我沒有寫夠多的`config.json`功能，請自己進到原始檔案裏面改，以下是你要改的內容：

### 機器人管理員

取得自己Discord帳號ID，他應該長這樣：`959977374471028779`(這是作者SamHacker的ID)
打開根目錄下的`main.py`，他應該有幾段長這樣：
```python
@client.event
async def on_message(message):
    # ...
    # 重設歷史對話
    if message.content == '!reset':
        if message.author.id == 959977374471028779:
            aibot.reset_history()
            await message.reply('歷史對話已重設！')
            return
        else:
            await message.reply('你沒有權限重設歷史對話！這只有作者 <@959977374471028779> 辦的到')
            return
    
    if message.content.startswith('!change'):
        if message.author.id == 959977374471028779:
            game = message.content.split(' ')[1]
            await client.change_presence(activity=discord.Game(name=game))
            await message.reply('遊戲已變更為「{}」！'.format(game))
        else:
            await message.reply('你沒有權限重設歷史對話！這只有作者 <@959977374471028779> 辦的到')
            return
    
    # ...
```

把裡面的`959977374471028779`全部取代成自己的ID，完美，已經改好了！

### 發送啟動、關閉訊息的頻道

一樣是`main.py`，找到這幾行：
```python
@client.event
async def on_ready():
    logging.warning(f'We have logged in as {client.user}')
    channel = client.get_channel(1185756393169485884)
    await channel.send("<:__:1185578246276919316> 我上線囉！\n要找我聊天記得@我喔~~")

@client.event
async def on_disconnect():
    channel = client.get_channel(1185756393169485884)
    await channel.send('<:__:1185578246276919316> 我下線囉！\n現在沒空聊天QAQ，待會見~~')
```

裡面的`channel = client.get_channel(1185756393169485884)`裡`1185756393169485884`通通換成自己要用來發送訊息的頻道ID。
上面的`on_ready`裡面是上線訊息，把`<:__:1185578246276919316> 我上線囉！\n要找我聊天記得@我喔~~`換成自己要的上線訊息，`<:__:1185578246276919316>`這段請自己換成自己要的Emoji，不想或沒有Emoji可以把這段移除；底下`on_disconnect`裡面是下線訊息，把`<:__:1185578246276919316> 我下線囉！\n現在沒空聊天QAQ，待會見~~`換成自己要的下線訊息，`<:__:1185578246276919316>`這段請自己換成自己要的Emoji，不想或沒有Emoji可以把這段移除。

### 專用頻道

需要設定一個專屬頻道，讓機器人可以只在這個頻道出現？請如此設定：
一樣，在`main.py`挖出這幾行：
```python
@client.event
async def on_message(message):
    # ...
    # 檢查是否有提及機器人
    if client.user.mentioned_in(message):
        # ...
        async with message.channel.typing():
            if message.channel.id != 1185756393169485884:
                return
        
        #...
```
把裡面的`message.channel.id != 1185756393169485884`中`1185756393169485884`改成專屬頻道的ID(只能一個！！)，收工！

> Note：如果你不想要這個功能，你用VS Code可以直接選取這幾行，按下`Ctrl + /(Windows，Mac自己把Ctrl換成Cmd)`(預設快捷鍵，你有改過註解快捷鍵自己用自己的)註解起來就OK了！

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

然後重新啟動機器人，


## 貢獻

歡迎任何形式的貢獻！請先開啟一個問題，然後提交一個拉取請求。

## 授權

此項目使用 GNU v3 授權。請參見 `LICENSE` 文件以獲取更多資訊。
