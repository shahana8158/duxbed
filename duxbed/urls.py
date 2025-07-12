"""
URL configuration for duxbed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from duxbed_innovation_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', views.homefn),

    path('stores/', views.stores_view, name='stores'),
    path('languages/', views.languagesfn),
    
    path('why-dux/', views.whyduxfn),
    path('more/', views.morefn),
    path('cart/', views.cartfn),
    
    path('search/', views.searchfn, name='search'),
    
    path('career/', views.careerfn, name='career'),
    
    path('interior/', views.interiorfn),
    path('solidfurniture/', views.solidfurniturefn),


    path('bedcot/', views.bedcotfn),
    path('sofacomebed/', views.sofacomebedfn),   
    path('storagebed/', views.storagebedfn),
    path('bridalset/', views.bridalsetfn),
    path('ironboard/', views.ironboardfn),
    path('shoerack/', views.shoerackfn),      
    path('diningtable/', views.diningtablefn),
    path('coffeecounter/', views.coffeecounterfn),
    path('studyunit/', views.studyunitfn),
    path('mirrorunit/', views.mirrorunitfn),

    path('islandkitchen/', views.islandkitchenfn),
    path('lshapekitchen/', views.lshapekitchenfn),
    path('ushapekitchen/', views.ushapekitchenfn),
    path('parallelkitchen/', views.parallelkitchenfn),
    path('straightkitchen/', views.straightkitchenfn),

    path('register/', views.registerfn, name='register'),
    path('login/', views.loginfn, name='login'),
    path('logout/', views.logoutfn, name='logout'),
    
    path('products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),

     path('products/', views.product_list, name='product_list'),
    
    path('add-product/', views.add_product, name='add_product'),
    path('add-review/', views.add_review, name='add_review'),

    path('submit-booking/', views.submit_booking, name='submit_booking'),
            

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
