from django.db import models

from datetime import date

class FamilyRole(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return u"%s" %(self.name)
    
class Family(models.Model):
    def members(self):
        return self.person_set.all()
    
    def __unicode__(self):
        if len(self.members()):
            return u"Familia %s" %(self.members()[0].last_name)
        else:
            return u"El nombre de la familia sera asignado luego"

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dni = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    description = models.TextField()
    role = models.ForeignKey(FamilyRole)
    family = models.ForeignKey(Family)
    age =models.IntegerField(null=True)
    
    def get_age(self):
        if not self.birth_date== None:
            today = date.today()
            age_aux = today.year - self.birth_date.year
            if not today >= self.birth_date.replace(year = today.year):
                age_aux = age_aux - 1
                return age_aux
            else:
                return self.age
    
    def __unicode__(self):
        return u"%s %s" %(self.first_name,self.last_name)
    
class ContactType(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return u"%s" %(self.name)
    
class Contact(models.Model):
    contact_type = models.ForeignKey(ContactType)
    value = models.CharField(max_length=400)
    owner = models.ForeignKey(Person)

    