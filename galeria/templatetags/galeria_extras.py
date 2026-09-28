from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    params = context['request'].GET.copy()
    for chave, valor in kwargs.items():
        if valor in (None, ''):
            params.pop(chave, None)
        else:
            params[chave] = valor
    return params.urlencode()
