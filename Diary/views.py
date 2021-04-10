from django.shortcuts import render
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

