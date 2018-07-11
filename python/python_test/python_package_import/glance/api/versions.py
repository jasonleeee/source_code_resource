import sys

sys.path.append('..//..')
from glance.api.policy import *
from glance.glance import *
from lib_api import *

get()
glance()
api_test()


def create_resource(conf):
    print('from version.py: ',conf)
