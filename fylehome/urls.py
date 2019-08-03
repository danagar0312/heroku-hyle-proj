from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'bank/(?P<ifsc>\w+)/$', views.BankIFSCDetailsView, name="bank-ifsc-details"),
    url(r'branch/(?P<branch>\w+ ?\w+?)/city/(?P<city>\w+ ?\w+?)/$', views.BranchDetailView, name="bank-ifsc-details"),
]