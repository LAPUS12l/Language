import value_maker
import error
import other.special
import sys
import time
class Evaluator(object):
	def __init__(self):
		self.ast = None
		self.variables = {}
		self.labels = {}
	def run(self, ast):
		self.ast = ast
		try:
			for i in self.ast:
				for l in i:
					if l == "printnew":
						print(value_maker.out_put_natural(str(eval(value_maker.make(i[l], sys.argv[1], self.variables)))))
					elif l == "dimention":
						if type(i[l]) != list:
							error.Error("BaseSystemError", "Syntax Evaluator error expected list. not "+str(type(i[l])), i[l], sys.argv[1])
						self.variables[i[l][0]] = value_maker.make(i[l][1], sys.argv[1], self.variables)
					elif l == "IF":
						if type(i[l]) != list:
							error.Error("BaseSystemError", "Syntax Evaluator error expected list. not "+str(type(i[l])), i[l], sys.argv[1])
						if eval(value_maker.make(i[l][0], sys.argv[1], self.variables)):
							self.rerun(i[l][1])
					elif l == "print":
						print(value_maker.out_put_natural(str(eval(value_maker.make(i[l], sys.argv[1], self.variables)))), end="")
					elif l == "CONVERTINT":
						try:
							self.variables[i[l]] = str(int(eval(self.variables[i[l]])))
						except:
							self.intl = other.special.get_int_array()
							try:
								eval(self.variables[i[l]])
							except:
								error.Error("NameError", "'"+i[l]+"' is not defined", i[l], sys.argv[1])
							for k in eval(self.variables[i[l]]):
								if k not in self.intl:
									error.Error("ConverterError", "Cannot convert to int because of illegal char '"+k+"'", i[l], sys.argv[1])
					elif l == "CONVERTSTR":
						try:
							self.variables[i[l]] = '"'+str(self.variables[i[l]])+'"'
						except:
							error.Error("NameError", "'"+i[l]+"' is not defined", i[l], sys.argv[1])
					elif l == "INPUT":
						self.variables[i[l]] = '"'+input()+'"'
					elif l == "LABEL":
						self.labels[i[l][0]] = i[l][1]
					elif l == 'GOTO':
						try:
							self.rerun(self.labels[i[l]])
						except KeyError:
							error.Error("NameError", "'"+i[l]+"' is not defined", i[l], sys.argv[1])
					elif l == "WHILE":
						while True:
							if eval(value_maker.make(i[l][0], sys.argv[1], self.variables)):
								self.rerun(i[l][1])
							else:break
					elif l == "SLEEP":
						if type(eval(value_maker.make(i[l], sys.argv[1], self.variables))) != int:
							error.Error("TypeError", "Cannot create a int value with str or op", i[l], sys.argv[1])
						time.sleep(eval(value_maker.make(i[l], sys.argv[1], self.variables)))
					elif l == "FOR":
						self.count = eval(value_maker.make(i[l][0][1], sys.argv[1], self.variables))
						if type(self.count) != int:
							error.Error("TypeError", "Cannot be a count because its not an int require integer", i[l][0][1], sys.argv[1])
						self.saved = i[l][1] 
						for k in range(0, self.count):
							
							i[l][1] = [{"dimention":[i[l][0][0], str(k)]}]
							for n in self.saved:
								i[l][1].append(n)
							self.rerun(i[l][1])
					elif l == "DIE":
						exit()
					elif l == "la atom":
						try:
							eval(value_maker.make(i[l], sys.argv[1], self.variables))
						except:
							error.Error("AtomError", "ATOM Value error or '"+i[l].split(" ", 1)[0]+"' is not a keyword", i[l], sys.argv[1])
		except KeyboardInterrupt:
			error.Error("KEYINTERRUPT", "Interrupted ^C", "NONE", sys.argv[1])
	def rerun(self, raw_):
		self.run(raw_)