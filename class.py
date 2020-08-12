from flask import Flask, request, abort
import linebot

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, TemplateSendMessage, ButtonsTemplate,
URIAction
)


class Templete_Button():
    def handle_image_message(event):
        if event.message.text == "ZA WORLD":
            buttons_template_message = TemplateSendMessage(
                alt_text='"世界" 時間暫停!!',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/LYEVqxV.gif',
                    title='"世界" 時間暫停!!',
                    text='時間暫停了，你想做什麼',
                    actions=[
                        URIAction(
                            label='看看你現在在哪',
                            uri='https://line.me/R/nv/location/'),
                        URIAction(
                            label='叫喬瑟夫用隱者之紫拍念照',
                            uri='https://line.me/R/nv/camera/'
                        ),
                        URIAction(
                            label='聽我唱歌',
                            uri='https://www.youtube.com/watch?v=ShR6QEn1QWQ'
                        ),
                        URIAction(
                            label='打電話',
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
    # 存照片
    from linebot.models import(
        ImageMessage
    )
    @handler.add(MessageEvent, message=ImageMessage)
    def handle_image_message(event):

        # 請line_bot_api 把照片取回來
        message_content = line_bot_api.get_message_content(event.message.id)

        # 把照片存回本地端
        with open(event.message.id+'.jpg', 'wb') as fd:
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
            TextSendMessage('哪尼! 會動的念照...不可能! 你的替身能力竟然提升了!')
        )