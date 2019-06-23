from populate import base
from account.models import User


def populate(): 
    print('Creating admin account ... ', end='')
    User.objects.all().delete()
    User.objects.create_superuser(username='admin', password='0000', email=None, fullName='管理者')
    print('done')


if __name__ == '__main__':
    populate()