from  django.urls import path
from .views import home, ad_detail, ad_by_category, add_ad, update_ad, delete_ad, save_comment, update_comment, delete_comment


urlpatterns=[
    path('', home, name='home'),
    path('ads/<int:ad_id>/', ad_detail, name='detail'),
    path('ads/update/<int:ad_id>/', update_ad, name='update'),
    path('ads/delete/<int:ad_id>/', delete_ad, name='delete'),
    path('ads/add/', add_ad, name='add_ad'),
    path('ads/<int:ad_id>/comment/add', save_comment, name='save_comment'),
    path('ads/<int:ad_id>/comment/<int:comment_id>/update', update_comment , name='update_comment'),
    path('ads//comment/<int:comment_id>/delete', delete_comment , name='delete_comment'),
    path('categories/<int:category_id>/', ad_by_category, name='about')
]