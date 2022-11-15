from django.shortcuts import render
# from django.http import HttpResponse

from . import util
import markdown2
from django import forms

def create(request):
    return render(request, "encyclopedia/create.html", {
        # "save": util.save_entry(name, "name.md")
        "name": util.list_entries()
    })
    
def wiki(request, name): 
    if util.get_entry(name) == None:
        return render(request, "encyclopedia/entry.html", {
            # "name": util.list_entries()
            "title": "Not found", "body": "Not Available, try creating it"
        })
    f = open(f"entries/{name}.md","r")
    f = f.read()
    html = markdown2.markdown(f)
    
    return render(request, "encyclopedia/entry.html", {
        # "name": util.list_entries()

        "title": name, "body2": html
    })


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
    
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
