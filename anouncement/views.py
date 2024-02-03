from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from anouncement.forms import UpdateAnnouncementForm,AddAnnouncementForm
from .models import Announcement, AnnouncementStatus, Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from anouncement.forms import UserProfileForm, ChangePasswordForm


def announcement_list(request):
    categories=Category.objects.all()

    if request.user.is_authenticated:
        user_announcement_list = Announcement.published.all()
        connected_username = request.user.username
    else:
        user_announcement_list = None

    return render( request,"anouncement/list.html", {"announcementlist": user_announcement_list,"categories":categories,"userName":connected_username}
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
@login_required
def edit_profile(request):
    user_form = UserProfileForm(instance=request.user)
    password_form = ChangePasswordForm()

    if request.method == 'POST':
        if 'update_user_info' in request.POST:
            user_form = UserProfileForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('anouncement:edit_profil')

        elif 'change_password' in request.POST:
            password_form = ChangePasswordForm(request.POST)
            if password_form.is_valid():
                password1 = password_form.cleaned_data.get('password1')
                password2 = password_form.cleaned_data.get('password2')
                password_verif = password_form.cleaned_data.get('password_verif')

                if password1 == password2 and request.user.check_password(password_verif):
                    request.user.set_password(password1)
                    request.user.save()
                    update_session_auth_hash(request, request.user)  # Keep the user logged in
                    messages.success(request, 'Password changed successfully.')
                    return redirect('anouncement:edit_profil')
                else:
                    messages.error(request, 'Passwords do not match or current password is incorrect.')

    return render(request, 'anouncement/profil.html', {'user_form': user_form, 'password_form': password_form})