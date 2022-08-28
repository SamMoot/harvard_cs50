# django has the ability to create forms for us. so we don't have to create it from scratch  
from http.client import HTTPResponse
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


#now rather than having to change the html anytime there's data changes to the application, 
# we can change the task form. 

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    # example: adding data - priority
    priority = forms.IntegerField(label="Priority", min_value = 1, max_value = 8)
    
    #django does client side validation automatically. this means the server isn't doing any work. 
    # the webpage is encoded so that it can constrain the inputs that are valid. 
    # in general, we want to to have both server & client side validation. e.g. server validation is more up ot date. or client side validation can be disabled. 



# Create your views here.
def index(request):
    if "tasks" not in request.session: 
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks":request.session["tasks"]
    })

#opt 1 ) creating html from scratch 
def add(request):
    return render(request, "tasks/add.html")

# opt2) 
def add_option2(request):

    #a server side validation for post methods
    # NewTaskForm() creates a new form without anything. 
        #populate the new form with some data which is request.post.
        # request.post is all the data the user submitted. 

    # normal paradigm for webpages - first get the form then also allows for a post request. 
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else: 
            return render(request, "tasks/add_2.html", {
                "form":form
            })

    return render(request, "tasks/add_2.html", {
        "form": NewTaskForm()
    })

# sessions - Django remembers who you are. store data about your data. e.g. store all of your tasks. 

# python manage.py migrate - creates the tables in django