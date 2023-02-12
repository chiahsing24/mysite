from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.

def index(response, name):
    ls = TodoList.objects.get(name=name)
    item = ls.item_set.all().get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))
