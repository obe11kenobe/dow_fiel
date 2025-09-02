from django import forms
from .models import Data

class DataCreate(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['nomenclature', 'document_number', 'old_order', 'quantity', 'cost', 'resource', 'new_order']
        exclude = ['date']  # Исключаем поле date, так как оно auto_now_add=True
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем CSS классы для всех полей
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Введите {field.label.lower()}'
            })
