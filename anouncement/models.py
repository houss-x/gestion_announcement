from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class AnnouncementStatus(models.IntegerChoices):
    PENDING = 0, 'Pending'
    APPROVED = 1, 'Approved'
    REJECTED = 2, 'Rejected'
    PUBLISHED = 3, 'Published'

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
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
            return super().get_queryset().filter(status=AnnouncementStatus.PUBLISHED)
        
    objects=models.Manager
    published=PublishedAnouncementManager()

    
    
    def get_absolute_url(self):
        return reverse(
            "anouncement:anouncement_detail",
            args=[self.slug],
        )
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
        indexes = [ models.Index(fields=['-created_at']),]
