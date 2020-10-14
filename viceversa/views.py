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
	
	count = 0
	flag = 0
	for i in range(len(user_text)):
	    if user_text[i] != ' ' and flag == 0:
	        count += 1
	        flag = 1
	    else:
	        if user_text[i] == ' ':
	            flag = 0

	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':text_rev, 'count_text':count})

	#Так же можно было решить эту задачу селд образом
	#text_rev = user_text[::-1] Этот вариант намного короче и проще
