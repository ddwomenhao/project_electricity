# coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseNotAllowed
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from df_user.models import Passport
from hashlib import sha1
# Create your views here.

'''
def require_GET(view_func):
    def wrapper(request, *view_args, **view_kwargs):
        if request.method == 'GET':
            return view_func(request, *view_args, **view_kwargs)
        else:
            return HttpResponseNotAllowed()
    return wrapper

def require_POST(view_func):
    def wrapper(request, *view_args, **view_kwargs):
        if request.method == 'POST':
            return view_func(request, *view_args, **view_kwargs)
        else:
            return HttpResponseNotAllowed('error')
    return  wrapper
'''

#@require_GET request.method
@require_http_methods(['GET','POST'])
def register(request):
    '''
    展示用户注册页面
    '''
    return render(request, 'register.html')


@require_POST
def register_handle(request):
    '''
    注册用户信息
    '''
    # 1.接收用户的注册信息
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    # 2.创建新用户 add_one_passport(username, password, email) objects
    Passport.objects.add_one_passport(username=username, password=password, email=email)

    # 跳转到首页
    return redirect('/')


def check_username_exist(request):
    '''
    校验用户名是否已经注册
    '''
    # 1.接收用户名
    username = request.GET.get('username')
    #print username
    # 2.根据用户名查找账户信息 get_passport_by_username(username) return None
    passport = Passport.objects.get_one_passport(username=username)
    if passport:
        # 用户名已注册
        return JsonResponse({'res':0})
    else:
        # 用户名可用
        return JsonResponse({'res':1})


















