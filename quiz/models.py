from django.db import models
from category.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Duration of the quiz in seconds", default="1")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    has_time_limit = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class QuesModel(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,null=True)
    question=models.CharField(max_length=600,null=True)
    option1=models.CharField(max_length=200,null=True)
    option2=models.CharField(max_length=200,null=True)
    option3=models.CharField(max_length=200,null=True)
    option4=models.CharField(max_length=200,null=True)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat,null=True)
    
    def __str__(self):
        return self.question

class user_history(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    total = models.IntegerField(null=True)
    correct = models.IntegerField(null=True)
    wrong = models.IntegerField(null=True)
    parcentage = models.IntegerField(null=True)
    date_taken = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username



class UserReviewModel(models.Model):
    RATING =(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    rating = models.CharField(max_length=100,choices=RATING)
    details = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
