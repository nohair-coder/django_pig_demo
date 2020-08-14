from django.http import JsonResponse

def SuccessResponse(param):
    return JsonResponse({'code': param, 'message': 'SUCCESS'},status=200)

def FailResponse(param):
    return JsonResponse({'code': param, 'message': 'ERROR'})