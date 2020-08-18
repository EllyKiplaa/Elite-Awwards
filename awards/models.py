from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.core.validators import MaxValueValidator,MinValueValidator

# Models
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images')
    bio = models.TextField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    
    def __str__(self):
        
        return self.profile_photo.url
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    @classmethod   
    def update_bio(cls,id,new_bio):
        cls.objects.filter(pk = id).update(bio=new_bio)
        new_bio_object = cls.objects.get(bio = new_bio)
        new_bio = new_bio_object.bio
        return new_bio
        
    def __str__(self):
        
        return self.profile_photo.url
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()

class Project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='project')
    title=models.CharField(max_length=150)
    landing=ImageField(manual_crop='')
    description=models.TextField()
    live_site=models.URLField(max_length=299)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    @classmethod
    def get_all_projects(cls):
        return cls.objects.all()

    @classmethod
    def single_project(cls,id):
        return cls.objects.get(id=id)


class Review(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='review')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='review')
    comment=models.TextField()
    design=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    useability=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.user.username

    @classmethod
    def project_reviews(cls, id):
        return cls.objects.filter(id)   
