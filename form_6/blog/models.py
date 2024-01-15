from django.db import models

class Friends(models.Model):

    name=models.CharField(max_length=255)





    mail=models.EmailField()
    
    
    
    
    gender=models.BooleanField()
    
    
    
    age=models.IntegerField(defalt=0)
    
    
    
    birthday=models.DateField()
    


    def __str__(self):
        return '<Friend:id='  +  str(self.id)  +  ','  + \
            self.name  +  '('  +  str(self.age)  +  ')>'



