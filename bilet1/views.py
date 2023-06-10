from django.shortcuts import render
from django.views.generic import ListView
from bilet1.models import Dictionary


def listzadan(request):
    return render(request, 'bilet1/main.html')

def bilet_1(request):
    news = Dictionary.objects.all()
    return render(request, 'bilet1/bilet_1.html', {'news':news})

class Search(ListView):
    template_name = 'bilet1/bilet_1.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        return Dictionary.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

