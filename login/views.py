from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse
from login import models
from django.contrib.auth.decorators import login_required


# Create your views here.

# 登录页面
def login(request):
    return render(request, 'login.html')

# 登录处理
def login_action(request):
    if request.method == 'POST':
        # 从请求中获取邮箱
        email = request.POST.get('email')
        print(email)
        # 从请求中获取密码
        password = request.POST.get('password')
        print(password)
        # 用户信息校验
        # 根据用户输入的邮箱进行查找
        user = models.UserInfo.objects.get(email=email)
        result = user.password
        if password == result:
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'error':'帐号或密码错误'})

# 注册页面
def registration(request):
    return render(request, 'registration.html')

# 注册处理
def sign(request):
    if request.method == 'POST':
        # 从请求中获取邮箱
        email = request.POST.get('email')
        # 从请求中获取用户名
        username = request.POST.get('username')
        # 从请求中获取密码
        password = request.POST.get('password')
        # 判断是否有相同的邮箱在数据库内
        em = models.UserInfo.objects.filter(email=email)
        if em:
            # 有相同数据，则注册失败
            return render(request, 'registration.html', {'error': '该邮箱已经注册'})
        else:
            models.UserInfo.objects.create(email=email, username=username, password=password)
            return render(request, 'login.html', {'data': '注册成功,请登录'})

# 首页页面
@login_required
def index(request):
    return render(request, 'index.html')

# 星标项目页面
@login_required
def startproject(request):
    return render(request, 'StarProject.html')

# 404
def page_not_found(request):
    return render_to_response('error-404.html')

# 500
def server_error(request):
    return render_to_response('error-500.html')

# 400
def bad_request(request):
    return render_to_response('error-400.html')
