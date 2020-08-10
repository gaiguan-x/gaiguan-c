from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django_redis import get_redis_connection
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from order.models import *
from django.conf import settings
from django.urls import reverse

import logging
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest


# /order/alipay
class AlipayView(LoginRequiredMixin, View):
    """支付宝支付"""

    @staticmethod
    def sign(logger=None):
        # 构造签名基础参数
        alipay_client_config = AlipayClientConfig(sandbox_debug=True)
        alipay_client_config.app_id = settings.ALIPAY_APPID
        alipay_client_config.app_private_key = settings.APP_PRIVATE_KEY
        alipay_client_config.alipay_public_key = settings.ALIPAY_PUBLIC_KEY
        client = DefaultAlipayClient(alipay_client_config, logger)
        return client

    @staticmethod
    def logger():
        """初始化日志"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(levelname)s %(message)s',
            filemode='a', )
        logger = logging.getLogger('')
        return logger

    def post(self, request):
        # 获得支付宝客户端
        client = AlipayView.sign()
        # 构造请求参数
        model = AlipayTradePagePayModel()
        model.out_trade_no = order_id
        model.total_amount = str(order.total_price)
        model.subject = "天天生鲜订单支付"
        model.timeout_express = str(settings.ALIPAY_TIMEOUT_MINUTE) + 'm'

        pay_request = AlipayTradePagePayRequest(biz_model=model)
        url = 'http://121.40.139.86:8000' + reverse('order:alipay_result')
        pay_request.notify_url = url  # 支付后回调地址
        pay_url = client.page_execute(pay_request, http_method='GET')  # 获取支付链接
        return JsonResponse({'res': 0, 'msg': '正在支付中...', 'url': pay_url})


# /order/alipay_result
class AlipayResult(View):
    def check_pay(self, params):  # 定义检查支付结果的函数
        from alipay.aop.api.util.SignatureUtils import verify_with_rsa
        sign = params.pop('sign', None)  # 取出签名
        params.pop('sign_type')  # 取出签名类型
        params = sorted(params.items(), key=lambda e: e[0], reverse=False)  # 取出字典元素按key的字母升序排序形成列表
        message = "&".join(u"{}={}".format(k, v) for k, v in params).encode()  # 将列表转为二进制参数字符串
        # with open(settings.ALIPAY_PUBLIC_KEY_PATH, 'rb') as public_key: # 打开公钥文件
        try:
            #     status =verify_with_rsa(public_key.read().decode(),message,sign) # 验证签名并获取结果
            status = verify_with_rsa(settings.ALIPAY_PUBLIC_KEY.encode('utf-8').decode('utf-8'), message,
                                     sign)  # 验证签名并获取结果
            return status  # 返回验证结果
        except:  # 如果验证失败，返回假值。
            return False

    def post(self, request):
        """支付宝POST回应"""
        params = request.POST.dict()  # type: dict
        if self.check_pay(params):  # 调用检查支付结果的函数
            '''
                此处编写支付失败后的业务逻辑
            '''
            return HttpResponse('success')  # 返回成功信息到支付宝服务器
        else:
            '''
                此处编写支付失败后的业务逻辑
            '''
            print('支付失败!')
            return HttpResponse('')

    def get(self, request):
        """支付宝的GET回应"""
        params = request.GET.dict()  # 获取参数字典
        if self.check_pay(params):  # 调用检查支付结果的函数
            '''
                此处编写支付成功后的业务逻辑
            '''
            return HttpResponse('支付成功！')
        else:
            '''
                此处编写支付失败后的业务逻辑
            '''
            return HttpResponse('支付失败！')


from alipay.aop.api.domain.AlipayTradeQueryModel import AlipayTradeQueryModel
from alipay.aop.api.request.AlipayTradeQueryRequest import AlipayTradeQueryRequest
from alipay.aop.api.response.AlipayTradeQueryResponse import AlipayTradeQueryResponse
import time


# /order/alipay_check
class AlipayCheck(LoginRequiredMixin, View):
    """支付宝结果用户查询"""

    def post(self, request):
        """查询POST请求"""
        while True:
            # 检测订单状态
            if order.order_status > 1:
                print('支付宝内部修改成功!')
                return JsonResponse({'res': 0, 'msg': '支付成功!'})
            # 发送查询请求
            client = AlipayView.sign(AlipayView.logger())

            # 构造请求对象
            model = AlipayTradeQueryModel()
            model.out_trade_no = order_id
            req = AlipayTradeQueryRequest(biz_model=model)

            # 执行请求操作
            try:
                response_content = client.execute(req)
            except Exception as e:
                return JsonResponse({'res': -1, 'msg': e})
            if response_content:
                # 解析响应结果
                response = AlipayTradeQueryResponse()
                response.parse_response_content(response_content)
                # 响应成功的业务处理
                if response.is_success():
                    # 成功
                    if response.trade_status == 'TRADE_SUCCESS':
                        return JsonResponse({'res': 0, 'msg': '支付成功!'})
                    # 等待付款
                    elif response.trade_status == 'WAIT_BUYER_PAY':
                        time.sleep(settings.ALIPAY_TIMEOUT_SLEEP_SECS)
                        continue
                    else:
                        return JsonResponse({'res': -1, 'msg': '支付失败'})
                # 等待创建交易
                elif response.code == '40004':
                    # 创建交易超时
                    if (expire_time > settings.ALIPAY_TIMEOUT_MINUTE * 60):
                        return JsonResponse({'res': -1, 'msg': '创建交易超时'})
                    expire_time += settings.ALIPAY_TIMEOUT_SLEEP_SECS
                    time.sleep(settings.ALIPAY_TIMEOUT_SLEEP_SECS)
                    continue
                else:
                    return JsonResponse({'res': -1, 'msg': '支付失败'})