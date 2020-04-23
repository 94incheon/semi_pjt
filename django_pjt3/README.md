# PJT

## 1 기본 환경설정세션,accounts

- 드라이버 : 강재구, 네비 : 나윤지

- settings.py

  - host [*]
  - django_extensions
  - template- os.path.join
  - ko-kr
  - Asia/Seoul

- template-base.html

  - bootstrap4

- accounts - 앱 설치

- url - index - accounts에 index가 없는 것을 감지. 네비에서 있다는 것. 

  account, community 무엇을 처음 만들까 다시 고민...

- community앱을 만들기로 함.

- url등록.

- Model 만들기

- Form

- admin 등록 -   4번 완료.

   list_filter = ['created_at'] - 옵션 적용.

> :red_circle:주의사항
>
> settings.py
>
> django_extensions 복수형.
>
> 전체적인 흐름을 먼저 보고 어떤 앱부터 짤 지 대략적인 앱의 세부사항들은 확인 해보기.
>
> accounts의 경우 index.html이 아닌 nav에서 활용되고 있음. 

> amdin.py
>
> ```python
> admin.site.register(Review,Comment, CommentAdmin) -> 안됨.
> 
> 각각 같은 모델과 클래스를 같이 넘겨준다.
> admin.site.register(Review, ReviewAdmin)
> admin.site.register(Comment, CommentAdmin)
> ```
>
> 

## 2 community

- 드라이버 : 나윤지, 네비 : 강재구
- model - review, comment
- form 
- community 앱 url 모두 만들기. - 안쓰는 것들은 주석처리.
- view.py :  index, create, 나머지는 pass
  - create - method POST, else분기처리. 로그인 하지 않았을 경우는 추후 처리예정.indexhtml이 아닌 revie_list.html으로 변경.
- html - create와 연결되는 forms.html - bootstrap4소스를 이용.
- template - base : 기본 네비 구성 bootstrap 소스 참고.

>:red_circle:주의사항
>
>forms.py
>
>from django import forms 짧지만 장고에서 임포트 하는 폼스!

>base.html
>
>href가 아직 만들어 지지 않았을 경우 비워둔다.
>
>```html
><aclass="nav-item nav-link" href="">로그인</a>
>```

## 3.accounts

- 같이 다함

- from django.contrib.auth import login as auth_login

  from django.contrib.auth import logout as auth_logout

>:red_circle:주의사항
>
>장고 User모델을 쓸 경우 따로 models과 forms 설정이 필요하지 않다.
>
>authenticated는 값! 함수가 아님!

## 4.comments

- 같이

> :red_circle:주의사항
>
> @데코레이션을 이용하면 login페이지로 자동 ~

