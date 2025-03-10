#!/usr/bin/env python
# -*- coding:utf-8 -*-
import ssl

# 认证失败把下面这一行注释解除
# ssl. create default https context = ssl. create unverified context

from qcloudsms_py import SmsMultiSender
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

from django.conf import settings

def send_sms_single(phone_num, template_id, template_param_list):
    """"
    单条发送短信
    :param phone_num:手机号
    :param template_id:腾讯云短信模板ID
    :param template_param_list:短信模板所需参数列表，例如:【验证码:{1}，描述:{2}】，则传递参数[888,666]按顺序去格式模板
    :return:
    """
    appid = settings.SMS_APPID
    appkey = settings.SMS_APPKEY
    sms_sign = settings.SMS_SIGN

    sender = SmsSingleSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num, template_id, template_param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}

    return response


def send_sms_multi(phone_num_list, template_id, param_list):
    """"
    批量发送短信
    :param phone_num_list:手机号列表
    :param template_id:腾讯云短信模板ID
    :param param_list:短信模板所需参数列表，例如:【验证码:{1}，描述:{2}】，则传递参数[888,666]按顺序去格式化模板
    :return:
    """
    appid = settings.SMS_APPID
    appkey = settings.SMS_APPKEY
    sms_sign = settings.SMS_SIGN

    sender = SmsMultiSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num_list, template_id, param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}

    return response
