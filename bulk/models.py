from django.db import models
from django.contrib import admin


from django.utils.timezone import now

# Create your models here.
'''
Person class
Customer class
Contact class
Message class
Service_log class

/NANA B./
destroy person class.
include all its attributes to Customer.
create class Group with attributes
groupname, date_created, date_updated. They should be like the blog project dates.
it should have a FK field that links to Customer
and in the Contact class it should have
a FK field to Group class and Customer
so the contact class has two FK fields  
'''

class Customer(models.Model):
      name = models.CharField(max_length=30,blank=True,null=True)
      username=models.CharField(max_length=30, unique=True)

      #lastname = models.CharField(max_length=30)

      email = models.EmailField(max_length=254,unique=True,blank=True,null=True)

      mobilenumber=models.PositiveIntegerField(unique=True,blank=True,null=True)
      
      datecreated=models.DateTimeField(auto_now_add=True,blank=True,null=True)
      dateupdated=models.DateTimeField(auto_now=True,blank=True,null=True)


      gender=models.CharField(max_length=30,blank=True,null=True)

      companyname=models.CharField(max_length=30,blank=True,null=True)

      postalAddress=models.TextField(blank=True,null=True)
      activation_key = models.CharField(max_length=40,null=True)
      key_expires = models.DateTimeField(null=True)


      
 
      def __unicode__(self):
             return self.username

'''
describing the customer class
inside the customer class we have an email,mobile number ,date of birth ,customer's company name and then their postal address.
the email field should be unique in our database and must have  a maximum length of 254 
the mobile number and the companyname are also unique(database)
username=models.CharField(max_length=30)


when we refer to the customer class in our views we have email as our initials

u
 
'''

class Contact(models.Model):
      username=models.CharField(max_length=30)
      groupname=models.CharField(max_length=100,blank=True,null=True )
      contactnumber=models.PositiveIntegerField(blank=False)

      group=models.ForeignKey('Group',related_name='contacts',blank=True,null=True)
      
      datecreated=models.DateTimeField(auto_now_add=True)
      dateupdated=models.DateTimeField(auto_now=True)

      #customer=models.ForeignKey(Customer,related_name='contacts'
      
      
      def viewcontact():
          pass
      def updatecontact():
          pass
      def deletecontact():
          pass
      def saveContact():
          pass



     

      def __unicode__(self):
           return self.groupname

'''
the contact refers to all contacts under a particular customer.
there is a one to many relationship between the customer and the contact class 
that is why we have the foreignkey at the contact class


when we refer to the contact class in our views we have groupname as our initials 
'''





class Group(models.Model):
      groupname=models.CharField(max_length=30,default='unspecified')
      username=models.CharField(max_length=30)

      datecreated=models.DateTimeField(auto_now_add=True)
      dateupdated=models.DateTimeField(auto_now=True)

      contact=models.ForeignKey(Contact,related_name='groups',blank=True,null=True)
      customer=models.ForeignKey(Customer,related_name='groups',blank=True,null=True)
     
     

      def __unicode__(self):
             return self.groupname

'''
the class group is very important because it provides a group name for each contacts
so we have attribute like datecreated , dateupdated


we also have a customer attribute that is related to the customer class
NB  that it has a related name group with respect to the class Customer



the contact attribute also relate the class Contacts with the class Group
So  a contact may have many groups.(many to one relationship)

'''


class Message(models.Model):
      subject=models.CharField(max_length=30 ,blank=True,null=True)
      username=models.CharField(max_length=30)

      sender=models.CharField(max_length=30)

      receiver=models.CharField(max_length=1000)
      body=models.TextField()


      scheduledate=models.DateTimeField(default=now)
      sent=models.BooleanField(default=False)
      optout=models.BooleanField(default=False)

      customer=models.ForeignKey(Customer,related_name='messages',blank=True,null=True)
      group = models.ManyToManyField("Group")
     
      def createmessagelog():
          pass
      def usetemplate():
          pass

      def __unicode__(self):
             return str(self.receiver)

'''
in the message class we have the subject, sender and one who receives the message
the customer attribute only depict an individual (customer ) with a lot of messages 


the functions will be explained later

when we refer to the Message  class in our views we have subject as our initials 
'''







     




class Servicelog(models.Model):
      smsstatus=models.TextField()

      def createservicelog():
          pass
      


      def __unicode__(self):
             return self.smsstatus

'''
this class only has  and smsstatus attribute
this will depict the status of the sms sent to the gateway


functions will be explained later

when we refer to the servicelog class in our views we have smsstatus as our initials 
'''



'''
registering all our classes 
'''
'''
creating inlines
'''
class ContactInline(admin.TabularInline):     
      model=Contact
class GroupInline(admin.TabularInline):     
      model=Group
class MessageInline(admin.TabularInline):     
      model=Message


'''
extending admin

'''

class CustomerAdmin(admin.ModelAdmin):
      list_display=('username','email','mobilenumber')


      search_fields=('name','email','mobilenumber','companyname')
      list_filter=('datecreated','dateupdated')
      inlines=[GroupInline]
      inlines=[ContactInline]
      inlines=[MessageInline]
      ordering=('-datecreated',)



class GroupAdmin(admin.ModelAdmin):
      list_display=('groupname','contact','customer')


      search_fields=('groupname','contacts','customer')
      list_filter=('datecreated','dateupdated')
      inlines=[ContactInline]
      ordering=('-datecreated',)

admin.site.register(Message)

admin.site.register(Group,GroupAdmin)
admin.site.register(Contact)


admin.site.register(Customer,CustomerAdmin)





      
