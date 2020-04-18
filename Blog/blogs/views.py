from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import blog
from django.http import HttpResponse

# Create your views here.

def home(request):
     return HttpResponse("Hello World")


class BlogCreate(CreateView):
    
    model = blog
    fields = ['title', 'desc', 'image']
    template_name = 'user_register.html'
    success_url = "/"
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(BlogCreate, self).get_context_data(**kwargs)
        context['page'] = 'create'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogCreate, self).form_valid(form)

    def get_initial(self):
        initials = super(BlogCreate, self).get_initial()
        initials['user'] = self.request.user
        return initials


class BlogUpdate(UpdateView):
   
    model = blog
    fields = ['title', 'desc', 'image']
    template_name = ''
    success_url = "/"
    raise_exception = True
    def get_context_data(self, **kwargs):        
        context = super(BlogUpdate, self).get_context_data(**kwargs)
        context['page'] = 'update'
        return context

    def form_valid(self, form):
        return super(BlogUpdate, self).form_valid(form)

class BlogDelete(DeleteView):
    
    model = blog
    success_url = "/"
   