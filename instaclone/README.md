# :heart: 인스타클론 Project :heart:

> 파이썬 버전 3.6.4
>
> Django 버전 2.1.15



## :one: 프로젝트 생성

- **Django 설치 ( 버전 2.1.15 )**

```shell
$ pip install django==2.1.15
```



- **프로젝트 생성**

```shell
$ django-admin startproject instaclone
# django-admin startproject [프로젝트명]
```

`git bash` 을 열고 프로젝트를 만들고싶은 경로로 이동한후에 `instaclone` 이라는 프로젝트를 생성해준다.



- **프로젝트 구조**

```bash
instaclne
├── instaclone
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
```



## :two: 초기 셋팅

> ```shell
> $ pip install django-bootstrap4
> $ pip install django-extensions ipython # python manage.py shell_plus
> ```



- **settings.py**

```python
# 호스트를 일단 * 모두 받아들인다.
ALLOWED_HOSTS = ['*']

# 인스톨드 앱 설정
INSTALLED_APPS = [
    bootstrap4,
]

# 루트 Templates 폴더 경로를 설정해준다.
TEMPLATES = [
    {'DIRS': [ os.path.join(BASE_DIR, 'templates') ],} 
]
    
# 언어 & 시간 설정
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'    
```



- **루트 디렉토리에 Templates 폴더를 생성한다.**
  - 그 안에 `base.html` 파일을 만들어준다.
  - `base.html`
  - DTL ( 장고 템플릿 랭귀지 ) 는 따로 언급하지 않는다.

```html
<!DOCTYPE html>
{% load bootstrap4 %}
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  {% bootstrap_css %}
</head>
<body>

  <!-- 본문 -->
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>

  {% bootstrap_javascript jquery='full' %}
</body>
</html>
```



## :three: Accounts 앱 생성

> 앱을 생성하고 나면 앱 폴더안에
>
> `urls.py` 와 `forms.py` 파일을 생성해주고 세팅 해야 한다.



- 각 기능을 수행하는 앱을 생성한다.
  - 사용자들을 관리할 `accounts` 생성

```shell
$ python manage.py startapp accounts
# python manage.py startapp [앱이름]
```



- **settings.py 에 앱을 추가한다.**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'accounts',
]
```



- **`instaclone/urls.py`**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
```



- **`accounts/urls.py`**

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
]
```



- **`accounts/models.py`**

```python
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name='followings'
        )
```

