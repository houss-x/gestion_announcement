from django.shortcuts import render

from django.http import Http404

from django.shortcuts import get_object_or_404

from .models import Announcement

def announcement_list(request):
    if request.user.is_authenticated:
        user_announcement_list = Announcement.published.filter(user=request.user)
        count = user_announcement_list.count()
    else:
        user_announcement_list = None
        count = 0

    return render( request,"anouncement/list.html", {"announcementlist": user_announcement_list, "count": count}
    )

def get_announcement(request, slug, id):
      anouncement =get_object_or_404(Announcement,id,slug=slug,id=id)
      return render(request,"anouncement/list.html",{"item":anouncement})