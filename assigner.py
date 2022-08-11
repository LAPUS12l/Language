from init_name import init
import error
import sys
def _reAst(raw_code):
	return assigner(raw_code).build()
class assigner:
	def __init__(self, code):
		self.ast = []
		self.code = code

		self.in_if = False
		self.if_arg = ""
		self.if_ = []

		self.in_label = False
		self.label_name = ""
		self.label_ = []

		self.in_while = False
		self.while_arg = ""
		self.while_ = []

		self.in_for = False
		self.for_ = []
		self.for_var_handler = ""
		self.count_ = ''
	def build(self):
		for i in self.code:
			#CHECK CODE
			if i[len(i)-1] == "\n":
				i = i[0:len(i)-1]
			if self.in_if is False and self.in_label is False and self.in_while is False and self.in_for is False: #
				i = i.rstrip()
				if i[0:len("PRINTNEW")].upper() == "PRINTNEW":
					i = i.replace(i[0:len("PRINTNEW")], "", 1)
					i = i.strip()
					self.ast.append({"printnew":i})
				elif i[0:3].upper() == "DIM":
					i = i.replace(i[0:len("DIM")], "", 1).strip()
					self.name = ""
					self.value = ""
					self.id = ""
					for l in i:
						if l != "=" and self.id == "":
							self.name += l
						elif l == "=" and self.id == "":
							self.id = "value"
						else:
							self.value += l
					self.name = self.name.strip()
					init(self.name, sys.argv[1])
					self.value = self.value.strip()
					self.ast.append({"dimention":[self.name, self.value]})
				elif i.strip().upper() == "DIE":
					self.ast.append({"DIE":"0"})
				elif i[0:5].upper() == "PRINT":
					i = i.replace(i[0:5], "", 1).strip()
					self.ast.append({"print":i})
				elif i[0:2].upper() == "IF":
					self.saved = i
					i = i.replace(i[0:2], "", 1).strip()
					if i[len(i)-4:len(i)].upper() != "THEN":
						error.Error("SymbolError", "Invalid symbol expected 'THEN'", self.saved, sys.argv[1])
					i = i[0:len(i)-4].strip()
					self.if_arg = i
					self.in_if = True
					continue
				elif i[0:len("CONVERTSTR")].upper() == "CONVERTSTR":
					i = i.replace("CONVERTSTR", "", 1).strip()
					init(i, sys.argv[1])
					self.ast.append({"CONVERTSTR":i})
				elif i[0:5].upper() == "INPUT":
					i = i.replace(i[0:5], "", 1).strip()
					init(i, sys.argv[1])
					self.ast.append({"INPUT":i})
				elif i[0:5].upper() == "LABEL":
					if i[len(i)-2:len(i)].upper() != "DO":
						error.Error("SymbolError", "Invalid symbol expected 'DO'", i, sys.argv[1])
					i = i[0:len(i)-2]
					i = i.replace(i[0:5], "", 1)
					init(i, sys.argv[1])
					self.label_name = i.strip()
					self.in_label = True
					continue
				elif i[0:len("CONVERTINT")].upper() == "CONVERTINT":
					i = i.replace("CONVERTINT", "", 1).strip()
					init(i, sys.argv[1] )
					self.ast.append({"CONVERTINT":i})
				elif i[0:len("GOTO")].upper() == "GOTO":
					i = i.replace(i[0:4], "", 1).strip()
					self.ast.append({"GOTO":i})
				elif i[0:len("WHILE")].upper() == "WHILE":
					if i[len(i)-2:len(i)].upper() != "DO":
						error.Error("SymbolError", "Invalid symbol expected 'DO'", i, sys.argv[1])
					i = i[0:len(i)-2]
					i = i.replace(i[0:5], "", 1).strip()
					self.while_arg = i
					self.in_while = True
					continue
				elif i[0:5].upper() == "SLEEP":
					i = i.replace(i[0:5], "", 1).strip()
					self.ast.append({"SLEEP":i})
				elif i[0:len("FOR")].upper() == "FOR":
					if i[len(i)-2:len(i)].upper() != "DO":
						error.Error("SymbolError", "Invalid symbol expected 'DO'", i, sys.argv[1])
					i = i[0:len(i)-2]
					i = i.replace(i[0:3], "", 1).strip()
					self.id = ""
					for l in i:
						if l != "," and self.id == "":
							self.for_var_handler += l
						elif l == "," and self.id == "":
							init(self.for_var_handler, sys.argv[1])
							self.id = "count"
						elif self.id == "count":
							self.count_ += l
					self.in_for = True
					continue

				else:
					#ATTOMS IS TO CHECK A VALUE LIKE 'hello world' IF THERES AN ERROR WITH THE STRING
					self.ast.append({"la atom":i})

			if self.in_if is True:
				if i.upper() != "END":
					if i[0] != "\t":
						error.Error("IndentationError", "Invalid indent expected '\\t'. not '"+i[0]+"'", i, sys.argv[1])
					i = i.replace("\t", "", 1)
					self.if_.append(i)
				elif i.upper() == "END":
					self.ast.append({"IF":[self.if_arg, _reAst(self.if_)]}) #Index of the array
					self.if_ = []
					self.if_arg = ""
					self.in_if = False
			if self.in_label is True:
				if i.upper() != "END":
					if i[0] != "\t":
						error.Error("IndentationError", "Invalid indent expected '\\t'. not '"+i[0]+"'", i, sys.argv[1])
					i = i.replace("\t", "", 1)
					self.label_.append(i)
				elif i.upper() == "END":
					self.ast.append({"LABEL":[self.label_name, _reAst(self.label_)]}) #Index of the array
					self.label_ = []
					self.label_name = ""
					self.in_label = False
			if self.in_while is True:
				if i.upper() != "END":
					if i[0] != "\t":
						error.Error("IndentationError", "Invalid indent expected '\\t'. not '"+i[0]+"'", i, sys.argv[1])
					i = i.replace("\t", "", 1)
					self.while_.append(i)
				elif i.upper() == "END":
					self.ast.append({"WHILE":[self.while_arg, _reAst(self.while_)]}) #Index of the array
					self.while_ = []
					self.while_arg = ""
					self.in_while = False
			if self.in_for is True:
				if i.upper() != "END":
					if i[0] != "\t":
						error.Error("IndentationError", "Invalid indent expected '\\t'. not '"+i[0]+"'", i, sys.argv[1])
					i = i.replace("\t", "", 1)
					self.for_.append(i)
				elif i.upper() == "END":
					self.ast.append({"FOR":[[self.for_var_handler, self.count_], _reAst(self.for_)]}) #Index of the array
					self.for_ = []
					self.for_var_handler = ""
					self.in_for = False
					self.count_ = ""
		return self.ast