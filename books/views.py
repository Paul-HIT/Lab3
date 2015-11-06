# -*- coding: utf-8 -*-
from django.shortcuts import render, RequestContext
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from books.models import Book, Author

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 30:
			errors.append('Please enter at most 30 characters.')
		else:
			author = Author.objects.filter(Name__icontains=q)
			books = Book.objects.filter(AuthorID=author)
			return render_to_response('search_results.html', {'books': books, 'q': q})
	return render_to_response('search_form.html', {'errors': errors})

def details(request, BookID):
	books = Book.objects.filter(ISBN=BookID)
	return render_to_response('details.html', {'books': books})

def delete(request, Search, BookID):
	if request.method == 'POST':
		Book.objects.get(ISBN=BookID).delete()
		return HttpResponseRedirect('/?q='+Search)
	else:
		books = Book.objects.filter(ISBN=BookID)[0]
	return render(request, 'delete.html', {'books': books}, context_instance = RequestContext(request))

def edit(request, Search, BookID):
	if request.method == 'POST':
		publisher = request.POST['publisher']
		name = request.POST['Name']
		PD = request.POST['PD']
		price = request.POST['Price']
		if publisher:
			Book.objects.filter(ISBN=BookID).update(Publisher = publisher)
		if name:
			author = Author.objects.filter(Name=name)[0]
			Book.objects.filter(ISBN=BookID).update(AuthorID=author)
		if PD:
			Book.objects.filter(ISBN=BookID).update(PublishDate = PD)
		if price:
			Book.objects.filter(ISBN=BookID).update(Price = price)
		books = Book.objects.filter(ISBN=BookID)[0]
		return HttpResponseRedirect('/?q='+Search)
	else:
		books = Book.objects.filter(ISBN=BookID)[0]
	return render(request, 'edit.html', {'books': books, 'q': Search}, context_instance = RequestContext(request))
def newauthor(request):
	error = []
	if request.method == 'POST':
		authorID = request.POST['AuthorID']
		name = request.POST['Name']
		age = request.POST['Age']
		country = request.POST['Country']
		if not authorID or not name or not age or not country:
			if not authorID:
				error.append('没有填写ID')
			if not name:
				error.append('没有填写姓名')
			if not age:
				error.append('没有填写年龄')
			if not country:
				error.append('没有填写国籍')
			return render(request, 'newauthor.html', {'Error': error}, context_instance = RequestContext(request))
		else:
			new_obj = Author(AuthorID=authorID, Name=name, Age=age, Country=country)
			new_obj.save()
			return HttpResponseRedirect('/new')
	return render(request, 'newauthor.html', {'Error': error}, context_instance = RequestContext(request))
	
	
	
	
def new(request):
	error = []
	authorforselect = Author.objects.all()
	if request.method == 'POST':
		title = request.POST['Title']
		isbn = request.POST['ISBN']
		getauthor = request.POST['AuthorID']
		author = Author.objects.filter(Name=getauthor)
		publisher = request.POST['Publisher']
		publishdate = request.POST['PD']
		price = request.POST['Price']
		if not author or not title or not isbn or not publisher or not publishdate or not price or len(author) > 1:
			if not author:
				error.append('作者姓名输入有误')
			if not title:
				error.append('没有填写标题')
			if not isbn:
				error.append('没有填写ISBN编号')
			if not publisher:
				error.append('没有填写出版社')
			if not publishdate:
				error.append('没有填写出版日期')
			if not price:
				error.append('没有填写价格')
			return render(request, 'new.html', {'Author': authorforselect, 'Error': error}, context_instance = RequestContext(request))
		else:
			new_obj = Book(ISBN=isbn, Title=title, AuthorID=author[0], Publisher=publisher, PublishDate=publishdate, Price=price)
			new_obj.save()
			return HttpResponseRedirect('/')
	return render(request, 'new.html', {'Author': authorforselect, 'Error': error}, context_instance = RequestContext(request))















