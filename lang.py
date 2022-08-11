from assigner import assigner
from evaluator import Evaluator
from sys import argv
import error
file = argv[1]

def main():
	try:
		data = open(file, "r")
	except:
		error.Error("FileNameError", "No file found '"+file+"'", "NONE", "NONE")
	if ".lang" not in file:
		error.Error("FileNameError", "File is has no '.lang' extention exmp : 'project.lang'", "None", "NONE")
	data = data.readlines()
	ast = assigner(data).build()
	Evaluator().run(ast)

if __name__ == '__main__':
	main()