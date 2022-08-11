import os
import sys

def Error(errovalue, valueError, details, file):
	print(f"""
Interruption with error {errovalue}:{os.getcwd()}:
	
	ValueError : {valueError}
	Details    : {details}
	file       : {file}

exit code 1""")
	exit()
	quit()