from .models import StationInfo
from django.views import View
from django.http import JsonResponse
from app.pig_base.models import PigBase
import json


# Create your views here.
class Station(View):
    def post(self, request):
        try:
            req = json.loads(request.body)
            print(req)
            exist_S = StationInfo.objects.filter(build_unit_station=req).first()
            if exist_S == None:
                S = StationInfo()
                S.build_unit_station = req
                S.save()
                return JsonResponse({'code': '饲喂站添加成功'}, status=200)
            else:
                return JsonResponse({'code': '饲喂站已存在,请重新输入'}, status=201)
        except Exception as e:
            print(e)

    def get(self, request):
        try:
            try:
                req_pageIndex = request.GET['pageIndex']
            except Exception as e:
                # print(e)
                req_pageIndex = 1
            stationlist = StationInfo.objects.filter()
            station_options = list()
            all_station = list()
            for s in stationlist:
                s_info = dict()
                if s.status == '已关机':
                    s.status_num = False
                else:
                    s.status_num = True
                s_info['build_unit_station'] = s.build_unit_station
                s_info['status'] = s.status
                s_info['temperature'] = s.temperature
                s_info['humidity'] = str(s.humidity * 100) + '%'
                s_info['status_num'] = s.status_num
                all_station.append(s_info)
                station_options.append({
                    'value' : s_info['build_unit_station'],
                    'label' : s_info['build_unit_station']
                })
            # print(station_options)
            total = len(all_station)
            return JsonResponse({'all_station': all_station,
                                 'total': total,
                                 'station_options': station_options,
                                 "code": "SUCCESS"}, status=200)
            # return JsonResponse({'code': 'SUCCESS'})
        except:
            return JsonResponse({'code': 'error'}, status=201)

    def put(self, request):
        pass

    def delete(self, request):
        pass

class SystemCheck(View):
    def get(self, request):
        pig_num = PigBase.objects.filter().count()
        station_num = StationInfo.objects.filter().count()
        print(pig_num)
        print(station_num)
        return JsonResponse({'code': '获取成功','pig_num': pig_num, 'station_num': station_num}, status=200)
