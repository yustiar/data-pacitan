from django.shortcuts import render
import requests as re 
from django.http import JsonResponse

def index(request):
	context = {
		'Title' : 'Data Pacitan | Data Pacitan ',
		'Heading' : 'Dashboard Data',
	}

	return render(request, 'index.html', context)

def load_init_news(request):
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'news',
		'lang': 'ind',
		'domain': '3501',
		'page':1,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}

	res = re.get(url, params=params)
	data = res.json()
	posts = data['data'][1]
	return JsonResponse(data={
		'posts':posts,
	})
def load_more_news(request):
	offset=int(request.POST['offset'])
	page=(offset/10)+1
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'news',
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

def detail_pub(request):
	url = 'https://webapi.bps.go.id/v1/api/view'
	params = {
		'model': 'publication',
		'lang': 'ind',
		'domain': '3501',
		'id':indeks,
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

def load_init_brs(request):
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'pressrelease',
		'lang': 'ind',
		'domain': '3501',
		'page':1,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}

	res = re.get(url, params=params)
	data = res.json()
	posts = data['data'][1]
	return JsonResponse(data={
		'posts':posts,
	})
def load_more_brs(request):
	offset=int(request.POST['offset'])
	page=(offset/10)+1
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'pressrelease',
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

def load_init_data(request):
	sosial = []
	ekonomi = []
	pertanian = []
	url = 'https://webapi.bps.go.id/v1/api/list'
	for i in range(5):
	    params = {
	    	'model': 'subject',
	    	'lang': 'ind',
	    	'domain': '3501',
	    	'page':i+1,
	    	'key': '481cbe5f8403e091cb7abfd4d83829a3'
	    }
	    res = re.get(url, params=params)
	    data = res.json()
	    j=0
	    for j in range(len(data['data'][1])):
	        if data['data'][1][j]['subcat_id'] == 1:
	            sosial.append(data['data'][1][j])
	        elif data['data'][1][j]['subcat_id'] == 2:
	            ekonomi.append(data['data'][1][j])
	        elif data['data'][1][j]['subcat_id'] == 3:
	            pertanian.append(data['data'][1][j])
	return JsonResponse(data={
		'sosial':sosial,
		'ekonomi':ekonomi,
		'pertanian':pertanian,
	})
