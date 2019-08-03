from rest_framework.decorators import api_view
from rest_framework.response import Response
from fylehome.models import Bank
from .serializer import BankSerializer
from django.http import HttpResponse
from django.core.paginator import Paginator
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend



@api_view(["GET"])
def BankIFSCDetailsView(request,ifsc):
    print(ifsc)
    bank = Bank.objects.get(ifsc=ifsc)
    print(bank)
    serializer = BankSerializer(bank)
    print(serializer)
    return Response(serializer.data)

@api_view(["GET"])
def BranchDetailView(request,branch,city):
    print(branch)
    print(city)
    branchlist = Bank.objects.filter(branch__icontains=branch, city__icontains=city)
    for branchd in branchlist:
        serializerd = BankSerializer(branchd)
        print(serializerd)
        return Response(serializerd.data)

# class SetLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 2
#     limit_query_param = 1
#     offset_query_param = 2

# class ClassBranchDetailView(generics.ListAPIView):
#     queryset = Bank.objects.all()
#     serializer_class = BankSerializer
#     pagination_class = LimitOffsetPagination
#     filter_backends = (DjangoFilterBackend,)
#     filterset_fields = ('branch', 'city')