from django.http import HttpResponse
from django.shortcuts import render

def home(request):
 	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	length = len(user_text) #Эта функция len() возвращает длину строки.
	text_rev = ""
	while length>0:
		text_rev += user_text[length-1]
		length = length-1
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':text_rev})

	#Так же можно было решить эту задачу селд образом
	#text_rev = user_text[::-1] Этот вариант намного короче и проще