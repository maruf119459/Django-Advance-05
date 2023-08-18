from django.urls import path
from . import views
urlpatterns = [
    # path('',views.home ), #cookies er jonno
    path('',views.set_session ), #session er jonno
    #path('get/',views.get_cookie ),  #cookies er jonno
    path('get/',views.get_session ),  #session er jonno
    path('del/',views.delete_cookie ),
    path('del/',views.delete_session ),  #session er jonno
]