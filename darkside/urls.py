from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('sith', views.Sithview, name = 'sith'),
    path('test', views.viewtest, name = 'test'),
    path('recruit', views.RecruitCreateView.as_view(), name = 'recruit'),
    path('viewrecruits',views.viewrecruits, name = 'viewrecruits'),
    path('detailrecruit/<int:idrecruit>/', views.detailrecruit, name = 'detailrecruit'),
]