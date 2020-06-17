from django.db import models

# Create your models here.
class Cow(models.Model):
    dob = models.DateTimeField()
    name = models.CharField(max_length=50)
    stage = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    production = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class Parturation(models.Model):
    cow = models.ForeignKey(Cow,on_delete=models.DO_NOTHING,related_name="parturation")
    date_served = models.DateTimeField()
    expected_date = models.DateTimeField()
    breed = models.CharField(max_length=200,null=True,blank=True)
    vet = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.cow.name

class Feed(models.Model):
    cow = models.ForeignKey(Cow,on_delete=models.DO_NOTHING,related_name="feed")
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField()
    rate = models.CharField(max_length=60)

    def __str__(self):
        return self.cow.name
class Treatment(models.Model):
    cow = models.ForeignKey(Cow,on_delete=models.DO_NOTHING,related_name="treatment")
    disease = models.CharField(max_length=100)
    prescription = models.TextField()
    vet = models.CharField(max_length=100)
    date_treated = models.DateTimeField(auto_now_add=True)
    date_observed = models.DateField()

    def __str__(self):
        return self.cow.name