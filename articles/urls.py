from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
)

app_name='articles'
urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='edit'),
    path('<int:pk>/detail/', ArticleDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),
    path('new/', ArticleCreateView.as_view(), name='new'),
    path('', ArticleListView.as_view(), name='article_list'),
]
