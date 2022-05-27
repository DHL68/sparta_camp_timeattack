from django.shortcuts import render, redirect
from .models import UserModel_sparta

from django.http import HttpResponse


# user/views.py
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        username = request.POST.get('email', None)
        password = request.POST.get('password', None)

        # 조건문 @ 여부
        if not '@' == password:
             return HttpResponse("이메일 형식 에러", 401)

        else:
            new_user = UserModel_sparta()
            new_user.username = username
            new_user.password = password
            new_user.save()

            return HttpResponse("회원가입 완료")