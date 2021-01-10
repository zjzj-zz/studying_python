import subprocess

try:
	res = subprocess.check_call('dummy')
except:
	print "Error."
