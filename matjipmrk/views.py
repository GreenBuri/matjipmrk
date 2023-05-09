from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Filter, Comment
from .forms import FilterForm, RestaurantForm
from django.utils import timezone
from django.http import HttpResponse
from django.core.paginator import Paginator
import pandas as pd
import numpy as np
import json

# Create your views here.

def home(request):
    restaurants = Restaurant.objects.all() #등록되어 있는 식당 객체를 모두 불러옵니다

    if Filter.objects.count() == 0: #Filter 모델의 객체가 생성되어 있지 않다면, 객체 생성!
        Filter.objects.create()
    option = get_object_or_404(Filter) #get_object_or_404를 호출하여 수정하고자 하는 filter 객체를 불러온다

    if request.method == 'POST':
        form = FilterForm(request.POST, instance=option)
        if form.is_valid(): #POST방식의 요청을 받은 경우, 입력받은 form이 유효하다면, 입력받은 form의 내용을 option에 저장하고 그 filter객체에 덮어씌워 저장한다.
            option=form.save(commit=False)
            option.save()
            return redirect(home)
    else:
        form = FilterForm() #POST방식이 아닌 GET 방식의 요청을 받은 경우, FilterForm()을 담아 form에 보낸다.

    # option에 따라 return할 식당 객체를 설정. 
    if option.korean == False:
        restaurants = restaurants.exclude(foodtype='korean')
    if option.chinese == False:
        restaurants = restaurants.exclude(foodtype='chinese')
    if option.japanese == False:
        restaurants = restaurants.exclude(foodtype='japanese')
    if option.western == False:
        restaurants = restaurants.exclude(foodtype='western')
    if option.etc == False:
        restaurants = restaurants.exclude(foodtype='etc')

    #게시물 리스트 만들기
    page = request.GET.get('page', 1) #입력 인자
    rst_list = Restaurant.objects.order_by('-create_date') #조회

    paginator = Paginator(rst_list, 7)
    page_obj = paginator.get_page(page)

    context = {'rst_list' : page_obj}

    #지도 데이터와 paginator 데이터 모두 넘기기.
    return render(request, 'matjipmrk/rst_home.html', {'restaurants':restaurants, 'form':form, 'rst_list':page_obj})
    #식당 정보를 모두 front(rst_home.html)로 넘겨줍니다.


def rst_detail(request, rst_id):
    rst = Restaurant.objects.get(id=rst_id)
    restaurants = Restaurant.objects.all()

    #댓글 리스트 만들기
    page = request.GET.get('page',1) 
    cmnt_list = Comment.objects.filter(rst_id=rst_id).order_by('-create_date')

    paginator = Paginator(cmnt_list, 3)
    page_obj = paginator.get_page(page)
    
    context = {'cmnt_list':page_obj}

    return render(request, 'matjipmrk/rst_detail.html', {'rst':rst, 'restaurants':restaurants, 'cmnt_list':page_obj})

def cmnt_create(request, rst_id):
    rst =Restaurant.objects.get(id=rst_id)
    # comment = Comment(board=board, content=request.POST.get('content'), creaimage.pngte_data=timezone.now())
    # comment.save()
    rst.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #위 표현이나 위 두줄 표현이나 같다!
    return redirect('matjipmrk:rst_detail', rst_id=rst.id)
    #redirect 는 render하고 다르게 데이터를 바인딩 해 보내는 것이 아니라, 현재 받은 함수 안의 board 정보의 id 값을 그대로 받아서 넘김.

def rst_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            rst = form.save(commit=False)
            rst.create_date = timezone.now()
            rst.save()
            return redirect('matjipmrk:home')
    else:
        form = RestaurantForm()
    return render(request, 'matjipmrk/rst_form.html', {'form':form})

def rst_delete(request, rst_id):
    rst = get_object_or_404(Restaurant, id=rst_id)
    rst.delete()
    return redirect('matjipmrk:home')

def cmnt_delete(request, cmnt_id, rst_id):
    cmnt = get_object_or_404(Comment, id=cmnt_id)
    cmnt.delete()
    return redirect('matjipmrk:rst_detail', rst_id)

def rst_search(request):
    return render(request, 'matjipmrk/rst_search.html')