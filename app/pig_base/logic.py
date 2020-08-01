from ..station.models import StationInfo
from .models import PigBase
from ..food_quantity.models import FoodQuantity, Backfat


def algo_backfat(backfat):
    """
    依据背膘厚计算出的饲喂量，算法饲喂量
    :param backfat:
    :return:
    """
    algo_intake = backfat * 2
    return algo_intake

def write_pigbase(req):
    """
    把数据写入母猪基础表
    :param req:
    :return:
    """
    P = PigBase()
    P.stationid = StationInfo.objects.get(build_unit_station=req['Build_Unit_StationId'])
    P.pigid = req['PigId']
    P.earid = req['EarId']
    P.breedtime = req['BreedTime']
    P.malepignum = req['MalePigId']
    P.gesage = req['GestationalAge']
    P.save()
    # print('write_pigbase')

def write_backfat(req):
    """
    把数据写入背膘厚表
    :param req:
    :return:
    """
    B = Backfat()
    B.pigid = PigBase.objects.get(pigid=req['PigId'])
    if req['BackFat'] != '':
        B.backfat = req['BackFat']
    else:
        B.backfat = None
    B.save()
    # print('write_backfat')

def write_foodquantity(req):
    """
    把数据写入饲喂量表
    :param req:
    :return:
    """
    F = FoodQuantity()
    F.pigid = PigBase.objects.get(pigid=req['PigId'])
    if req['BackFat'] != '':
        F.backfat = req['BackFat']
        F.algo_quantity = algo_backfat(float(req['BackFat']))
    else:
        F.backfat = None
    F.save()
    # print('write_foodquantity')

def is_none(backfat):
    '''
    背膘厚不是 None
    :param param:
    :return:
    '''
    return backfat if backfat != None else '-'