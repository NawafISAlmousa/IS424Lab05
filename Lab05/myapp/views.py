from django.shortcuts import render
from django import forms

persons = []
names = []
# Create your views here.
def default(request):
    return render(request, "myapp/default.html", {"listOfNames": names})

def add(request):
    if request.method == "POST":
        form = PersonsForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # persons.append(Person(username,password))
            # names.append(username)
            person = Person(username, password)
            persons.append(person)
            names.append(person.objusername)
    return render(request, "myapp/add.html", {"form":PersonsForm})

class Person():
    def __init__(self, objusername, objpassword):
        self.objusername = objusername
        self.objpassword = objpassword
class PersonsForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password")
