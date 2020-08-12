from flask import Flask, request, abort
import linebot

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.models import (
    FollowEvent, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction,
    MessageAction, QuickReply, QuickReplyButton, PostbackEvent, PostbackAction)

from Question import Q

import os

app = Flask(__name__)

line_bot_api = LineBotApi(
    'MjIA5qDnDq6PwZAizAbPFJcmyILba0CBoJ/s8HmqE+t0wpgjQC+X5l8Pg50vnKjjsJvN+aoogNEdra3gWbbKUBJhxzN08hPzDvrs9mUfNtLk9S4T5/n/1dLpOj5Pedb3ulNA9CyCrYxFXwY6zLoTCgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('48e7d430dda98841dad45ca219096dbc')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'



n = 1

# 收個資
@handler.add(FollowEvent)
def handle_follow_event(event):
    user_profile = line_bot_api.get_profile(event.source.user_id)

    print(user_profile.display_name)
    print(user_profile.user_id)
    print(user_profile.picture_url)
    print(user_profile.status_message)

    with open("./users.csv", "w") as myfile:
        myfile.write(json.dumps(vars(user_profile), sort_keys=True))
        myfile.write('\r\n')




    # 歡迎詞
    text_send_message = TextSendMessage('このDIOだ! 我是Dio，\n歡迎你來到我的"世界"!\n在繁忙的日子，壓力很大嗎?\n在這裡，你可以利用我的能力暫停時間，停下來，休息一下，\n不妨花個時間做個小測驗，\n來檢視自己的壓力程度唷~\n那麼準備好的話，跟我講個暗號"Wryyy"，我就會幫你測驗了... \n另外，輸入"壓力"的話，我也會推薦你一些能夠幫助你的書唷!')
    image_send_message = ImageSendMessage(
        original_content_url="https://steamuserimages-a.akamaihd.net/ugc/915795043500363825/7B320C3E3D06532C2E1CCB298928BBBEAEB6CC84/",
        preview_image_url="https://steamuserimages-a.akamaihd.net/ugc/915795043500363825/7B320C3E3D06532C2E1CCB298928BBBEAEB6CC84/"
    )

    line_bot_api.reply_message(
        event.reply_token,
        [
            image_send_message,
            text_send_message
        ]
    )

# 定義按鈕
textQuickReplyButton1 = QuickReplyButton(
    action=MessageAction(
        label="是",
        text="1"))
textQuickReplyButton2 = QuickReplyButton(
    action=MessageAction(
        label="否",
        text="0"))

quickReplyList = QuickReply([textQuickReplyButton1,
                             textQuickReplyButton2])


flexCarouselContainerJsonDict = """{
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/077/67/0010776719.jpg&v=5a5c90bc&w=250&h=250",
          "size": "full",
          "aspectRatio": "20:13",
          "backgroundColor": "#D89393",
          "action": {
            "type": "uri",
            "uri": "http://www.eslite.com/product.aspx?pgid=1001116172652361&kw=放鬆之書+找出源頭+調適情緒+釋放壓力的全方位療癒減壓手冊&pi=0"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "放鬆之書",
              "flex": 0,
              "size": "xxl",
              "align": "start",
              "weight": "bold",
              "color": "#000000",
              "wrap": true
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "text",
                  "text": "找出源頭、調適情緒、釋放壓力的全方位療癒減壓手冊",
                  "flex": 0,
                  "size": "md",
                  "weight": "bold",
                  "wrap": true
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "我有興趣!!",
                "uri": "http://www.eslite.com/product.aspx?pgid=1001116172652361&kw=放鬆之書+找出源頭+調適情緒+釋放壓力的全方位療癒減壓手冊&pi=0"
              },
              "color": "#D67979",
              "style": "primary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/075/03/0010750391_bc_01.jpg&v=58f4a77b&w=250&h=250",
          "size": "full",
          "aspectRatio": "20:13",
          "backgroundColor": "#D89393",
          "action": {
            "type": "uri",
            "uri": "http://www.eslite.com/product.aspx?pgid=1001119732587157&kw=不被壓力綁架+駕馭壓力黃金8法則+在關鍵時刻不失常+表現出眾+&pi=0"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "不被壓力綁架",
              "size": "xxl",
              "align": "start",
              "weight": "bold",
              "color": "#000000",
              "wrap": true
            },
            {
              "type": "box",
              "layout": "baseline",
              "flex": 1,
              "contents": [
                {
                  "type": "text",
                  "text": "駕馭壓力黃金8法則, 在關鍵時刻不失常, 表現出眾! ",
                  "flex": 0,
                  "size": "md",
                  "weight": "bold",
                  "wrap": true
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "我有興趣!!",
                "uri": "http://www.eslite.com/product.aspx?pgid=1001119732587157&kw=不被壓力綁架+駕馭壓力黃金8法則+在關鍵時刻不失常+表現出眾+&pi=0"
              },
              "color": "#D67979",
              "style": "primary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/083/17/0010831746.jpg&w=200",
          "size": "full",
          "aspectRatio": "20:13",
          "backgroundColor": "#D89393"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "頂尖人士這樣面對壓力",
              "size": "xl",
              "align": "start",
              "weight": "bold",
              "color": "#000000",
              "wrap": true
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "text",
                  "text": "活用行為科學消除工作與人際難題",
                  "flex": 0,
                  "size": "md",
                  "weight": "bold",
                  "wrap": true
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "我有興趣!!",
                "uri": "http://www.eslite.com/product.aspx?pgid=1001122732787642&kw=頂尖人士這樣面對壓力+活用行為科學消除工作與人際難題&pi=0"
              },
              "color": "#D67979",
              "style": "primary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/084/13/0010841334.jpg&w=200",
          "size": "full",
          "aspectRatio": "20:13",
          "backgroundColor": "#D89393"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "你累了嗎? ",
              "size": "xl",
              "weight": "bold",
              "wrap": true
            },
            {
              "type": "box",
              "layout": "baseline",
              "flex": 1,
              "contents": [
                {
                  "type": "text",
                  "text": "根除疲勞的究極健康法",
                  "flex": 0,
                  "size": "md",
                  "weight": "bold",
                  "wrap": true
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "我有興趣!!",
                "uri": "http://www.eslite.com/product.aspx?pgid=1001309202811303&kw=世界の最新医学が証明した+根こそぎ疲れがとれる究極の健康法&pi=0"
              },
              "flex": 2,
              "color": "#D67979",
              "style": "primary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://s3.amazonaws.com/cms.ipressroom.com/332/files/20201/Photo+by+Alfons+Morales+on+Unsplash.jpg",
          "size": "full",
          "aspectMode": "cover",
          "backgroundColor": "#B25151"
        },
        "body": {
          "type": "box",
          "layout": "horizontal",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "前往誠品網路書店看更多",
                "uri": "http://www.eslite.com/search_BW.aspx?query=壓力"
              },
              "color": "#C36464",
              "height": "md",
              "style": "primary",
              "gravity": "center"
            }
          ]
        }
      }
    ]
  }
"""

from linebot.models import (
    FlexSendMessage, CarouselContainer)

import json

carouselContent = CarouselContainer.new_from_json_dict(json.loads(flexCarouselContainerJsonDict))
flexCarouselSendMeesage = FlexSendMessage(alt_text="壓力", contents=carouselContent)

template_message_dict = {
    "Book": flexCarouselSendMeesage}


Answer_list = []
dict_ID_USERS = {}
m = int(len(Answer_list)) + 1

# 每個人的狀態記下來用{ID:Q(n)}
# 不管輸入什麼都回應text的內容
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_profile = line_bot_api.get_profile(event.source.user_id)
    global m
    global sum
    global dict_ID_USERS
    if event.message.text == "ZA WARUDO":
        buttons_template_message = TemplateSendMessage(
            alt_text='"世界" 時間暫停!!',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/LYEVqxV.gif',
                title='"世界" 時間暫停!!',
                text='時間暫停了，你想做什麼',
                actions=[
                    URIAction(
                        label='看看自己現在在哪',
                        uri='https://line.me/R/nv/location/'),
                    URIAction(
                        label='逼喬瑟夫用隱者之紫拍念照',
                        uri='https://line.me/R/nv/camera/'
                    ),
                    URIAction(
                        label='看我跟承太郎打牌',
                        uri='https://www.youtube.com/watch?v=5NlsjWHHlfw'
                    ),
                    URIAction(
                        label='還是你要打電話給誰',
                        uri='https://line.me/R/calls'
                    )
                ]
            )
        )
        line_bot_api.reply_message(
            event.reply_token,
            [
                buttons_template_message
            ]
        )

    elif event.message.text == "Book":
        line_bot_api.reply_message(
            event.reply_token,
            template_message_dict.get(event.message.text)
        )

    elif event.message.text == "Wryyy":
        dict_ID_USERS.update([(user_profile.user_id, len(Answer_list))])
        print(dict_ID_USERS)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=Q[m], quick_reply=quickReplyList))
    elif event.message.text == "1" or event.message.text == "0":
        if user_profile.user_id not in dict_ID_USERS.keys():
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=Q[m], quick_reply=quickReplyList))
        elif user_profile.user_id in dict_ID_USERS.keys():
            if m < 12:
                m += 1
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=Q[m], quick_reply=quickReplyList))
                Answer_list.append(event.message.text)
                dict_ID_USERS.update([(user_profile.user_id, len(Answer_list))])
                print(dict_ID_USERS)
                print(Answer_list)
            elif m == 12:
                Answer_list.append(event.message.text)
                dict_ID_USERS.update([(user_profile.user_id, len(Answer_list))])
                sum = 0
                for t in Answer_list:
                    sum += int(t)
                print(sum)
                result = "完成了! 你的分數是 " + str(sum) + "分!!\n回答3個「是」：您的壓力指數還在能負荷的範圍。\n" \
                                                    "回答4~5個「是」：壓力滿困擾您，雖能勉強應付，但必需認真學習壓力管理了，同時多與良師益友聊一聊。\n" \
                                                    "回答6~8個「是」：您的壓力很大，趕快去看心理衛生專業人員，接受系統性的心理治療。\n" \
                                                    "回答9個以上「是」：您的壓力已很嚴重，應該看精神專科醫師，依醫師處方用藥物治療與心理治療，幫忙您的生活趕快恢復正常軌道。"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=result))
                Answer_list.clear() # 為甚麼清空了再次打Wryyy還是會m=12
                dict_ID_USERS.update([(user_profile.user_id, len(Answer_list))])
                print(dict_ID_USERS)
                m = len(Answer_list) + 1

    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))

# 存照片
from linebot.models import (
    ImageMessage
)


@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    # 請line_bot_api 把照片取回來
    message_content = line_bot_api.get_message_content(event.message.id)

    # 把照片存回本地端
    with open(event.message.id + '.jpg', 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
    # 請line_bot_api 回復用戶，收到消息了
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage('念照我就偷走啦! WRYYYYYY')
    )


# 影片或音檔
from linebot.models import (
    VideoMessage, AudioMessage
)


@handler.add(MessageEvent, message=VideoMessage)
def handle_video_message(event):
    # 請line_bot_api 把照片取回來
    message_content = line_bot_api.get_message_content(event.message.id)

    # 把照片存回本地端
    with open(event.message.id + '.mp4', 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
    # 請line_bot_api 回復用戶，收到消息了
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage('哪尼! 會動的念照...霸卡哪! 替身能力竟然提升了!')
    )




app.run(host='0.0.0.0', port=os.environ['PORT'])