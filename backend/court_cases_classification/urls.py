from django.urls import path
from court_cases_classification import views


app_name = 'court_cases_classification'

urlpatterns = [
    # path('list/', views.index, name='lecturer_list'),
    # path('data/', views.upload_data, name='court_case'),
    # path('data/download/page', views.download_page, name='download_page'),
    # path('data/download', views.downloads, name='download'),
    # path('data/about', views.about, name='about'),
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('logout', views.logoutUser, name='logout'),

    path('login/user', views.LoginView.as_view()),
    path('predictions', views.UploaDataView.as_view()),
    path('data/download', views.DownloadView.as_view()),
    
]