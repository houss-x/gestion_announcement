from django.shortcuts import render

from django.http import Http404

from django.shortcuts import get_object_or_404

from .models import Announcement

def announcement_list(request):
    announcement_list = Announcement.published.all()
    return render(request, "anouncement/list.html", {"announcementlist": announcement_list,"count":announcement_list.count()})

def get_announcement(request, slug, id):
      anouncement =get_object_or_404(Announcement,id,slug=slug,id=id)
      return render(request,"anouncement/detail.html",{"item":anouncement})