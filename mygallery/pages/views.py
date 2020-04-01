from django.shortcuts import render
import requests


# Create your views here.
def pages(request):
    return render(request, 'index.html')

def gallery(request):
    # Unsplash
    text = request.GET['text'] # 여기 text 는 form 로 가져온 친구..
    item = request.GET['item'] # 몇개 검색해줄지...
    # 과제 제출용이니 내 key 숨기는법 몰라서 그냥 올립니다..흑흑.. env.. decouple... 몰라...
    p_key = '공개키 비공개' # 내 공개 키
    api = f'https://api.unsplash.com/search/photos?query={text}&client_id={p_key}&per_page={item}'

    a = requests.get(api).json()['results']

    images = []
    for i in range(len(a)):
        aa = a[i]['urls']['regular']  
        images.append(aa)


    context = {
        'text': text,
        'images': images,
    }
    return render(request, 'gallery.html', context)
