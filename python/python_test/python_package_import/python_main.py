import sys,os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
sys.path.append(BASE_DIR)


from glance.api import versions

