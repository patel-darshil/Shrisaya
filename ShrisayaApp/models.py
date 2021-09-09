from django.db import models

# Create your models here.
class Form(models.Model):
    cotact_id = models.AutoField(db_column='id',primary_key=True,null=False, unique=True)
    fname =  models.CharField(db_column='fname',max_length=70,null=False)
    lname =  models.CharField(db_column='lname',max_length=70,null=False)
    email =  models.EmailField(db_column='email',max_length=70,null=False)
    phn   =  models.BigIntegerField(db_column='phn',null=False)
    message = models.CharField(db_column='message',max_length=1000)

    def __str__(self):
        return str(self.fname +" "+ self.lname +" "+ self.email)

    class Meta:
        db_table = "cotact_form"