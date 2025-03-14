from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.

def index(request):
    feature1 = Feature()
    feature1.id=0
    feature1.name='Fast'
    feature1.details='Our Service is very Quick'

    feature2 = Feature()
    feature2.id=1
    feature2.name='Reliable'
    feature2.details='Our Service is very Reliable'

    feature3 = Feature()
    feature3.id=2
    feature3.name='Easy to use'
    feature3.details='Our Service is very easy to use'

    feature4 = Feature()
    feature4.id=3
    feature4.name='Affordable'
    feature4.details='Our Service is very affordable'

    feature5 = Feature()
    feature5.id=4
    feature5.name='Trustworthy'
    feature5.details='Our Service is very affordable'
    icons=['bi bi-easel','bi bi-gem','bi bi-geo-alt','bi bi-command']
    features=[feature1,feature2,feature3,feature4,feature5]

    zipped_item=zip(features,icons)

    return render(request,'index.html',{'zipped_item': zipped_item})

def counter(request):
    words=request.POST['words']
    
    return render(request,'counter.html',{'length': words })

