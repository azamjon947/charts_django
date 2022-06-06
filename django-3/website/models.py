from django.db import models

class Chart(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=100)
    link = models.CharField(max_length=230)
    car = models.CharField(max_length=102)
    title = models.CharField(max_length=129)
    brend = models.CharField(max_length=123)
    
    
def __str__(self):
    return self.name    
    return self.text
    return self.link
    return self.car
    return self.title
    return self.brend
    
class Chart2(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=100)
    link = models.CharField(max_length=234)
    list1 = models.CharField(max_length=124)
    
def __str__(self):
    return self.name
    return self.text
    return self.link
    return self.list1
# class Image(models.Model):

#      text = models.CharField(max_length=60)   
#      image = models.ImageField()     
        
     
#      def __str__(self):
#         return self.text
