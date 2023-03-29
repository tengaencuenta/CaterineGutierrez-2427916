from django.urls import path

from.import views

urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('productos',views.productos,name='calculo'),
]


urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('categorias',views.categorias,name=''),
]
