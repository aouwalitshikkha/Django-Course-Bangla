# জ্যাংগো প্রথম প্রজেক্ট ( Views ও URLs ফাইল নিয়ে আলোচনা )


এখানে আমরা একটি স্টাটিক হোম পেজ তৈরী করব । সম্পুর্ন স্টেপ গুলা নিচে দেওয়া হল 


# ভিডিও ১১ঃ ইউ আর এল ফাইল কনফিগ 

## সংক্ষিপ্ত ধাপ 
-   প্রথমে ভার্চুয়াল এনভায়রনমেন্ট ক্রিয়েট করা 
-   ভার্চুয়াল এনভায়রনমেন্ট এক্টিভ করা 
-   জ্যাংগো ভার্চুয়াল এনভায়রনমেন্টে ইন্সটল করা 
-   জ্যাংগোতে প্রজেক্ট ক্রিয়েট করা 
-   জ্যাংগোতে এপস ক্রিয়েট করা 
-   জ্যাংগোর প্রজেক্টের সাথে এপসকে যুক্ত করা 
-   এপস এ ইউ আর এল (urls.py) ফাইল তৈরী ও প্রজেক্ট ফাইলের সাথে যুক্ত করা 
-   ভিউস ফাইল নিয়ে কাজ করা 


### ভার্চুয়াল এনভায়রনমেন্ট ক্রিয়েট করা

যেই ফোল্ডারে ভার্চুয়াল এনভায়রনমেন্ট ক্রিয়েট করতে চান সেখানে কমান্ড রান করুন । 

```python
python -m venv env
```

###  ভার্চুয়াল এনভায়রনমেন্ট এক্টিভ করা 
```python 
source env/Scripts/activate
```

### Django Install 
```python
pip install django 
```

### জ্যাংগোতে প্রজেক্ট ক্রিয়েট করুন 
```python
django-admin startproject core 
```

ভিডিওতে প্রথম Core ফোল্ডারের নাম চেঞ্জ করে src করা হয়েছে । 

###  এপস ক্রিয়েট করুন 

এপস ক্রিয়েট করার জন্য প্রথমে প্রজেক্ট ফোল্ডারে প্রবেশ করুন । এখানে SRC ফোল্ডার। সেই ফোল্ডারে প্রবেশ করা ও এপস ক্রিয়েটের কোড 
```python
cd src
python manage.py startapp weather
```

### প্রজেক্ট ও এপস এর সাথে যুক্ত করুন

প্রজেক্ট ফোল্ডার *core* এর settings.py ফাইল এডিটরে খুলুন । ৩৩ নং লাইন থেকে শুরু হওয়া Installed Apps লিস্টের শেষে আপনার এপস এর নাম যুক্ত করুন 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weather', # এই লাইন নতুন ভাবে যুক্ত করা হয়েছে 
]
```

- #### Weather ফোল্ডারে urls.py ফাইল যুক্ত করুন । 
- #### core এর urls.py ফাইলের ২ নং লাইনে path এর পর কমা দিয়ে include ফাংশনকে ইম্পোর্ট করুন । আর urlpattern লিস্টে নতুন করে *path('', include('weather.urls'))* যুক্ত করুন । এখানে weather হচ্ছে এপস এর নাম আর urls হচ্ছে সেখানকার ফাংশনের নাম। 

```python 
# core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls'))
]
```
- Weatther ফোল্ডারে আগের core ফোল্ডারের কোড কপি করে নিন। সেখানে প্রথম লাইন *from django.contrib import admin* বাদ দিন । আর path পরে include বাদঃ দিয়ে দিন । একই ফোল্ডার থেকে views ফাইল ইম্পোর্ট করুন । 

- urlpatterns লিস্টের প্রথম লাইন বাদ দিন *path('admin/', admin.site.urls),* । আর এরপরের লাইনে যুক্ত করুন path('', views.home_view , name ="home" ) । তাহলে মুল ফাইল হবে নিচের মত 

```python
# weather/urls.py


from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view , name ="home" )
]
```

- এখানে urls প্যাটার্ন লিস্টে views.home_view নির্দেশ করে views.py ফাইলে তৈরী করা home_view ফাংশনকে  । আর এরপর নাম হচ্ছে home. যা আমরা পরবর্তীতে ব্যবহার করব বিভিন্ন সময় নির্দিষ্ট ইউ আর এলকে কল করার জন্য । 

## ভিডিও -১২ঃ  Views তৈরী 

weather ফোল্ডারের views.py ফাইল যে কোন আইডিএলই তে খুলুন । এরপর সেখানে weather/urls.py ফাইলে দেওয়া নাম অনুসারে একটি ফাংশন ডেভেলপ করুন। আমরা এর আগে নাম দিয়েছিলাম home_view তাই হোম ভিউ নামে একটা ফাংশন তৈরী করা হয়েছে প্রথমে । 

ফাংশনটি 

```python
# weather/views.py 

from django.shortcuts import render, HttpResponse

def home_view(request):
    return HttpResponse('<h1>First Django Project</h1>') 
```

এবার সার্ভার রান করুন । 
```python
python manage.py runserver
```

আপনি হোম পেজে ( http://127.0.0.1:8000/ ) দেখতে পারবেন First Django Project লিখাটি h1 হিসাবে । 

কিন্তু এতে বড় কোন ফাইল লিখা অনেক ঝামেলা । এইজন্য আমরা টেমপ্লেট ইউজ করুব । টেমপ্লেট নামে একটি ফোল্ডার যুক্ত করুন আপনার src ডিরেক্টরিতে । 

তাহলে আপনার ফোল্ডার স্ট্রাকচার হবে 
```code
.
├── src                     # মুল ফোল্ডার 
├── core                    # প্রজেক্ট ফোল্ডার
├── weather                 # এপ্লিকেশন ফোল্ডার
├── templates               # টেমপ্লেট ফোল্ডার 
```
সেই টেমপ্লেট ফোল্ডারের মধ্যে যে কোন টেমপ্লেট রাখুন ।  এরপর views.py ফাইলে নিচের কোড লিখুন । 

```python
# weather/views.py 

from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'home.html')
```


 ব্রাউজারে http://127.0.0.1:8000/ ইউ আর এল প্রবেশ করলে দেখতে পারবেন Template Doesn't Exists দেখাচ্ছে । এই সমস্যা সল্ভ করার জন্য core/settings.py ফাইলে প্রবেশ করুন । এরপর templates লিস্ট ( ৫৮ নং লাইনে ) Dir এর ভিতরে লিখুন BASE_DIR / 'templates' । তাহলে কোড নিচের মত দেখাবে 
```python 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

আবার  সার্ভার রান করুন । 

```python
python manage.py runserver
```

তাহলে আপনার দেখানো টেমপ্লেট দেখতে পারবেন ব্রাউজারে (http://127.0.0.1:8000/)। 


রিসোর্স লিংকঃ 
