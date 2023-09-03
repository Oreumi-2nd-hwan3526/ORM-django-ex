from django.shortcuts import render

# Create your views here.
def index(request):
    item = {'items': ["사과", "바나나", "수박"], 'item2': "문서의 끝입니다."}
    return render(request, 'index.html', item)

def new_page(request):
    return render(request, 'oreumi_page.html')

def new_page2(request):
    return render(request, 'oreumi_page2.html')