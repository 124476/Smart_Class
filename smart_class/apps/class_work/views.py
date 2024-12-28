from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from .models import Work, Computer


class WorkListView(LoginRequiredMixin, ListView):
    model = Work
    template_name = 'class_work/work_list.html'
    context_object_name = 'works'

    def get_queryset(self):
        return Work.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for work in context['works']:
            work.computers = Computer.objects.filter(work=work)
        return context


class WorkCreateView(LoginRequiredMixin, CreateView):
    model = Work
    template_name = 'class_work/work_form.html'
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('class_work:list')


class WorkUpdateView(LoginRequiredMixin, UpdateView):
    model = Work
    template_name = 'class_work/work_form.html'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy('class_work:list')


class WorkDeleteView(LoginRequiredMixin, DeleteView):
    model = Work
    template_name = 'class_work/work_confirm_delete.html'
    success_url = reverse_lazy('class_work:list')


class ComputerCreateView(LoginRequiredMixin, CreateView):
    model = Computer
    template_name = 'class_work/computer_form.html'
    fields = ['name', 'work']

    def get_success_url(self):
        return reverse_lazy('class_work:list')


class ComputerUpdateView(LoginRequiredMixin, UpdateView):
    model = Computer
    template_name = 'class_work/computer_form.html'
    fields = ['name', 'work']

    def get_success_url(self):
        return reverse_lazy('class_work:list')


class ComputerDeleteView(LoginRequiredMixin, DeleteView):
    model = Computer
    template_name = 'class_work/computer_confirm_delete.html'
    success_url = reverse_lazy('class_work:list')


class ComputerControlView(LoginRequiredMixin, View):
    def post(self, request, pk):
        computer = get_object_or_404(Computer, pk=pk, work__user=request.user)
        action = request.POST.get("action")

        if action == "toggle_power":
            computer.is_active = not computer.is_active
            messages.success(
                request,
                f"Компьютер '{computer.name}' был {'включен' if computer.is_active else 'выключен'}."
            )
        elif action == "toggle_signal":
            computer.signal = not computer.signal
            messages.success(
                request,
                f"Сигнал на компьютере '{computer.name}' был {'включен' if computer.signal else 'выключен'}."
            )
        else:
            messages.error(request, "Некорректное действие.")

        computer.save()
        return redirect('class_work:list')