from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView
from . import models
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name='index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model=models.School     # ListView takes the model name and add _list to it as a default contex return( like= School_list)

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School           # DetailView just return the model lower case (like = school)
    template_name = 'basic_app/school_detail.html'

# school createView
class SchoolCreateView(CreateView):
    fields =('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model=models.School

class SchoolDeleteView(DeleteView):
    model=models.School
    # template_name ='school_confirm_delete.html'
    success_url = reverse_lazy('basic_app:list')



