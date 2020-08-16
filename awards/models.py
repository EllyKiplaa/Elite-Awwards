from django.db import models

# Models
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    avi=ImageField(manual_crop='')
    bio=models.CharField(max_length=240)
    phone=models.IntegerField(blank=True)
    email=models.EmailField()


