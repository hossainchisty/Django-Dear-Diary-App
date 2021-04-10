from django.urls import path
from . import views
from . views import DiaryUpdateView,DiaryDeleteView
urlpatterns = [
    path('', views.home,name="home"),
    path('<pk>/update_diary', DiaryUpdateView.as_view(), name="update_diary"),
    path('<pk>/delete_diary', DiaryDeleteView.as_view(), name="delete_diary"),
]