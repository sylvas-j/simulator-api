from django.urls import path
from smart_home_monitoring import views


app_name = 'smart_home_monitoring'

urlpatterns = [
    path('list/', views.index, name='lecturer_list'),
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('logout', views.logoutUser, name='logout'),

    path('predictions', views.UploaDataView.as_view()),
    path('download/', views.DownloadView.as_view()),
    
    
]