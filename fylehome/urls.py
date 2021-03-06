from django.conf.urls import url
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    url(r'bank/(?P<ifsc>\w+)/$', views.BankIFSCDetailsView, name="bank-ifsc-details"),
    url(r'branch/(?P<branch>\w+ ?\w+?)/city/(?P<city>\w+ ?\w+?)/$', views.ClassBranchDetailView.as_view(), name="bank-ifsc-details"),
    
]