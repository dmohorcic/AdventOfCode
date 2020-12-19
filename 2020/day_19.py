import numpy as np

def getRequirements(rules):
	req = dict()
	for key in rules.keys():
		rule = rules[key]
		if "\"" in rule:
			req[key] = set([])
		else:
			args = [int(x) for x in ''.join(rule.split(" |")).split(' ')]
			req[key] = set(args)
	return req

def isSatisfied(test, generated):
	for t in test:
		if t not in generated:
			return False
	return True

def generateDinamicaly(rules, generated):
	req = getRequirements(rules)
	for key, val in req.items():
		if not bool(val):
			generated[key] = [rules[key].split('\"')[1]]
	while 0 not in generated.keys():
		for key, rule in rules.items():
			if isSatisfied(req[key], generated.keys()) and key not in generated.keys():
				gen = list()
				if " | " in rule:
					args_l = [int(x) for x in rule.split(" | ")[0].split(' ')]
					args_r = [int(x) for x in rule.split(" | ")[1].split(' ')]
					if len(args_l) == 1:
						for x in generated[args_l[0]]:
							gen.append(x)
					else:
						ll = generated[args_l[0]]
						lr = generated[args_l[1]]
						for s1 in ll:
							for s2 in lr:
								gen.append(s1+s2)
					if len(args_r) == 1:
						for x in generated[args_r[0]]:
							gen.append(x)
					else:
						rl = generated[args_r[0]]
						rr = generated[args_r[1]]
						for s1 in rl:
							for s2 in rr:
								gen.append(s1+s2)
				else:
					args = [int(x) for x in rule.split(" ")]
					if len(args) == 1:
						for x in generated[args[0]]:
							gen.append(x)
					else:
						l = generated[args[0]]
						r = generated[args[1]]
						for s1 in l:
							for s2 in r:
								gen.append(s1+s2)
				generated[key] = gen

def task1(rules, msgs):
	c = 0
	generated = dict()
	generateDinamicaly(rules, generated)
	possible = generated[0]
	for msg in msgs:
		if msg in possible:
			c += 1
	return c

def task1(rules, msgs):
	rules[8] = "42 | 42 8"
	rules[11] = "11: 42 31 | 42 11 31"

def main():
	rules = dict()
	msgs = list()
	with open("2020/day_19.in", "r") as f:
		read_rules = False
		for l in f:
			if l == '\n':
				read_rules = True
			elif not read_rules:
				args = l.split('\n')[0].split(": ")
				rules[int(args[0])] = args[1]
			else:
				msgs.append(l.split('\n')[0])
	msgs = np.array(msgs)

	res1 = task1(rules, msgs)
	print("Taks 1: %d" % res1)

if __name__ == "__main__":
	main()