#Other option : importlib.metadata

#Pip freeze get the modules being used

import platform #Doesn't requiere any librery to execute

print('-------------------------------')
x = platform.architecture()
print('Architecture: ', x)
x = platform.processor()
print('Processor: ', x)
x = platform.machine()
print('Machine: ', x)
x = platform.node()
print('Name: ', x)
x = platform.platform()
print('system: ', x)
print('-------------------------------')
x = platform.python_build()
print('Python Build: ', x)
x = platform.python_implementation()
print('Python implementation: ', x)
print('-------------------------------')

#To get RAM
#pip install psutil

import psutil

x = psutil.virtual_memory()
print('RAM: \n', x)
x = psutil.disk_usage('/')
print('Disk: \n', x)
x = psutil.cpu_count()
print('Nucleos CPU: ', x)
x = psutil.cpu_freq()
print('Frequency CPU: ', x, ' Mhz')
print('-------------------------------')