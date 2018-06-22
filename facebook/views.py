from django.shortcuts import render

# Create your views here.

def play(request):
    return render(request, 'play.html')

count = 0
def play2(request):
    choidogeun = '최도근'
    age = 20

    global count # 바깥영역의 변수를 사용할 때 global
    count = count + 1 # 접속할 때마다 방문자 1 증가

    if age > 19: # age가 19 보다 크면?
        status = '성인'
    else: # 성인이 아닌 경우
        status = '청소년'

    return render(request, 'play2.html', { 'name': choidogeun, 'cnt': count, 'age': status })