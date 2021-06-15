from django.shortcuts import render
import requests as re 
from django.http import JsonResponse

def index(request):
	context = {
		'Title' : 'Data Pacitan | Data Pacitan ',
		'Heading' : 'Dashboard Data',
	}

	return render(request, 'index.html', context)

def load_init_pub(request):

	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'publication',
		'lang': 'ind',
		'domain': '3501',
		'page':1,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}

	res = re.get(url, params=params)
	data = res.json()
	posts = data['data'][1]
	print(posts)
	return JsonResponse(data={
		'posts':posts,
	})


	
def load_more_pub(request):
	offset=int(request.POST['offset'])
	page=(offset/10)+1
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'publication',
		'lang': 'ind',
		'domain': '3501',
		'page':page,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}
	posts=[]

	res = re.get(url, params=params)
	data = res.json()

	posts = data['data'][1]
	totalresult = data['data'][0]['total']
	return JsonResponse(data={
		'posts':posts,
		'totalResult':totalresult,
	})