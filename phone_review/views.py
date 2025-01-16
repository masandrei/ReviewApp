from django.shortcuts import render
from .models import Phone

def main_page_view(request):
    phones = Phone.objects.order_by("-year_of_presentation", "-manufacturer", "-phone_model")
    context = {"phones" : phones}
    return render(request, "main/index.html", context = context)

