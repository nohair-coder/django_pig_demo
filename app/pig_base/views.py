from .models import PigBase
from ..food_quantity.models import FoodQuantity
from django.http import JsonResponse
from django.views import View
import json
import datetime

def algo_backfat(backfat):
    algo_intake = backfat * 2
    return algo_intake

# Create your views here.
class PigBaseCheck(View):
    def post(self, request):
        req = json.loads(request.body)
        # print(req)
        exist_pig = PigBase.objects.filter(stationid=req['pig_stationid'], earid=req['earid'], decpigtime=None)
        if exist_pig:
            return JsonResponse({'code': '猪只已存在，请重新输入'}, status=201)
        else:
            P = PigBase()
            P.stationid = req['pig_stationid']
            P.pigid = req['pigid']
            P.earid = req['earid']
            P.breedtime = req['breedtime']
            P.malepignum = req['malepignum']
            P.pigkind = req['kind']
            P.gesage = req['gesage']
            P.vaccine = ','.join(req['vaccine'])
            print(req['vaccine'])
            P.save()
            F = FoodQuantity()
            try:
                F.backfat = req['backfat']
                F.algo_quantity = algo_backfat(float(req['backfat']))
            except:
                F.backfat = '—'
            F.pigid = req['pigid']
            F.earid = req['earid']
            F.save()
            return JsonResponse({'code': '入栏成功'}, status=200)

    def get(self, request):
        req = request.GET['id']
        piglist = PigBase.objects.filter(stationid=req,decpigtime=None)
        stationpig = list()
        for s in piglist:
            s_info = dict()
            s_info['stationid'] = s.stationid
            s_info['pigid'] = s.pigid
            s_info['earid'] = s.earid
            s_info['pigkind'] = s.pigkind
            s_info['backfat']= FoodQuantity.objects.get(pigid=s.pigid).backfat
            s_info['malepignum'] = s.malepignum
            s_info['gesage'] = s.gesage
            s_info['vaccine'] = s.vaccine
            # s_info['id'] = s.pigid
            s_info['breedtime'] = s.breedtime
            stationpig.append(s_info)
            # print(stationpig)
        return JsonResponse({'code':'获取pigbase成功', 'stationpig': stationpig},status=200)

    def put(self, request):
        req = json.loads(request.body)
        print(req)
        req_pigid = req['pigid']
        req_newstation = req['newstation']
        change_pig = PigBase.objects.get(pigid=req_pigid)
        change_pig.stationid = req_newstation
        change_pig.save()
        return JsonResponse({'code': '转栏成功'},status=200)

    def delete(self, request):
        now_time = datetime.datetime.now().strftime('%F')
        req = json.loads(request.body)
        req_pigid = req['pigid']
        print(req_pigid)
        sub_pig = PigBase.objects.get(pigid=req_pigid)
        sub_pig.decpigtime = now_time
        sub_pig.save()
        return JsonResponse({'code': '离栏成功'}, status=200)

    def patch(self,request):
        req = json.loads(request.body)
        req_pigid = req['pigid']
        req_newearid = req['newearid']
        print(req_pigid)
        print(req_newearid)
        change_pig = PigBase.objects.get(pigid=req_pigid)
        change_pig.earid = req_newearid
        change_pig.save()
        return JsonResponse({'code': '更换成功'}, status=200)
