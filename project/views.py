from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from .models import Progect,task,category
from .forms import project_forms,ProjectUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class ProjectView(LoginRequiredMixin,ListView):
    model = Progect
    template_name = r'C:\Users\ali\PycharmProjects\pythonProject\pythonProject1\todo\templates\project_list.html'
    paginate_by = 2
    def get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id':self.request.user}
        q = self.request.GET.get('q', None)

        if q:
            where['title__icontains'] = q

        return query_set.filter(**where)
class ProjectCreate(LoginRequiredMixin,CreateView):
    model = Progect
    form_class = project_forms
    template_name = 'create_project.html'
    success_url = reverse_lazy('view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    36
class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Progect
    form_class = ProjectUpdateForm
    template_name = 'update_project.html'

    def test_func(self):
        return self.get_object().user.id == self.request.user.id

    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])



class TaskCreateView( LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model =task
    fields = ['project', 'description']
    template_name = 'create_task.html'

    def test_func(self):
        project_id = self.request.POST.get('project', '')

        return Progect.objects.get(pk=project_id).user_id == self.request.user.id
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])



class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = task
    fields = ['is_complete']
    http_method_names = ['post']

    def test_func(self):
        return self.get_object().project.user.id == self.request.user.id
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])






class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = task
    http_method_names = ['post']

    def test_func(self):
        return self.get_object().project.user.id == self.request.user.id
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])



class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Progect
    template_name = 'delete_task.html'
    success_url = reverse_lazy('view')

    def test_func(self):
        return self.get_object().user.id == self.request.user.id

