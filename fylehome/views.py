from rest_framework.decorators import api_view
from rest_framework.response import Response
from fylehome.models import Bank
from .serializer import BankSerializer
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Q
import operator

@api_view(["GET"])
def BankIFSCDetailsView(request,ifsc):
    print(ifsc)
    bank = Bank.objects.get(ifsc=ifsc)
    print(bank)
    serializer = BankSerializer(bank)
    print(serializer)
    return Response(serializer.data)

@api_view(["GET"])
def BranchDetailView(request,branch,city,offset,limit):
    branlst = Bank.objects.filter(branch__icontains=branch, city__icontains=city)
    print(branlst)
    branchlist = Bank.objects.filter(branch__icontains=branch, city__icontains=city)[2:3]
    print(branchlist)
    serializerd = BankSerializer(branchlist, many=True)
    return Response(serializerd.data)

class SetLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 1
    offset_query_param = 2

class MultipleFieldLookupMixin(object):
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            filter[field] = self.kwargs[field]
        q = reduce(operator.or_, (Q(x) for x in filter.items()))
        return get_object_or_404(queryset, q)

class ClassBranchDetailView(MultipleFieldLookupMixin,generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    pagination_class = LimitOffsetPagination
    lookup_fields = ('branch', 'city')