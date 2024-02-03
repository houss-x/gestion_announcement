from django import forms 
from anouncement.models import Announcement ,User,AnnouncementStatus

class UpdateAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'image', 'content', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].choices = AnnouncementStatus.choices

class AddAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'image', 'content', 'category']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)
    password_verif = forms.CharField(label='Current Password', widget=forms.PasswordInput)