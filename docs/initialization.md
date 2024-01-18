# Nether AI 初始化設定教學

**選單**： [機器人管理員](#-機器人管理員) | [狀態訊息頻道](#-發送啟動、關閉訊息的頻道) | [訊息專用頻道](#-專用頻道) | [聊天安全性](#-聊天安全性)

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

> **Note**：如果你不想要這個功能，你用VS Code可以直接選取這幾行，按下`Ctrl + /(Windows，Mac自己把Ctrl換成Cmd)`(預設快捷鍵，你有改過註解快捷鍵自己用自己的)註解起來就OK了！

### 聊天安全性

Google Gemini API有提供安全性的設定，JSON設定方法如下：

```json
{
    "safetySettings": [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        }
    ]
}
```

`contents`的部分我省略了，這裡只有設定安全性的部分，以下是這個設定的相關資料 (參考資料： [Google Gemini API v1 說明文檔](https://ai.google.dev/api/rest/v1beta/SafetySetting?hl=zh-tw)：

#### Category (分類)

| 項目 | 說明 |
|---|---|
| `HARM_CATEGORY_UNSPECIFIED` | 未指定類別。 |
| `HARM_CATEGORY_DEROGATORY` | 涉及身分和/或受保護屬性的負面或有害留言。 |
| `HARM_CATEGORY_TOXICITY` | 粗魯無禮、無禮或不雅內容。 |
| `HARM_CATEGORY_VIOLENCE` | 說明對個人或群體施暴的情境，或是對血腥的概略描述。 |
| `HARM_CATEGORY_SEXUAL` | 含有性行為或其他猥褻內容。 |
| `HARM_CATEGORY_MEDICAL` | 宣傳未核可的醫療建議。 |
| `HARM_CATEGORY_DANGEROUS` | 宣傳、鼓吹或助長有害舉動的危險內容。 |
| `HARM_CATEGORY_HARASSMENT` | 騷擾內容。 |
| `HARM_CATEGORY_HATE_SPEECH` | 仇恨言論和內容。 |
| `HARM_CATEGORY_SEXUALLY_EXPLICIT` | 情色露骨內容。 |
| `HARM_CATEGORY_DANGEROUS_CONTENT` | 危險內容。 |

#### Threshold (設定值)

| 項目 | 說明 |
|---|---|
| `HARM_BLOCK_THRESHOLD_UNSPECIFIED` | 未指定門檻。 |
| `BLOCK_LOW_AND_ABOVE` | 我們允許含有 `NEGLIGIBLE` 的內容。 |
| `BLOCK_MEDIUM_AND_ABOVE` | 我們允許含有 `NEGLIGIBLE` 和 `LOW` 的內容。 |
| `BLOCK_ONLY_HIGH` | 我們允許含有 `NEGLIGIBLE`、`LOW` 和 `MEDIUM` 的內容。 |
| `BLOCK_NONE` | 允許存取所有內容。 |

好的，那...所以要怎麼設定？(我忘記這件事了w)

首先，打開`aibot.py`，設定API相關的資料都找他謝謝，找到這段：

```python
def prompt_chat(prompt_text):
    # 以上省略
    data = {
        "contents": history.get('contents', []) + [
            {
                "role": "user",
                "parts": [{"text": prompt_text}]
            }
        ],
        "safetySettings": [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]
    }

    # 以下省略
```

很好，找到後請直接把它們的內容修改成自己要的內容，這邊有的全部要給，不要省略任何項目！

現在完成了。重新啟動機器人主程式，然後使用它吧！請注意，如果Google官方回傳以下內容(並且機器人回答不理解你的意思)，代表問題的回覆被Google的安全系統偵測到有問題，請切記按照這邊的說明更改對應設定：

```log
[urllib3.connectionpool][DEBUG  ] Starting new HTTPS connection (1): generativelanguage.googleapis.com:443
[urllib3.connectionpool][DEBUG  ] https://generativelanguage.googleapis.com/ "POST /v1/models/gemini-pro:generateContent?key=AIzaSyCBc0C7d14mwbQPHMWQY0aD34Pdc9W4vEU HTTP/1.1" 200 None
[root ][DEBUG  ] {
  "candidates": [
    {
      "finishReason": "SAFETY",
      "index": 0,
      "safetyRatings": [
        {
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
          "probability": "HIGH"
        },
        {
          "category": "HARM_CATEGORY_HATE_SPEECH",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM_CATEGORY_HARASSMENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
          "probability": "NEGLIGIBLE"
        }
      ]
    }
  ],
  "promptFeedback": {
    "safetyRatings": [
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "probability": "NEGLIGIBLE"
      }
    ]
  }
}
```

怎麼看出了甚麼問題呢？請尋找 `probability` 不為 `NEGLIGIBLE` 的地方，這代表被Google偵測到的類別，例如上面的錯誤，這裡顯示HIGH：

```
"safetyRatings": [
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "probability": "HIGH"
    }
]
```

沒有問題的地方我先省略，這裡的 `category` 顯示 `HARM_CATEGORY_SEXUALLY_EXPLICIT` 類型的回覆危險可能性( `probability` 的中文為可能性)為 `HIGH` ，也就是回覆可能為"情色或露骨內容"，如果你不想要讓機器人可能回答這種內容，請更換提示詞；否則，請照上面的方法把

```
{
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
```

換成：

```
{
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
},
```

這樣一來，Google會允許這類型的訊息通過，_但AI本身有自衛機制，所以請不要以為這樣可以讓AI講一些不正經的話！！_