# meu_template_teste.py

import django
from django.conf import settings
from django.template import engines

# Configura o Django para rodar fora de um projeto
settings.configure(
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
        },
    ]
)
django.setup()

# Usa o sistema de templates
django_engine = engines["django"]
template = django_engine.from_string("Hello {{ name }}!")
rendered = template.render({"name": "Alice"})

print(rendered)
