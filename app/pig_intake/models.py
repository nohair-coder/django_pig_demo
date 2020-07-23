from django.db import models

# Create your models here.
class PigIntake(models.Model):
    pigid = models.IntegerField(verbose_name='身份码')
    earid = models.IntegerField(verbose_name='耳标号')
    entrytime = models.DateTimeField(verbose_name='开始时间')
    outtime = models.DateTimeField(verbose_name='结束时间')
    feedquantity = models.CharField(max_length=20, default=0, verbose_name='采食量')

    class Meta:
        db_table = 'tb_pigintake'  # 指明数据库表名
        verbose_name = '母猪采食表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
