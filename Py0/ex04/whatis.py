import sys

def check_parity(val: str):

	try:
		nb = int(val)
	except ValueError:
		print("AssertionError: argument is not an integer")
		return

	if nb % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")
	pass

if __name__ == "__main__":

	if len(sys.argv) > 2:
		print("AssertionError: more than one argument is provided")
	elif len(sys.argv) == 2:
			check_parity(sys.argv[1])
	pass