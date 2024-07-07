from django.db import models

#Install this library and import it to improve the password security | Parol xavfsizligini yaxshilash uchun ushbu kutubxonani o'rnating va import qiling
from django_cryptography.fields import encrypt
#Run this on terminal to install it | Bu kutubhonani o'rnatish uchun kerak bo'lgan terminal komandasi
#pip install django-cryptography





#If you're facing this error: | Agar siz bu error bilan yuzmayuz kelayotgan bolsangiz:
#ImportError: cannot import name 'baseconv' from 'django.utils'


#Install this: | Buni o'raning:
#pip install "git+https://github.com/saurav-codes/django-cryptography"

# Create your models here.

        
class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    
    user_name = models.CharField(max_length=255, unique=True)
    _password = encrypt(models.CharField(max_length=20))
    
    bio = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to = 'profile_pictures')
    
    facebook_l = models.URLField(max_length=255)
    twitter_l = models.URLField(max_length=255)
    linked_in_l = models.URLField(max_length=255)
    skype_l = models.URLField(max_length=255)
    
class Post(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to ='uploads/') 
    created_at = models.DateTimeField(auto_now_add=True)
    
class Category(models.Model):
    title = models.TextField(max_length=255)
    img = models.ImageField(upload_to ='category/')
    
    class Meta:
        verbose_name_plural = "Categories"
        
        
class Liked(models.Model):
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    @property
    def liked_by_count(self):
        return self.liked_by.count()

        
class Comment(models.Model):
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    @property
    def commented_by_count(self):
        return self.commented_by.count()


class Shared(models.Model):
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    @property
    def shared_by_count(self):
        return self.shared_by.count()
        
User.add_to_class('liked_count', property(lambda x: Liked.objects.filter(liked_by=x).count()))
User.add_to_class('commented_count', property(lambda x: Comment.objects.filter(commented_by=x).count()))
User.add_to_class('shared_count', property(lambda x: Shared.objects.filter(shared_by=x).count()))
    
    
class Blog_area_single_post(models.Model):
    img = models.ImageField(upload_to ='blog_area_sp/') #blog area single post
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    likes,coments,shares = Liked.liked_by_count, Comment.commented_by_count, Shared.shared_by_count
    
class Blog_area_list_post(models.Model):
    img = models.ImageField(upload_to ='blog_area_lp/') #blog area list post
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    likes,coments,shares = Liked.liked_by_count, Comment.commented_by_count, Shared.shared_by_count
