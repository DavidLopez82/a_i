import datetime
from configparser import ConfigParser
import sys

parser = ConfigParser()
parser.read('source/parameters.ini')

date = datetime.datetime.now()
parser.set('parametros de cultivo', 'fecha_inicio_plan', str(date))
print(parser.get('parametros de cultivo', 'fecha_inicio_plan'))
s = parser.get('parametros de cultivo', 'fecha_inicio_plan')
#d = datetime.date.fromisoformat("{0:9}".format(s))
print(datetime.date.fromisoformat(s[0:10]))
parser.write(open('source/parameters.ini', 'w+'))
