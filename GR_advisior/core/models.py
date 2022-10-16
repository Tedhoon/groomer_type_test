from django.db import models

class Advisor(models.Model):
    shop_name = models.CharField('샵 이름', max_length=100)
    phone_number = models.CharField('전화번호', max_length=100)
    instagram = models.CharField('인스타그램 아이디', max_length=100)
    position = models.CharField('운영 방식', max_length=100)
    collabo_number = models.CharField('함께 쓸 인원 수(본인포함)', max_length=100)
    address = models.CharField('배송지', null=True, blank=True, max_length=200)
    

