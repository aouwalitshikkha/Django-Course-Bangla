## ক্লাস - ১৯-২২ এর ডকুমেন্টেশন
 
এই মডিউলে মুলত আমরা এম ভিটির সাথে পরিচিত হব । MVT = Models , View , Template

এই মডিউল ৩ এ আমরা মুলত একটি সিম্পল ব্লগ হোম পেজ তৈরী করব । আর এর মাধ্যমেই MVT এর ধারনা ক্লিইয়ার করব । 

1.  Step -1: প্রজেক্টের শুরুতেই আপনাকে ভার্চুয়াল এনভায়রনমেন্ট ক্রিয়েট করতে হবে । ভার্চুয়াল এনভায়রনমেন্ট ক্রিয়েট করার জন্য আপনাকে গিটব্যাশে কমান্ড লিখতে হবে । এরপর সেই ভার্চুয়াল এনভায়রনমেন্ট এক্টিভ করতে হবে । পরবর্তীতে আমরা সেখানে জ্যাংগো ইন্সটল করব । কমান্ড নিচে দেওয়া হল । এক্টির পর একটি কমান্ড রান করুন । 

```python 
python -m venv env
source env/Scripts/activate
pip install django
```
2. Step -2: এই ধাপে আপনাকে প্রজেক্ট ও এপস ক্রিয়েট করতে হবে । ভার্চুয়াল এনভায়রনমেন্ট এক্টিভ থাকা অবস্থায় প্রজেক্ট ও এপস ক্রিয়েট করার জন্য নিচের কমান্ড রান করুন ।  পাশাপাশি টেমপ্লেট ডিরেক্টরি তৈরী ও index.html ফাইল তৈরী করার জন্য কমান্ড 
```python
django-admin startproject shome
cd shome 
python manage.py startapp blog
mkdir templates
cd templates 
touch index.html
cd ..
python manage.py runserver
```

ব্রাউজারে localhost:8000 লিখলেই আপনার জ্যাংগো সঠিকভাবে ইন্সটল হয়েছে কিনা দেখতে পারবেন । 

3. Step -3 এই ধাপে আপনাকে প্রজেক্টের সাথে এপস কনফিগ করে নিতে হবে । ভিএস কোডে ফোল্ডার ওপেন করার জন্য আপনাকে গিটব্যাশে টাইপ করতে হবে code . সেটিংস ফাইলে এপস এর নাম যুক্ত করতে হবে। টেমপ্লেট ফোল্ডার কনফিগ করে নিতে হবে । নিচের মত করে 

```python 
#shome/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'
]
# Line 58 
'DIRS': [BASE_DIR / 'templates'],
```

4. shome/urls.py এ নতুন ভাবে ইম্পোর্ট করতে হবে include ফাংশন । আর যুক্ত করতে নতুন পাথ । নতুন পাথ সহ ফাইলে কোড থাকবে নিচের মত 

```python
# shome/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]
```

এখানে আমরা path('', include('blog.urls')) এই লাইনে ব্লগের ইউ আর এলস ফাইলকে কল করেছি । কিন্তু এই ধরনের কোন ফাইল আমাদের নেই । সেইজন্য blog ফোল্ডারে urls.py নামে একটা ফাইল তৈরী করতে হবে । ফাইল তৈরী করার পর আপনাকে নিচের কোডটি blog/urls.py ফাইলে লিখতে হবে . 

```python 
# blog/urls.py 

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name ="home")
]

```

উপরের কোডের সেকেন্ড লাইনে আমরা views.py ফাইলকে ইম্পোর্ট করেছি । urlpatterns লিস্টে আমরা home_view নামে একটা ফাংশনকে কল করেছি । 

5. Step-5: যেহেতু আমরা এর আগে home_view নামে একটা ফাংশন তৈরী করেছি তাই আমাদের এই নামে একটা ফাংশন তৈরী করতে হবে । ফাংশনটি নিচের কোডে দেওয়া হল । 


```python
from django.shortcuts import render

def home_view(request):
    context = {}
    return render(request, 'index.html', context)
```

6. STEP-6 এই সেকশনে আমরা মডেল তৈরী করব । মডেলের সহজ অর্থ হচ্ছে ডাটাবেস। তার অর্থ হচ্ছে আমাদের ডাটাবেস তৈরী করতে হবে । ডাটাবেস তৈরী করার জন্য আমরা blog/models.py ফাইলে চলে যাব । মডেলস ফাইলে আমরা নিচের কোডটি লিখব । 

```python
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
```

এখানে  class Blog এ Blog হচ্ছে মডেলের নাম ।  এরপর ব্রাকেটের মধ্যে models.Model কে ইনহেরিট করবে । ইনহেরিট্যান্স নিয়ে আমরা পরবর্তীতে আলোচনা করব । এরপরের লাইন গুলা ডটাবেসের ফিল্ড গুলাকে নির্দেশ করে । টাইটেল ফিল্ড কে আমরা ক্যারেক্টার ফিল্ড হিসাবে নিব । এইজন্য লিখব title = models.CharField(max_length=200) এবং description যেহেতু লিমিটলেস তাই আমরা এইটাকে TextField হিসাবেই দিব । 

এরপর আমরা এইটাকে মাইগ্রেট করতে হবে । মাইগ্রেট আসলে ডাটাবেস বা এসকিউএল কমান্ড । এইজন্য আমাদের এসকিউএল এ কাজ করতে হবে না। জ্যাংগোর কমান্ডের সাহায্যেই এই কাজ করা সম্ভব । এইজন্য আমরা দুইটা কমান্ড দিব । কমান্ড গুলা নিচে দেওয়া হল

