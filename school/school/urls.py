from django.contrib import admin
from django.urls import path
from admission.views import *
from profiles.views import *
from transport.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('products/',products,name='products'),
    path('services/',services,name='services'),
    path('login/',login,name='login'),
    path('profiles/',profiles	,name='profiles'),
    path('transport/',transport,name='transport')  
]
