
import error
def init(name, file):
	illegals = ["+", "-", "%", "*", "#", "<", "(", ")", "@", "#"]
	ints = list("1234567890")
	keys = ["PRINTNEW", "DIM"]
	if name in keys:
		error.Error("NameError", "Name cannot be a keyword", name, file)
	for i in name:
		if i in illegals:
			error.Error("NameError", "illegal Name character '"+i+"'", name, file)
	if name[0] in ints:
		error.Error("NameError", "Illegal starting name '"+name[0]+"'", name, file)
