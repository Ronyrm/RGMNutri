import sys
import os

from App import app as application
from App import db 

sys.path.append(os.path.dirname(__file__))

if __name__ == '__main__':
     application.run(debug=False,host='0.0.0.0') #Docker
     #application.run()