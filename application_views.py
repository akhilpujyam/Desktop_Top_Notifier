from django.shortcuts import render
from django.http import HttpResponse
import time
from win10toast import ToastNotifier
import datetime
from django import forms
from django.http import HttpResponseRedirect
  
  



def index(request):
    return render(request,'tab1_template.html')




def getTimeInput(a,b,c):
	hour =a
	minutes =b
	seconds =c
	time_interval = seconds+(minutes*60)+(hour*3600)
	return time_interval


def log():
	now = datetime.datetime.now()
	start_time = now.strftime("%H:%M:%S")
	with open("log.txt", 'a') as f:
		f.write(f"You drank water {now} \n")
	return 0


def water_notify():
	notification = ToastNotifier()
	notification.show_toast("Time to drink water")
	log()
	return 0
def eye_notify():
	notification = ToastNotifier()
	notification.show_toast("Time to relax your eyes")
	log()
	return 0
def move_notify():
	notification = ToastNotifier()
	notification.show_toast("Time to just walk and get back to work")
	log()
	return 0


def starttime(time_interval,time_interval2,time_interval3,tot_time):
	k,k1,k2,k3=0,0,0,0
	while k<=tot_time:
		time.sleep(1)
		if(k1==time_interval or k2==time_interval2 or k3==time_interval3):
			if(k1==time_interval):
				water_notify()
				k1=0
			if(k2==time_interval2):
				eye_notify()
				k2=0
			if(k3==time_interval3):
				move_notify()
				k3=0
		
		k1+=1
		k2+=1
		k3+=1
		k+=1
	print("Thanks For Using Service")
	return 0


def starting(request):
	print("countdown started")
	a,b,c,d=list(map(int,request.GET["num1"].split(":"))),list(map(int,request.GET["num2"].split(":"))),list(map(int,request.GET["num3"].split(":"))),float(request.GET["num4"])
	time_interval = getTimeInput(a[0],a[1],a[2])
	time_interval2 = getTimeInput(b[0],b[1],b[2])
	time_interval3 = getTimeInput(c[0],c[1],c[2])
	print(time_interval,time_interval2,time_interval3)
	t=d*60*60
	tot_time=t
	take=starttime(time_interval,time_interval2,time_interval3,tot_time)
	return render(request,"success_print.html")


    
