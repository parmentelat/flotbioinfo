# file to place in /etc/jupyter
# probably temporary but fine for now with a single user that has a git repo
import os, os.path
os.environ['PYTHONPATH'] = os.path.join(os.getenv("HOME"),"flotbioinfo/modules")
