from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
from .models import Vincode,Image
# Create your views here.
def get_key():
	login=requests.post(" https://www.clearvin.com/rest/vendor/login",data={"email":"humbat27.94@mail.ru","password":'yz0zt13q'})
	data=login.json()
	token=data.get("token")
	return token


from ast import literal_eval
import json
def auth_barer(token,vincode):
	header= {'Authorization': 'Bearer ' + token}
	data = {'true' : 'true'}
	url = 'https://www.clearvin.com/rest/vendor/report?vin='+vincode
	response = requests.get(url, json=data, headers=header)
	if response:
		return json.loads(response.content).get("result").get("report")
	else:
		 return JsonResponse({"status":"no vincode found in DATABASE"})
	
def test(request):
	return render(request,"main.html")


def vincode_data(request):
	if request.method=='POST':
		user_vincode=request.POST.get('vincode')
		vin_data=Vincode.objects.filter(vin=user_vincode).first()
		images=Image.objects.filter(Vin__vin=user_vincode)
		if not vin_data:
			# uncomment below in production mode
			token=get_key()
			# comment below token in production mode
			# token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NDcxNTIsImVudmlyb25tZW50IjoidGVzdCIsImlhdCI6MTU3NTQwMTg1MiwiZXhwIjoxNTc3OTkzODUyfQ.CfavrAwR5Q8R2nO9ruHpzvx3jrotqKAfez12UmyBK7U'
			if token!=None:
				user_vincode=request.POST.get('vincode')
				content=auth_barer(token,user_vincode)
				print(content)
				return render(request,"vin_product.html",{"data":content})
			else:
				return HttpResponse(status=500)
		else:
			return render(request,"vin_product.html",{"aze_data":vin_data,"images":images})


def about(request):
	return render(request,"about.html",{})



def contact(request):
	if request.method=='POST':
		print("-----")
		message = request.POST.get('message', '')
		name= request.POST.get('name', '')
		email= request.POST.get('email', '')
		subject= request.POST.get('subject', '')

		send_mail(
			subject+name,
			message,
			email,
			['aytacismayil7@gmail.com'],
			fail_silently=False,
		)
		return redirect("home")
	return render(request,"contact.html",{})