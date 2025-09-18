from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    """
    Adiciona classes CSS ao widget de um campo do formulário Django.
    Uso: {{ form.campo|add_class:"classe1 classe2" }}
    """
    return field.as_widget(attrs={"class": css})
