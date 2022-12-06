from ast import Store
from app import views
from django.contrib import admin
from django.urls import path
from app.views import  index, cad, store, telaLogin, dologin,logouts, changePassword, fuvest, cebraspe, ciee, fgv, contato, sobre


# Define as rotas e funções que serão chamadas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cad/', cad),
    path('store/', store ),
    path('telaLogin/', telaLogin),
    path('dologin/', dologin),
    path('logouts/', logouts),
    path('resetPassword/', changePassword),
    path('fgv/', fgv),
    path('ciee/', ciee),
    path('cebraspe/', cebraspe),
    path('fuvest/', fuvest),
    path('contato/', contato),
    path('sobre/', sobre)
]