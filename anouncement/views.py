from django.shortcuts import redirect, render

from django.http import Http404

from django.shortcuts import get_object_or_404

from anouncement.forms import UpdateAnnouncementForm,AddAnnouncementForm

from .models import Announcement

def announcement_list(request):
    if request.user.is_authenticated:
        user_announcement_list = Announcement.published.all()
        count = user_announcement_list.count()
        connected_username = request.user.username
    else:
        user_announcement_list = None
        count = 0

    return render( request,"anouncement/list.html", {"announcementlist": user_announcement_list,"userName":connected_username, "count": count}
    )
def my_announcement(request):
    print(request.user)
    if request.user.is_authenticated:
        print(request.user)
        my_announcement_list = Announcement.objects.filter(user=request.user)
        print(my_announcement_list)
    else:
        my_announcement_list = None

    return render(request, "anouncement/userList.html", {"myanouncement": my_announcement_list})

def delete_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    announcement.delete()
    return render(request, 'anouncement/userList.html', {'myanouncement': Announcement.objects.filter(user=request.user)})
def edit_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)

    if request.method == 'POST':
        form = UpdateAnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('anouncement:my_anouncement') 
    else:
        form = UpdateAnnouncementForm(instance=announcement)

    return render(request, 'anouncement/edit_anouncement.html', {'form': form, 'announcement': announcement})
def add_announcement(request):
    if request.method == 'POST':
        form = AddAnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.user = request.user  
            announcement.save()
            return redirect('anouncement:my_anouncement')
    else:
        form = AddAnnouncementForm()

    return render(request, 'anouncement/add.html', {'form': form})
def get_announcement(request, slug, id):
      anouncement =get_object_or_404(Announcement,id,slug=slug,id=id)
      return render(request,"anouncement/list.html",{"item":anouncement})