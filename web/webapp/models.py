from django.db import models

# Create your models here.
class ultratech(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class astral(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class berger(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class steel(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class rmc(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class aggregates(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class BathroomFittings(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class tatawiron(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class waterTank(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class constructionSolution(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class waterproofing(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class tileadhesive(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class jointmortar(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class birlawhite(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1

class kdm(models.Model):
    image=models.ImageField(upload_to='images/')
    text1=models.CharField(max_length=100)
    text2=models.CharField(max_length=1000)

    def __str__(self):
        return self.text1


class offer(models.Model):
    image=models.ImageField(upload_to='images/')
    text=models.CharField(max_length=100)

    def __str__(self):
        return self.text

class form(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    PhoneNumber=models.CharField(max_length=50)
    Message=models.CharField(max_length=100)

    def __str__(self):
        return self.FirstName