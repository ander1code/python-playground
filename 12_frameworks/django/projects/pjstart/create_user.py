import os
import django
# from django.http import request

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pjstart.settings')
django.setup()

from django.contrib.auth.models import User
# User.objects.create_user('Anderson','anderson','@Anderson1981')

users = User.objects.all()
for u in users:
    print(u)

from django.contrib.auth import authenticate, login, logout

user = authenticate(username='Anderson', password='@Anderson1981')
if user is not None:
    print('Successfully authenticated.')
else:
    print('Invalid user.')

if user.is_authenticated:
    # session = login(request, user)
    # print(f'Session: {session}')
    print('Successfully authenticated.')
    del user # logout(request)  # simulando o logout!
    try:
        if user.is_authenticated:
            print('Successfully authenticated.')
        else:
            print('Invalid user.')
    except Exception as error:
        print(f'User unlogged.')
else:
    print('Invalid user.')

