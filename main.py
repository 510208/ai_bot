import discord
import base64
import aibot  # 假設你的 AIBot 實現在 aibot_module 中
import json
import logging
import aiohttp
import asyncio
import time

last_message_time = None

# 設定 logging 基本配置
logging.basicConfig(format='[%(name)-10s][%(levelname)-7s] %(message)s')

# 設定 logging 等級
logging.getLogger().setLevel(logging.DEBUG)

# 測試 logging
logging.info('Logging module initialized.')


with open('config.json', 'r') as f:
    config = json.load(f)
    bot_token = config['discord_api_key']

# 初始化Pycord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.warning(f'We have logged in as {client.user}')
    channel = client.get_channel(1185756393169485884)
    await channel.send("<:__:1185578246276919316> 我上線囉！\n要找我聊天記得@我喔~~")

@client.event
async def on_disconnect():
    channel = client.get_channel(1185756393169485884)
    await channel.send('<:__:1185578246276919316> 我下線囉！\n現在沒空聊天QAQ，待會見~~')

@client.event
async def on_message(message):
    global last_message_time
    # 發送上路訊息
    current_time = time.time()
    if last_message_time is not None and current_time - last_message_time < 10:
        return
    last_message_time = current_time

    if message.author == client.user:
        return

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

    # 檢查是否有提及機器人
    if client.user.mentioned_in(message):
        logging.info('=' * 5 + '開始AI紀錄' + '=' * 5)
        # 檢查用戶名是否在黑名單中
        # if user_input.name.lower() in [name.lower() for name in blacklist]:
        #     logging.warning(f'\n請求提出者；{message.author}\n請求頻道：{message.channel}\n請求伺服器：{message.guild}\n類型：請求失敗')
        #     print("抱歉，你在黑名單中，我無法回應你的請求。")
        #     await message.reply("抱歉，你在黑名單中，我無法回應你的請求。")
        #     return
        # 提取訊息文字
        prompt_text = message.content

        mentioned_users = message.mentions
        # 去除 mention 的部分
        for user in mentioned_users:
            prompt_text = prompt_text.replace(f'<@{user.id}>', '')

        async with message.channel.typing():
            if message.channel.id != 1185756393169485884:
                return
            
            logging.info(f'\n提示詞：{prompt_text}\n請求提出者；{message.author}\n請求頻道：{message.channel}\n請求伺服器：{message.guild}\n類型：純文字')
            prompt_text = prompt_text.lstrip()

            # 使用 prompt_chat 方法取得回應
            response_dict = aibot.prompt_chat(prompt_text)

            # 讀取回應字典中的 answer
            response_text = response_dict.get('answer')

            if response_text is None:
                response_text = '> 人家不懂啦！！再講一次嘛，好嗎好嗎？'

            # 回覆對方
            await message.reply(response_text)
    
    logging.info('=' * 5 + '結束AI紀錄' + '=' * 5)
    
    # # 等待十秒
    # await asyncio.sleep(10)

# 替換成你的機器人 Token
client.run(bot_token)
