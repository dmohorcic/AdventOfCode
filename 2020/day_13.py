import numpy as np
import math

def extendedEuclid(a, b):
	if a == 0:
		return b, 0, 1
	gcd, x_, y_ = extendedEuclid(b%a, a)
	x = y_-(b//a)*x_
	y = x_
	return gcd, x, y

def task1(time, departs):
	best_ID, wait_time = 0, -1
	for d in departs:
		if d == 'x':
			continue
		d = int(d)
		k = time/d
		wait = d*math.ceil(k)-time
		if wait_time == -1 or wait < wait_time:
			wait_time = wait
			best_ID = d
	return wait_time*best_ID

def task2(departs):
	i = 0
	n_i1, n_i = 0, 0
	a_i1, a_i = 0, 0
	while True:
		if departs[i] != 'x':
			if n_i1 == 0:
				n_i1 = int(departs[i])
				a_i1 = n_i1-i
			else:
				n_i = int(departs[i])
				a_i = n_i-i
				i += 1
				break
		i += 1

	gcd, m_i1, m_i = extendedEuclid(n_i1, n_i)
	x = a_i1*m_i*n_i+a_i*m_i1*n_i1

	k = x//(n_i1*n_i)
	x -= (n_i1*n_i)*k	

	n_i1 = n_i*n_i1
	a_i1 = x
	while i < len(departs):
		if departs[i] != 'x':
			n_i = int(departs[i])
			a_i = n_i-i

			gcd, m_i1, m_i = extendedEuclid(n_i1, n_i)
			x = a_i1*m_i*n_i+a_i*m_i1*n_i1

			k = x//(n_i1*n_i)
			x -= (n_i1*n_i)*k

			n_i1 = n_i*n_i1
			a_i1 = x
		i += 1
	return x


def main():
	with open("2020/day_13.in", "r") as f:
		time = int(f.readline()[:-1])
		departs = np.array(f.readline().split('\n')[0].split(','))
	
	res1 = task1(time, departs)
	print("Task 1: %d" % res1)

	res2 = task2(departs)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()