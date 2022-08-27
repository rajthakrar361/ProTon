from django.urls import reverse
from django.urls.conf import path
from website import views
app_name='website'

urlpatterns=[
    path('',views.HomeView.as_view(),name='web_home'),
    path('test_cookie/', views.test_cookie, name='test_cookie'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('team/',views.TeamView.as_view(),name='team'),
]