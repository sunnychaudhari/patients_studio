# imports from python libraries 
import os, datetime
# imports from django libraries
from django.contrib.auth.models import User
from django.db import models
# imports from django_mongokit libraries
from django_mongokit import connection
from django_mongokit import get_database
from django_mongokit.document import DjangoDocument
from mongokit import IS

try:
    from bson import ObjectId
except ImportError:  # old pymongo
    from pymongo.objectid import ObjectId

##################################################

@connection.register
class Patient(DjangoDocument):
    '''This is a 'Patient' collection where all its information will be 
       recorded for entire diagnosis in hospital
    '''
    objects = models.Manager()
    use_schemaless = True
    collection_name = 'Patients'
    structure = {
        'Patient_ID': unicode, 
        'f_name': unicode,
        'l_name': unicode,
        'address1': unicode,
        'address2': unicode,
        'city': unicode,
        'phone': int,
        'age': int,
        'email': unicode,
        'dr_name': unicode,

      	'created_at': datetime.datetime, # Patients entry 
        'created_by': int, # test required: only ids of Users(hospital staff member)

        'last_update': datetime.datetime, # Update entry
        'modified_by': int, # test required: only ids of Users(hospital staff member)

        'disease': unicode, 
        'prescription': unicode, 

        'collection_set': [ObjectId],  # for indivisual patients reports
    }
    
    required_fields = ['f_name','l_name','address1','city','phone','age', 'dr_name']

    default_values = {'created_at': datetime.datetime.utcnow}
    use_dot_notation = True

