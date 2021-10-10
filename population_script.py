import os
from django.contrib.auth import authenticate

from django.template.defaultfilters import title
os.environ.setdefault('DJANGO_SETTINGS_MODULE','yishi_project.settings')

import django
django.setup()
from yishi.models import Products, commentP
from django.contrib.auth.models import User