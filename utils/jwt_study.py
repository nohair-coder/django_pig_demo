import jwt
from jwt import exceptions
import datetime
from django.http import JsonResponse

salt = 'HZAU'
token = ''


def create_token(parm):
    salt = 'HZAU'
    headers = {
        "alg": "HS256",
        "typ": "JWT"
    }
    payload = {
        "sub": "1234567890",  # 设置为id       parm.id
        "name": "John Doe",  # 设置为用户名    parm.user
        "iat": 1516239022  # 超时时间
        # 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)  # 设置超时时间1分钟
    }
    global token
    token = jwt.encode(payload=payload, key=salt, algorithm='HS56', headers=headers).decode('utf-8')


def check_token():
    msg = None
    verified_payload = None
    try:
        verified_payload = jwt.decode(token, salt, True)
        return verified_payload
    except exceptions.ExpiredSignatureError:
        msg = 'token失效'
    except exceptions.DecodeError:
        msg = 'token认证失败'
    except jwt.InvalidTokenError:
        msg = '非法token'
    if not verified_payload:
        return JsonResponse({'code': '登录失败'}, status=201)
    else:
        print(verified_payload['sub'], verified_payload['name'])
        return JsonResponse({'code': '登录成功'}, status=200)


