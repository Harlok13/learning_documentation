#  URLconf для вызова представления
from . import views
from django.urls import path

app_name = 'polls'  # добавляет пространство имен, чтобы тег шаблона {% url %} мог определить представление этого приложения
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
