from django.shortcuts import render
from django.http import HttpResponse
from .models import Students, Logs
import datetime

# Create your views here.
def home(request):
	return render(request, 'attendance/home.html')

def index(request):
	return render(request, 'attendance/index.html')

def index1(request):
	logs = Logs.objects.all()
	logf = []
	for log in logs:
		if str(log.date) == str(datetime.datetime.now())[:10]:
			logf.append(log)
	logf.reverse()
	dataset = { 'log' : logf}
	return render(request, 'attendance/attendance.html', dataset)

def details(request):
	return render(request, 'attendance/details.html')

def details1(request):
	users = Students.objects.all()
	us = []
	for user in users:
		us.append(user)
	us.reverse()
	userset = {'users': us}
	return render(request, 'attendance/userdetails.html', userset)

def process(request):
	card = request.GET.get('card_id', 0)
	users = Students.objects.all()
	for user in users:
		if user.card_id == int(card): #Registered Card Detected
			ans = attend(user)
			return HttpResponse(ans)
	return HttpResponse('New Card Detected')

def attend(user):
	logs = Logs.objects.all()
	for log in logs:
		if log.card_id == int(user.card_id):
			if log.time_out == None:
				log.time_out = datetime.datetime.now()
				log.save()
				resp = 'logout'
				return resp
	new_log = Logs(name=user.name, card_id=user.card_id, team = user.team, date=datetime.datetime.now(), time_in=datetime.datetime.now())
	new_log.save()
	resp = 'login'
	return resp