```python 
python manage.py makemigrations 
python manage.py migrate
```

এর ফলে ডাটাবেস তৈরী হবে । আপনার প্রজেক্ট ফোল্ডারে দেখতে পারবেন db.sqlite3 নামে একটা ফাইল তৈরী করা হয়েছে । যেখানে ডাটাবেসের টেবিল গুলা আছে । ডাটাবেসের টেবিল গুলা দেখার জন্য SQLITE Viewer নামে VSCode এ একটা এক্সটেনশন পাওয়া যায় । 


7. Super User তৈরী ঃ আমরা প্রজেক্ট urls.py ফাইলে admin/ নামে একটা ইউ আর এল দেখতে পেয়েছি । এই ইউ আর এল প্রবেশ করলে লগিন দেখায়। কিন্তু লগিন করার জন্য আমাদের আইডি পাস ওয়ার্ড নেই । আইডি পাস ক্রিয়েট করার জন্য আপনাকে নিচের কমান্ড দিতে হবে 

```python
python manage.py createsuperuser
# if not works
winpty python manage.py createsuperuser
```

এরপর বাকি স্টেপ সম্পর্ন করলেই আপনি এডমিন প্যানেলে লগিন করতে পারবেন । কিন্তু সেখানে ইউজার আর গ্রুপ ছাড়া আমাদের তৈরী করা blog মডেলস দেখতে পারবেন না । এডমিন প্যানেলে সেই মডেল দেখার জন্য আপনাকে blog/admin.py ফাইলে মডেল রেজিস্টের করতে হবে । রেজিস্টার করার জন্য নিচের কোড লিখতে হবে । 

```python
# blog/admin.py 

from django.contrib import admin
from .models import Blog

# Register your models here.

admin.site.register(Blog)
```
এরপর আপনি ডাটাবেসে ইচ্ছামত ডাটা যুক্ত করতে পারবেন । ডাটা যুক্ত করার পর আরেকটি সমস্যা হচ্ছে টাইটেল গুলা না দেখিয়ে আমাদের দেখাচ্ছে Objects লিস্ট। টাইটেল দেখানোর জন্য আপনাকে নতুন করে যুক্ত করতে হবে 

```python
    def __str__(self):
        return self.title
```

এই লাইন যুক্ত করলেই আপনাকে টাইটেল দেখাবে । যুক্ত করতে না পারলে ভিডিও দেখুন । 



এর মাধ্যমেই আমাদের মডেলের কাজ শেষ হল । এরপর হচ্ছে ভিউ আর কাজ । 


8. Views ফাইলে কুয়েরিসেট 

MVT এর Models তৈরী করার কাজ আমাদের শেষ । এখন এরপরের ধাপ V মানে Views ফাইলে কাজ করতে হবে । Views ফাইলে আপনাকে models.py ফাইলকে ইম্পর্ট করতে হবে । ইম্পোর্ট করে আপনাকে সব অব্জেক্টকে কল করতে হবে । অব্জেক্ট গুলাকে কন্টেক্সটের মাধ্যমে পাস করতে হবে । নতুন ভিউ ফাইল হবে নিচের মত 

```python
from django.shortcuts import render
from .models import Blog

# Create your views here.
def home_view(request):
    blogpost = Blog.objects.all()
    context = {'blogpost':blogpost}
    return render(request, 'index.html', context)
```
এই টুকু হলেই আমাদের ভিউ ফাইলের কাজ শেষ । পরের ধাপ সেটা আমাদের টেমপ্লেট এ দেখানো । তাহলেই MVT পুর্ন হবে । 

9. Template এ ডাটা দেখানো 

context ফাইলে আমরা যা পেয়েছি সেটা হচ্ছে একটা লিস্ট। মানে এখানে অনেক অব্জেক্ট আছে । তাই প্রতিটা অব্জেক্টকে আলাদা আলাদা ভাবে দেখানোর জন্য আমাদের ফর লুপের হেল্প নিতে হবে । 

```python
{% for blog in blogpost %}
    <h2>{{ blog.title }}</h2>
    <p>{{ blog.description }}</p>
{% endfor %}
```

উপরের কোডটা লিখলেই আপনাকে ডাটা গুলা শো করবে । এবার সাজানোর পালা । টেমপ্লেট আপনি আপনার ইচ্ছামত সাজাতে পারেন । ভিডিওতে ব্যবহার করা কোড হচ্ছে 

```python 
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
          <a class="navbar-brand" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>

 
            </ul>
            <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
          </div>
        </div>
      </nav>

      <div class="container mt-5">
          <div class="row">
              <div class="col-md-8">
                  {% for blog in blogpost %}
                  <h2>{{ blog.title }}</h2>
                  <p>{{ blog.description }}</p>
                  {% endfor %}
              </div>
              <div class="col-md-4">
                  <h3>Sidebar</h3>
              </div>
          </div>
      </div>

    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  </body>
</html>
```

এবার সার্ভার রান করুন । localhost:8000 ভিজিট করলেই আপনার সাইট দেখতে পারবেন ।  জ্যাংগো এডমিন প্যানেলের এড্রেস হচ্ছে localhost:8000/admin 

ধন্যবাদ সবাইকে 








