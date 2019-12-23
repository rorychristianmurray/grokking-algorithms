## box pseudo code
# def look_for_key(box):
# 	for item in box:
# 		if item.is_a_box():
# 			look_for_key(item)
# 		elif item.is_a_key():
# 			print "found the key!"

## every recursive function has two parts
## the base case and the recursive case

def countdown(top_num):
	print(top_num)
	if top_num <= 0:
		return # base case -- return out 
	else :
		countdown(top_num - 1) # recursive case



# t1 = countdown(10)

# t1

def greet(name):
	print(f"hello, {name}!")
	greet2(name)
	print(f"getting ready to say goodbye")
	goodbye()

def greet2(name):
	print(f"how are you, {name}?")

def goodbye():
	print("goodbye")

def factorial(number):
	if number == 1: # base case
		return 1
	else:
		return number * factorial(number - 1)


