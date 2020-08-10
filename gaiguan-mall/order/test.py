from alipay import AliPay
import os,time

app_private_key_string = open("order/app_private_key.pem").read()

alipay_public_key_string = open("order/alipay_public_key.pem").read()

# app_private_key_string == """
#         #     -----BEGIN RSA PRIVATE KEY-----
#         #     base64 encoded content
#         #     -----END RSA PRIVATE KEY-----
#         # """
#         #
#         # alipay_public_key_string == """
#         #     -----BEGIN PUBLIC KEY-----
#         #     base64 encoded content
#         #     -----END PUBLIC KEY-----
#         # """
# 初始化
alipay = AliPay(
    appid="2016102300747738",  # 应用id
    app_notify_url=None,  # 默认回调url
    app_private_key_string=app_private_key_string,
    # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    alipay_public_key_string=alipay_public_key_string,
    # app_private_key_path=os.path.join(settings.BASE_DIR, 'order/app_private_key.pem'),
    # app_public = "MIIEowIBAAKCAQEApndIrTUWCx1TCZTKQn+GxpObsnzyr3OGfg5GgmOrtaWsbF5byomgmcjF0ixqbkojf2VjOXRsQDsCKMC3Hb6hiqW6hEPDHl85VaZ8FgYuwKBDh3h3n5/jYkBXlhRuO7g9xBNg1j5cr8aqrppK6TuHbxawb7XjWCYNSRmacT/ufHgVqQIAuq3K48ES3POO10LjeFMHVKtKQBPqqdA38acaclxDXgY1YQIrMfppsVSUg7O9sZRY8uF6rCjdvUgjKSBjj6DFAVbG0uKuNLHkRvPjmXfDnJRtrwG07zLa8a/ZWeLxQ8v2Y+SHKdzd1U+31OFVxqhnSSsT9eeD4EsF7jb6vQIDAQABAoIBAGBzNLTG0WLXNsmSYC5vXVOpKskcBDEMKpzXAJuDzHWO7HxNn7mWTGtOHPBNs8z7P94MjJU5k48ToYijQHYHgemnZI5GBMOQQNQThknsgyIwuW/AqO7f4QuIZDcc11Hayk7VO4Jm16Uw4qwP0d+ZEjuXVdsj8/ma8o+sOgPsGu4aZockCDkOxejhJBDEJixD+vBH3oiNJO0goXYq1Q9RbUCLetDLwHDvz48Upq3B5ssFE6IL39QKx3j7uH57WLAU0EAqHn1vickM17dGsuglrUQvILMDHmNtiF1gszx/UrLnAauHVgymo6Z7Z0OMIxVPF4xMCN8/KQmVu4lVDzv/ZoECgYEA06jXWgt6C8jiM7lOhhZYlOI+r65ypX2aIZhavZNwoI4E+v+8pkFbcUYNssjCnOIFQ/18LQW7cBUhN7jYmm7oyFGhIdsvknWz/h8oaOV2Zdyit1qExwcRLyeZiWbYUAiOI3GQq6ZRiw27dlMa9YgA6eS41jQnf/TjrH4O1jzxCLUCgYEAyVa9vBbKQfPNLLzztGyZ5WKiTlDYXE9zMB49SJJue7ZiQz4gBWydNBc0prY+0teQHo9lNFBRB8l2zCk/PcoQVwIrVVMYBvliyIrovhQeBIHhEb60dx9gwvnHGtFYEVNQumNBL+iAWTF3y6wJTAoJg4KONQVRnpHx+0Gnl85MlukCgYEAzTGfbSU5MZmTag+ZB7c8M0JPAWQ+sx9cQHuCZM0+X/iu7WLmUcuEygDfINcujIc2EZ76Nm+bMmLZrDqgir9BH4q7iqYCrZs8Xv134JGsQb4vZU/07zpzt2JNn/47cQOKQORFG5OG9Cbg+SpCNYyfTiE17Dvtm0gfPMeMvLeh+Q0CgYBfMkc1xqTNOEQ7sf+cwHinj9JkKy+RvfMdvj6FsM7SabLeTmJ/jhJqTcqURLlBobC/8lcMvCkEAIrOD3aadY7yRNFOX6KNsZ62aY+QSBzFTs+nPz8+z7RFnCo7EN6OGpGh/0oUJ99/zLbysx4WOOy0pKcuhJxJ2IHMpgdi7KUj+QKBgAZxkNFZ2a2YRvUYfTx/mWsfa2EolkPmblVy13w8G5/iV9/cexDC6H4WM9ROizLjvjI2wvlajNJhqQowja0zmd8bg7ykyMKvvINEiJYb1dRXN4mqS5mM1rCIwxusI8mkdmcCpLG2tKLedqPfH2iMJgLVqoAE5UuT8isgq2JFY0d+",
    # alipay_public_key_path=os.path.join(settings.BASE_DIR, 'order/alipay_public_key.pem'), # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    sign_type="RSA2",  # RSA 或者 RSA2
    debug=True  # 默认False
)

# 调用支付接口
# 电脑网站支付，需要跳转到https://openapi.alipaydev.com/gateway.do? + order_string


# 返回应答
pay_url = 'https://openapi.alipaydev.com/gateway.do?'
