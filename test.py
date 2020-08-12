x = int("5")+int("2")
print(x)


# 做一個TemplateButton 寫說 時間暫停了 接下來花個幾分鐘對自己做個小測驗 下面按鈕選擇"開始測驗"跟"下次再說吧"
# "開始測驗"就接下面的QuickReply，"下次再說"就給個提示或不給

# 測驗的選項
textQuickReplyButton1 = QuickReplyButton(
    action=MessageAction(
        label="1(都沒有)",
        text="1"))
textQuickReplyButton2 = QuickReplyButton(
    action=MessageAction(
        label="2(很少有)",
        text="2"))
textQuickReplyButton3 = QuickReplyButton(
    action=MessageAction(
        label="3(偶爾有)",
        text="3"))
textQuickReplyButton4 = QuickReplyButton(
    action=MessageAction(
        label="4(經常有)",
        text="4"))
textQuickReplyButton5 = QuickReplyButton(
    action=MessageAction(
        label="5(一直有)",
        text="5"))


quickReplyList = QuickReply([textQuickReplyButton1,
                             textQuickReplyButton2,
                             textQuickReplyButton3,
                             textQuickReplyButton4,
                             textQuickReplyButton5])

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if TextMessage == "壓力測驗":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="1. 這一個月來，您覺得心浮氣躁，不容易定下心。", quick_reply=quickReplyList))
 # 這裡輸入"壓力測驗"可以跳出QuickReplyButton 但前面的"ZA WORLD"功能就不見了