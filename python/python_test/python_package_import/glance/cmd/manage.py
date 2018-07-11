import sys

sys.path.append('..//..')
from glance.api.versions import *

create_resource(1)

def main():
    print('from manage.py')

