from django.db import models

# Create your models here.
class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    email = models.EmailField(unique = True,max_length=32)
    telephone = models.BigIntegerField(unique = True)
    sex = models.CharField(max_length = 32, choices = gender, default = "男")
    create_time = models.DateField(auto_now_add = True)

    # class Meta:
    #     db_table = "tb_User"
    #     verbose_name = "用户"
    #     verbose_name_plural = "用户"

    class Meta:
        db_table = 'tb_users'  # 指明数据库表名
        verbose_name = '用户'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.username
