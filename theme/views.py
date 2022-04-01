from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def news(request):
    return render(request, '실시간 뉴스정보.html')

def restarant(request):
    return render(request, '실시간 맛집정보.html')

def bicycle(request):
    return render(request, '실시간 따릉이정보.html')

def subway(request):
    return render(request, '실시간 열차정보.html')

def school(request):
    return render(request, '초 중 고.html')