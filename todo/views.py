from django.shortcuts import render
from models import Todo
from .forms import TodoForm
from django.http import HttpResponseRedirect
# from .models import List 


# Create your views here.
def todo_list(request):
	items = Todo.objects.all()
	# form = TodoForm(request.POST or None)
	context = {'items': items} #'form': form}
	template = 'todo_list.html'
	return render(request, template, context)

def todo_form(request):
	form = TodoForm(request.POST or None)
	if form.is_valid():
		title = form.cleaned_data['title']
		description = form.cleaned_data['description']
		new_todo = Todo(title=title, description=description)
		new_todo.save()
		return HttpResponseRedirect('/list')
	return render(request, 'todo_form.html', {'form': form})

  
# def status_report(request):  
#   todo_listing = []  
#   for todo_list in List.objects.all():  
#     todo_dict = {}  
#     todo_dict['list_object'] = todo_list  
#     todo_dict['item_count'] = todo_list.item_set.count()  
#     todo_dict['items_complete'] = todo_list.item_set.filter(completed=True).count()  
#     todo_dict['percent_complete'] = int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100)  
#     todo_listing.append(todo_dict)  
#   return render(request, 'status_report.html', { 'todo_listing': todo_listing })

# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">  
# <html xmlns="http://www.w3.org/1999/xhtml">  
#   <head>  
#     <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />  
#     <title>To-do List Status Report</title>  
#   </head>  
#   <body>  
#     <h1>To-do list status report</h1>  
# {% for list_dict in todo_listing %}  
#     <h2>{{ list_dict.list_object.title }}</h2>  
#     <ul>  
#       <li>Number of items: {{ list_dict.item_count }}</li>  
#       <li>Number completed: {{ list_dict.items_complete }} ({{ list_dict.percent_complete }}%)</li>  
#     </ul>  
# {% endfor %}  
#   </body>  
# </html>