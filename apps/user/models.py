from django.db import models

# Create your models here.
import datetime

from django.contrib.auth.models import  AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    username = models.CharField(max_length=255, null=False, blank=False, verbose_name=u"用户名",unique=True)
    password = models.CharField(max_length=255, null=False, blank=False, verbose_name=u"密码")
    gender=models.CharField(choices=(("male",u"男"),("female",u"女")),default="male",max_length=20,verbose_name=u"性别")
    mobile=models.CharField(max_length=11,null=True,blank=True,verbose_name=u"手机号")
    image=models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100,verbose_name=u"头像")
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name=u"邮箱",unique=True)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name
        #db_table = 'zy_user'
        #app_label='zy_user'

class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name=u"验证码")
    email=models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type=models.CharField(choices=(("register",u"注册"),("forget",u"找回密码")),max_length=100,verbose_name=u"验证码类型")
    send_time=models.DateTimeField(default=datetime.datetime.now,verbose_name=u"发送时间")

    class Meta:
        verbose_name=u"邮箱验证码"
        verbose_name_plural=verbose_name

class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name=u"标题")
    image=models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播图",max_length=100)
    url=models.URLField(max_length=200,verbose_name=u"访问地址")
    index=models.IntegerField(default=100,verbose_name=u"顺序")
    add_time=models.DateTimeField(default=datetime.datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"轮播图"
        verbose_name_plural=verbose_name