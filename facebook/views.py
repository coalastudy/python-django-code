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

    diary = ['오늘은 날씨가 맑았다. - 4월 3일', '미세머지가 너무 심하다. (4월 2일)', '비가 온다. 4월 1일에 작성']

    return render(request, 'play2.html', { 'name': choidogeun, 'diary': diary, 'cnt': count, 'age': status })

def my_profile(request):
    return render(request, 'profile.html')

def event(request):
    choidogeun = '최도근'
    age = 20

    global count # 바깥영역의 변수를 사용할 때 global
    count = count + 1 # 접속할 때마다 방문자 1 증가

    if age > 19: # age가 19 보다 크면?
        status = '성인'
    else: # 성인이 아닌 경우
        status = '청소년'

    if count is 7:
        lottery = '당첨!'
    else:
        lottery = '꽝...'

    return render(request, 'event.html', { 'name': choidogeun, 'cnt': count, 'age': status, 'lottery': lottery })