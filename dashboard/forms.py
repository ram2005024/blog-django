from django import forms
from blogs.models import Category,Blog

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
class PostForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','category','featured_image','is_featured','short_description','short_body','status')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_label,field in self.fields.items():
            widget_type=field.widget.__class__.__name__
            if widget_type in ['TextInput','Textarea']:
                field.widget.attrs.update({
                    'placeholder':f'Enter {field_label}',
                    'class':'w-full p-2 pl-5 text-gray-400 resize-none ring ring-gray-200 rounded-lg outline-none text-sm transition-all duration-200 focus:ring-indigo-400'

                })
            elif widget_type=='Select':
                 field.widget.attrs.update({
                    'class': 'w-full ring ring-gray-200 rounded-lg outline-none text-sm transition-all duration-200 focus:ring-indigo-400 p-2 '
                })
            elif widget_type == 'ClearableFileInput':
                 field.widget.attrs.update({
                'class': 'block w-full text-sm text-gray-500file:mr-4 file:py-2 file:px-4file:rounded-md file:border-0file:text-sm file:font-semiboldfile:bg-indigo-600 file:text-whitehover:file:bg-indigo-700'
    })

            elif widget_type == 'CheckboxInput':
                field.widget.attrs.update({
                    'class': 'h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500'
                })

