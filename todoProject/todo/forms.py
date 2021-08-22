from django import forms

class AddTaskForm(forms.Form):
    task = forms.CharField(label="Task")
