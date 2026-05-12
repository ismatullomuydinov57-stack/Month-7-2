from  django.urls import path
from .views import home, ad_detail, ad_by_category, add_ad, update_ad, delete_ad


urlpatterns=[
    path('', home, name='home'),
    path('ads/<int:ad_id>/', ad_detail, name='detail'),
    path('ads/update/<int:ad_id>/', update_ad, name='update'),
    path('ads/delete/<int:ad_id>/', delete_ad, name='delete'),
    path('ads/add/', add_ad, name='add_ad'),
    path('categories/<int:category_id>/', ad_by_category, name='about')
]