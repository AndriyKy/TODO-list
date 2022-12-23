from django import forms

from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.prefetch_related("tasks"),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"
