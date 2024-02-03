from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
class AnnouncementStatus(models.IntegerChoices):
    PENDING = 1, 'Pending'
    REJECTED = 2, 'Rejected'
    PUBLISHED = 3, 'Published',
    FINISHED=4,'Finished'

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image=models.ImageField(default="https://media.istockphoto.com/id/1344512181/vector/icon-red-loudspeaker.jpg?s=612x612&w=0&k=20&c=MSi3Z2La8OYjSY-pr0bB6f33NOuUKAQ_LBUooLhLQsk=")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='announcements')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='announcements')
    status = models.IntegerField(
        choices=AnnouncementStatus.choices,
        default=AnnouncementStatus.PUBLISHED,
    )
    slug = models.SlugField(max_length=250, unique_for_date="created_at",default="houssam")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class PublishedAnouncementManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=AnnouncementStatus.PUBLISHED, user__is_active=1)
        
    objects=models.Manager()
    published=PublishedAnouncementManager()
    
    def get_absolute_url(self):
        return reverse(
            "anouncement:anouncement_detail",
            args=[str(self.slug)],
        )
    
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
        indexes = [ models.Index(fields=['-created_at']),]
