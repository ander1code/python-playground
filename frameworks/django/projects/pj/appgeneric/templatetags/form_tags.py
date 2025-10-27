from django import template

register = template.Library()

@register.filter(name="add_class")
def add_class_function(field, class_css):
    return field.as_widget(attrs={'class': class_css})

# @register.filter(name="add_readonly")
# def add_readonly_function(field, value):
#     return field.as_widget(attrs={'readonly': value})  # Corrigido aqui
