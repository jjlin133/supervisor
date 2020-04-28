from django.shortcuts import render
from supervisorapp.models import Company
from django.http import HttpResponse

import logging
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from datetime import datetime
from flask import Flask
from flask import request
from flask import abort
from linebot.models import *
logger = logging.getLogger("django")

"""
line_bot_api = LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
parser  = WebhookParser(settings.LINE_CHANNEL_SECRET)
"""
app = Flask(__name__)

# 必須放上自己的Channel Access Token #ASIS機器人 2020.0418
line_bot_api = LineBotApi('6YO4sIvoxjcNIozLuKU7IBtnyofmyAfvY8+xiQqE0RWoCkakIXRkJt2PT4WF7zrgq7JDM7rnogrj3y90TGX+cvlnAVROQ2SPEx8Qx+qI0ASUYaY9rJyYkM38en7/XiSDYx8sBRX5NplreR9Q8i7ypAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('00a21f206bd05842de9fd9efb50a9af6') #ASIS機器人
# 必須放上自己的LINE Bot user ID 
line_bot_api.push_message('Uaa63a3f5feff2725536db7d81f09c929', TextSendMessage(text='可以開始連結Heroku'))

@csrf_exempt
@require_POST
def callback(request):
    signature = request.META['HTTP_X_Line_Signature']
    body = request.body.decode('utf-8')

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        messages = ( "Invalid signature. Please check your channel access token/channel secret.")
        HttpResponseForbidden()

    return HttpResponse('OK',status=200)


@handler.add(event=MessageEvent, message=TextMessage)
def handl_message(event: MessageEvent):
           line_bot_api.reply_message(
            reply_token=event.reply_token,
            messages=TextSendMessage(text=event.message.text),
        )
