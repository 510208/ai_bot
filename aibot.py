# 單個純文字
import json
import requests
import base64
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, format='[%(name)-5s][%(levelname)-7s] %(message)s')

with open('config.json', 'r') as f:
    config = json.load(f)

with open('prefix_prompt.json', 'r') as f:
    default_history = json.load(f)

# with open('history.json', 'r', encoding='utf-8') as f:
#     history = json.load(f)

API_KEY = config['gemini_api_key']

"""
Gemini 正常調用範例
"""
def prompt_chat(prompt_text):
    print(prompt_text)
    url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}'

    headers = {'Content-Type': 'application/json'}

    if prompt_text == '' or prompt_text == ' ':
        return {
            "status_code": 200,
            "response": "> 告訴人家你要說什麼啦！",
            "answer": "> 告訴人家你要說什麼啦！"
        }

    # 在這裡進行 history 變數的初始化
    history = json.load(open('history.json', 'r', encoding='utf-8'))

    # 將歷史對話加入到 data 中
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

    logging.info("傳出JSON：\n" + json.dumps(data, indent=4, ensure_ascii=False))

    response = requests.post(url, headers=headers, json=data)

    logging.debug(response.text)
    
    if response.status_code == 200:
        # 將 JSON 格式的回應轉換成 Python 字典
        response_data = response.json()

        logging.info("傳回JSON：\n" + json.dumps(data, indent=4, ensure_ascii=False))

        # 從回應字典中提取你需要的資訊
        candidates = response_data.get('candidates', [])

        # 提取 candidates 中的 content，假設 content 是一個字串
        if candidates and 'content' in candidates[0] and 'parts' in candidates[0]['content'] and candidates[0]['content']['parts']:
            content = candidates[0]['content']['parts'][0].get('text', '')
        else:
            content = ''

        # 將回應加入歷史對話

        history['contents'].append({
            "role": "user",
            "parts": [{"text": prompt_text}]
        })

        history['contents'].append({
            "role": "model",
            "parts": [{"text": content}]
        })

        # 將更新後的歷史對話寫入到 JSON 檔案
        with open('history.json', 'w', encoding='utf-8') as json_file:
            json.dump(history, json_file, ensure_ascii=False, indent=4)
        
        # 現在打開文件的副本以進行讀取
        with open('history.json', 'r', encoding='utf-8') as json_file:
            history = json.load(json_file)
        
        logging.info("History結果\n" + json.dumps(data, indent=4, ensure_ascii=False))
        
        print(content)

        if content:
            return {
                "status_code": response.status_code,
                "response": response_data,
                "answer": content
            }
        else:
            finish_reason = response_data.get('candidates', [{}])[0].get('finishReason', '')
            return {
                "status_code": response.status_code,
                "response": response_data,
                "answer": f"抱歉喔，我沒辦法告訴你這件事，Google因為這個原因：{finish_reason}，不讓我告訴你..."
            }
    else:
        return {
            "status_code": response.status_code,
            "response": response.text,
            "answer": None
        }
    
def reset_history():
    # 設定歷史紀錄檔案名稱，使用當前時間作為檔名
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f'history_{current_time}.json'
    
    # default_history = {}

    # 讀取當前的歷史紀錄
    with open('history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

    # 將歷史紀錄保存到新的檔案中
    with open(filename, 'w', encoding='utf-8') as new_file:
        json.dump(history, new_file, ensure_ascii=False, indent=4)

    # 重設歷史紀錄
    with open('history.json', 'w', encoding='utf-8') as f:
        json.dump(default_history, f, ensure_ascii=False, indent=4)

    logging.info(f"History 已保存到 {filename}，並已重設歷史紀錄")

def send_history():
    with open('history.json', 'r', encoding='utf-8') as json_file:
        history = json.load(json_file)

    return "History結果\n```" + json.dumps(history, indent=4, ensure_ascii=False) + "```"
# """
# Gemini 圖片識別調用
# """
# def img_identify(image_base64_string, prompt_text="詳細說明你在這張圖片中看到什麼？"):
#     logging.info(f'Image detected.\nBase64 string: {image_base64_string}')
#     url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro-vision:generateContent?key={API_KEY}'
#     headers = {'Content-Type': 'application/json'}
#     data = {
#         "contents": [
#             {
#                 "parts": [
#                     {"text": f"{prompt_text}"},
#                     {
#                         "inline_data": {
#                             "mime_type": "image/jpeg",
#                             "data": image_base64_string
#                         }
#                     }
#                 ]
#             },
#         ]
#     }

#     response = requests.post(url, headers=headers, json=data)

#     logging.debug(response.text)

#     if response.status_code == 200:
#         # 將 JSON 格式的回應轉換成 Python 字典
#         response_data = response.json()

#         # 從回應字典中提取你需要的資訊
#         candidates = response_data.get('candidates', [])

#         # 提取 candidates 中的 content，假設 content 是一個字串
#         content = candidates[0].get('content', {}).get('parts', [])[0].get('text', '')
#         print(content)
#         # 回傳的字典，包含狀態碼、完整回應和答案
#         return {
#             "status_code": response.status_code,
#             "response": response_data,
#             "answer": content
#         }
#     else:
#         return {
#             "status_code": response.status_code,
#             "response": response.text,
#             "answer": None
#         }