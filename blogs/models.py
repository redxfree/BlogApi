from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


#category of Blogs

class category(models.Model):
	categorie = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
    
	def __str__(self):
		return self.slug

	def save(self,*args,**kwargs):
		self.slug =self.slug or slugify(self.categorie)	
		super().save(*args,**kwargs)

# Blog model

class Blog(models.Model):
	title = models.CharField(max_length=270)
	content = models.CharField(max_length=270)
	image_blog = models.ImageField(upload_to = "iamges/blogs",blank = False)
	slug = models.CharField(max_length=270)
	category = models.ForeignKey(category,on_delete=models.CASCADE)
	post_date = models.DateTimeField(auto_now_add=True)
    
	def __str__(self):
		return self.title
    
	def save(self,*args,**kwargs):
		self.slug =self.slug or slugify(self.title)
		super().save(*args,**kwargs)
        
#commenting for a blogs if user is logged in with time of comment
        
class comment(models.Model):
	comment = models.CharField(max_length=200)
	blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
	user  = models.OneToOneField(User,on_delete=models.CASCADE)
	comment_time = models.DateTimeField(auto_now_add=True)
    
	def __str__(self):
		return self.comment
    