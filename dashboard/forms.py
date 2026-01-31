from django import forms
from blogs.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs.update({
                'placeholder':f'Enter new category',
                'class':'p-2 pl-6 rounded-md text-gray-400 ring outline-none ring-gray-200 transition-all ease-in duration-200 focus:ring-indigo-600'
            })