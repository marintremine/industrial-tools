from django.shortcuts import render
from apps.table import models


# Create your views here.
def home(request):
    context = {
        "tables": models.DYT_DynamicTable.objects.all()
    }
    print(context)
    return render(request, "table/home.html", context=context)

