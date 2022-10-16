from django.shortcuts import redirect, render
from .models import Advisor
import random

def landing(req):
    return render(req, 'landing.html')

def game(req):
    return render(req, 'game.html')

def answer(req):
    res = random.randint(1,4)
    return render(req, 'answer.html', {"res": res})

def result(req):
    return render(req, 'result.html')

def success(req):
    advisor_instance = Advisor()
    if req.method == 'POST':
        advisor_instance.shop_name = req.POST.get('shop_name')
        advisor_instance.phone_number = req.POST.get('phone_number')
        advisor_instance.instagram = req.POST.get('instagram')
        advisor_instance.position = req.POST.get('position')
        advisor_instance.collabo_number = req.POST.get('collabo_number')
        advisor_instance.address = req.POST.get('address')
        advisor_instance.save()
    return redirect('landing')
