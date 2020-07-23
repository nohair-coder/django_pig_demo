from .models import User
from django.views import View
from django.http import JsonResponse
import json

# Create your views here.

class LoginCheck(View):
    def get(self, request):
        # user = User.objects.filter()
        print(1111)
        return JsonResponse({'code': 'success', 'message': '成功了'}, status=200)

    def post(self, request):
        req = json.loads(request.body)
        req_username = req['username']
        req_password = req['password']
        # print(req_username, req_password)
        if req_username and req_username:
            try:
                user = User.objects.filter(username=req_username).first()
                # print(req_password)
                if user.password == req_password:
                    return JsonResponse({"code": "SUCCESS", 'message': '登录成功'}, status=200)
                else:
                    return JsonResponse({'code': '登录失败'}, status=401)
            except:
                return JsonResponse({'code': '登录失败'}, status=401)
        else:
            return JsonResponse({'code': '登录失败'}, status=401)

    def put(self, request):
        person = User()
        person.username = request.GET.get('username')
        person.password = request.GET.get('password')
        person.email = request.GET.get('email')
        person.telephone = request.GET.get('telephone')
        person.sex = request.GET.get('sex')
        # print(person.username,person.password,person.email,person.telephone,person.sex)
        person.save()
        return JsonResponse({'code': 'success', 'message': '添加成功'}, status=200)

# addUser('admin',123456,13260666950,'male')
