from django.urls import path
from . import views
from django.urls import path
from . import views
from . import restapi as restapis_views



app_name = 'order'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path(r'getpost', restapis_views.RestApiViewSet.as_view({'get': 'display_post'}), name='getpost')
]
