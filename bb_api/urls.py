from django.urls import path
from .views import bbs, BbDetailView, comments, BbListView, BbCreateView, BbUpdateView, BbDeleteView
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('bbs/<int:pk>/comments/', comments),
    path('bbs/<int:pk>/update/', BbUpdateView.as_view()),
    path('bbs/<int:pk>/delete/', BbDeleteView.as_view()),
    path('bbs/<int:pk>/', BbDetailView.as_view()),
    path('bbs/add/', BbCreateView.as_view()),
    path('bbs/', BbListView.as_view()),
    path('', bbs),
]

urlpatterns += doc_urls
