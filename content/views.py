from django.shortcuts import render

# Create your views here.
def projects_list_view(request):
    return render(request, "content/projects_list.html")