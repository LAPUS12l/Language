import error
def make(raw_string, file, variables):
	result = ""
	id = ""
	tmp = ""
	ints = list("1234567890")
	operands = list("+-*/<>")
	for i in raw_string:
		tmp += i
		if i == '"' and id == "":
			id = "char"
		elif i == '"' and id == "char":
			result += tmp
			tmp = ""
			id = ""
		elif i == "$" and id == "":
			tmp = ""
			id = "ready"
		elif i != "{" and id == "ready":
			error.Error("SyntaxError", "Invalid syntax '"+i+"'. Expected '{'", raw_string, file)
		elif i == "{" and id == "ready":
			id = "varname"
			tmp = ""
		elif i != "}" and id == "varname":
			pass
		elif i == "T" and id == "":
			id = "Attemp-t"
		elif i == "R" and id == "Attemp-t":
			id = "Attemp-tr"
		elif i == "U" and id == "Attemp-tr":
			id = "Attemp-tru"
		elif i == "E" and id == "Attemp-tru":
			result += "True"
			id = ''
		elif i == "}" and id == "varname":
			tmp = tmp[0:len(tmp)-1].strip()
			try:
				result += variables[tmp]
			except:
				error.Error("NameError", "'"+tmp+"' is not defined", raw_string, file)
			id = ""
			tmp = ""
		elif i == "=" and id == "":
			id = "atempting-eqeq"
		elif i == " " and id == "":
			tmp = ""
			continue
		elif i == "." and id == "":
			id = "atempting-add-str"
			tmp = ""
		elif i in ints and id == "":
			tmp = ""
			result += i
		elif i == "." and id == "atempting-add-str":
			result += "+"
			tmp = ""
			id = ""
		elif i == "N" and id == "":
			id = "At-n"
		elif i == "U" and id == "At-n":
			id = "At-nu"
		elif i == "L" and id == "At-nu":
			id = "At-nul"
		elif i == "L" and id == "At-nul":
			result += "None"
			id = ""
		elif i == "@" and id == "":
			id = "att-i"
		elif i == "@" and id == "att-i":
			result += "in"
			id = ""
		elif i == "|" and id == "":
			id = "a-o"
		elif i == "|" and id == "a-o":
			result += " or "
			id = ''
		elif i == "&" and id == "":
			result += " and "
		elif i != "." and id == "atempting-add-str":
			error.Error("SyntaxError", "Invalid syntax '"+tmp+"'. Expected '.'", raw_string, file)
		elif i == "=" and id == "atempting-eqeq":
			result += tmp
			tmp = ""
			id = ""
		elif i in operands and id == "":
			result += tmp
			tmp = ""
		elif i != "=" and id == "atempting-eqeq":
			error.Error("SyntaxError", "Invalid syntax '"+i+"'. Expected '='", raw_string, file)

		#Just pass processing things
		elif id == "char" and i != '"':
			pass
		elif id == "varname" and i != "}":
			pass
		else:
			error.Error("SyntaxError", "Invalid syntax '"+i+"'. Expected 'None'", raw_string, file)
	try:
		eval(result)
	except:
		error.Error("CharError", "Unknown Invalid input", raw_string, file)
	return result
def out_put_natural(string):
	out_put = ""
	while string != "":
		if string[0:4] == "True":
			out_put += "TRUE"
			string = string.replace("True", "", 1)
		elif string[0:5] == "False":
			out_put += "FALSE"
			string = string.replace("False", "", 1)
		elif string[0:4] == "None":
			out_put += "NULL"
			string = string.replace("None", "", 1)
		else:
			out_put += string[0]
			string = string.replace(string[0], "", 1)

	return out_put