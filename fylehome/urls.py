from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'bank/(?P<ifsc>\w+)/$', views.BankIFSCDetailsView, name="bank-ifsc-details")
]