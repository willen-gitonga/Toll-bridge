from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    image = models.ImageField(upload_to = 'photos/', default='DEFAULT VALUE')
    heading = models.CharField(max_length=150)
    description = models.TextField(max_length=500,null=True)
    time = models.CharField(max_length=20)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

class Project(models.Model):
    image = models.ImageField(upload_to = 'photos/', default='DEFAULT VALUE')
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500,null=True)
    location = models.CharField(max_length=50)
    time_taken = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Future_plans(models.Model):
    image = models.ImageField(upload_to = 'photos/', default='DEFAULT VALUE')
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500,null=True)
    location = models.CharField(max_length=50)
    time_taken = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title


class Bursary(models.Model):
    PARTICIPATE_CHOICES = [
        ('Yes','Yes'),
        ('No','No'),
    ]
    INFLUENCE_CHOICES = [
        ('Books','Books'),
        ('Newspapers','Newspapers'),
        ('Magazines','Magazines'),
        ('E-Learning','E-Learning'),
        ('Online Articles','Online Articles'),
        ('Journals','Journals'),
        ('Teachers','Teachers'),
        ('Other','Other')
    ]
    EDUCATION_CHOICES = [
        ('Kindergarten','Kindergarten'),
        ('Primary School','Primary School'),
        ('High School','High School'),
        ('Diploma','Diploma'),
        ('Bachelor Degree','Bachelor Degree'),
        ('Masters Degree','Masters Degree'),
        ('Doctorate','Doctorate'),
        ('Other','Other')

    ]
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
        ('Prefer not to say','Prefer not to say')
    ]
    PAY_CHOICES = [
        ('Above 60,000 ksh','Above 60,000 ksh'),
        ('40,000 - 50,000 ksh','40,000 - 50,000 ksh'),
        ('20,000 - 40,000 ksh','20,000 - 40,000 ksh'),
        ('1,000 - 20,000 ksh','1,000 - 20,000 ksh'),
        ('Below 1,000 ksh','Below 1,000 ksh'),


    ]
    First_name = models.CharField(max_length =40)
    Last_name = models.CharField(max_length =40)
    Email = models.CharField(max_length =100)
    Gender = models.CharField(max_length =100,choices=GENDER_CHOICES, null=True)
    Have_you_participated_in_any_aid_providing_programme_before = models.CharField(max_length =100,choices=PARTICIPATE_CHOICES, null=True)
    Which_avenue_was_most_influential_in_your_learning =models.CharField(max_length =100,choices=INFLUENCE_CHOICES, null=True)
    What_is_your_average_family_monthly_income = models.CharField(max_length =100,choices=PAY_CHOICES, null=True)
    What_is_your_highest_level_of_education_completed =models.CharField(max_length =100,choices=EDUCATION_CHOICES, null=True)
    Please_outline_any_community_work_you_have_undertaken=models.TextField(max_length=2000)

    def __str__(self):
        name = self.first_name     
        return name

class News(models.Model):
    headline = models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'photos/', default='DEFAULT VALUE')
    def __str__(self):
        return self.headline


