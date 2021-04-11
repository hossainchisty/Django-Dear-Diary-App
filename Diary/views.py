from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Diary
# Create your views here.

def home(request):
    if request.method == 'POST':
        text = request.POST.get('editordata')
        
        diary_post = Diary(text=text)
        diary_post.save()
        
    diary_post = Diary.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(diary_post, 3)
    try:
        diary_post = paginator.page(page)
    except PageNotAnInteger:
        diary_post = paginator.page(1)
    except EmptyPage:
        diary_post = paginator.page(paginator.num_pages)

    context = {'diary_post':diary_post}
    return render(request, 'index.html', context)


class DiaryUpdateView(UpdateView):
    model = Diary
    fields = ('text',)
    template_name = 'diary_form.html'
    success_url ="/"

class DiaryDeleteView(DeleteView):
    model = Diary
    template_name = 'diary_confirm_delete.html'
    success_url = "/"

