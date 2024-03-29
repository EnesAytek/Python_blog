from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from page.models import Page


 

FAKE_DB_CAROUSEL = [
        f"https://picsum.photos/id/{id}/1200/400" for id in range (24, 28)
    ]



def home_view(request):
    context = dict(
        # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
        FAKE_DB_CAROUSEL = FAKE_DB_CAROUSEL,
    )
    return render(request, "page/home_page.html", context)




def page_view(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    context = dict(
        page=page,
    )
    return render(request, "page/page_detail.html", context)
    
    
    