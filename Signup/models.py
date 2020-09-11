from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User=get_user_model()

class ProfileManager(models.Manager):
    def create_profile(self,user):
        profile=self.create(user=user)
        profile.save()


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number=models.IntegerField(blank=True,null=True)
    profile_picture=models.ImageField(upload_to='Profile/',default='Profile/dummypic.jpeg')
    
    objects=ProfileManager()
     
    def __str__(self):
        return self.user.username



@receiver(post_save,sender=User)
def createit(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create_profile(user=instance)