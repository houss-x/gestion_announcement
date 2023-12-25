from django import forms 
from anouncement.models import Announcement ,Category,AnnouncementStatus

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