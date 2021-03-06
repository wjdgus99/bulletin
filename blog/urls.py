from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostLV.as_view(), name = 'index'),
    path('post/', views.PostLV.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDV.as_view(), name = 'post_detail'),
    path('archive/', views.PostAV.as_view(), name = 'post_archive'),
    path('archive/<int:year>/', views.PostYAV.as_view(), name = 'post_year_archive'),
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name = 'post_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name = 'post_day_archive'),
    path('archive/today/', views.PostTAV.as_view(), name = 'post_today'),

    path('create/', views.CreatePost.as_view(), name='create_post'),
    path('update/<int:pk>', views.UpdatePost.as_view(), name='update_post'),
    # path('delete/<int:pk>', views.DeletePost.as_view(), name='delete_post'),
    path('delete/<int:pk>/', views.delete,name='delete')

]
