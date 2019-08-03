from rest_framework.decorators import api_view
from rest_framework.response import Response
from fylehome.models import Bank
from .serializer import BankSerializer
from django.http import HttpResponse

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
    print(branchlist)

    for branchd in branchlist:
        serializerd = BankSerializer(branchd)
        print(serializerd)
        return Response(serializerd.data)