from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact


# Create your views here.
def index(request):

    context = {
        
    }

    return render(
        request,
        'contact/index.html',
        context
    )