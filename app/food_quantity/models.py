from django.db import models
import datetime
# Create your models here.

class FoodQuantity(models.Model):
    now_time = datetime.datetime.now().strftime('%F')
    pigid = models.CharField(max_length=16, verbose_name='身份码')
    backfat = models.CharField(max_length=20,verbose_name='背膘厚',null=True)
    index_quantity = models.FloatField(verbose_name='默认饲喂量',default=1)
    algo_quantity = models.FloatField(verbose_name='计算饲喂量',null=True)
    set_quantity = models.FloatField(verbose_name='设置饲喂量',null=True)
    settime = models.DateField(default=now_time, verbose_name='设置日期')

    class Meta:
        db_table = 'tb_foodquantity'  # 指明数据库表名
        verbose_name = '饲喂量'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
