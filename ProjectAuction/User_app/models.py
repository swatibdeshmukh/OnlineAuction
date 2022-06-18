from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=50)
    country_code = models.IntegerField()

    def __str__(self):
        return str(self.country_name)

class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.state_name)

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.city_name)

class Address(models.Model):
    area_id = models.IntegerField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=200)
    street_name = models.CharField(max_length=150)
    house_no = models.CharField(max_length=50)
    area_pincode = models.CharField(max_length=50)

    def __str__(self):
        return str(self.area_name)

class MyUser(User):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField()
    gender = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)

class IdProof(models.Model):
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    idproof_id = models.IntegerField(primary_key=True)
    idproof_type = models.CharField(max_length=50)
    idproof_image = models.ImageField(upload_to = 'idphoto/')

    def __str__(self):
        return str(self.idproof_type)



    

