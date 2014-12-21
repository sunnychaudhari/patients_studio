''' -- imports from installed packages -- '''
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django_mongokit import get_database

try:
    from bson import ObjectId
except ImportError:  # old pymongo
    from pymongo.objectid import ObjectId

from p_app.models import Patient

#####################################################################

collection = get_database()[Patient.collection_name]   # This broughts the 'Patient'  collection from 'patients_store' DB

def homepage(request, p_id=None):	
	'''
	1.This method is for savig patient details and displaying list of patients who has 
	  come for diagnosis 
	2.POST request handels the editing and saving new patients
	3.Outside of POST request part is handeled for displaying patients list and particular
	  patient details
	'''
	if request.method == "POST":

		fname = request.POST.get('f_name','')
		lname = request.POST.get('l_name','')
		city = request.POST.get('city','')
		age = request.POST.get('age','')
		phone = request.POST.get('phone','')
		email = request.POST.get('email','')
		addr1 = request.POST.get('addr1','')
		addr2 = request.POST.get('addr2','')
		dr_name = request.POST.get('dr_name','')
		disease = request.POST.get('disease','')
		prescription = request.POST.get('prescription','')

		patient = collection.Patient.one({'phone': phone,'f_name': unicode(fname) })

		if patient is None:
			try:
				patient = collection.Patient()
				patient.f_name = unicode(fname)
				patient.l_name = unicode(lname) 
				patient.city = unicode(city)
				patient.age = int(age)
				patient.phone = int(phone)
				patient.email = unicode(email)
				patient.address1 = unicode(addr1)
				patient.address2 = unicode(addr2)
				patient.dr_name = unicode(dr_name)
				patient.disease = unicode(disease)
				patient.prescription = unicode(prescription)
				patient.save()
			except Exception as err:
				print "\nerror:",err,"\n"

		else:
			print "Patient name ",patient.f_name," already registered\n"

	p = None
	patient_list = collection.Patient.find()

	if p_id:
		p = collection.Patient.one({'_id': ObjectId(p_id) })

	return render_to_response("home.html",{'patient_list': patient_list, 'patient': p},context_instance=RequestContext(request))

