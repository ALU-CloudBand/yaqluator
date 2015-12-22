import sys
path = '/var/www/yaqluator.com/python'

if path not in sys.path:
    sys.path.append(path)

from api import app as application