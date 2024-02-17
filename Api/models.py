from django.db import models

class Specialist(models.Model):
    image = models.ImageField(null=True)
    lastname = models.CharField(max_length=20,null=True)
    firstname = models.CharField(max_length=25,null=True)
    middlename = models.CharField(max_length=25,null=True)
    specialty = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=25,null=True)
    experience = models.IntegerField(null=True)
    consultation_price = models.IntegerField(null=True)
    office = models.CharField(max_length=100,null=True)
    working_days = models.CharField(max_length=25,null=True)
    time = models.IntegerField(null=True)
    phone = models.IntegerField(max_length=25,null=True)
    bio = models.TextField()
    level = models.FloatField(max_length=15,null=True)
    view = models.IntegerField(max_length=15,null=True)
    hard = models.IntegerField(max_length=15, null=True)

    
    def __str__(self):
        return self.specialty



class Hospitals(models.Model):
    type = models.CharField(max_length=25,null=True)
    image = models.ImageField(null=True)
    name = models.CharField(max_length=100,null=True)
    region = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=50,null=True)
    adress = models.CharField(max_length=100,null=True)
    level = models.FloatField(max_length=15,null=True)
    view = models.IntegerField(max_length=15,null=True)
    hard = models.IntegerField(max_length=15, null=True)
    web_site = models.CharField(max_length=50,null=True)

    
    def __str__(self):
        return self.name



class Pharmacys(models.Model):
    type = models.CharField(max_length=25,null=True)
    image = models.ImageField(null=True)
    name = models.CharField(max_length=100,null=True)
    region = models.CharField(max_length= 100,null=True)
    city = models.CharField(max_length=100,null=True)
    adress = models.CharField(max_length=100,null=True)
    level = models.FloatField(max_length=15,null=True)
    view = models.IntegerField(max_length=15,null=True)
    hard = models.IntegerField(max_length=15, null=True)
    web_site = models.CharField(max_length=50,null=True)
    
    
    def __str__(self):
        return self.name
    

class Section(models.Model):
    name = models.CharField(max_length=100,null=True)
    icon = models.FileField(null=True)

    def __str__(self):
        return self.name