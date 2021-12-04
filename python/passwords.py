import re 

def password_validate(password):
	if not re.search("[a-z]", password):
		return False 
	if not re.search("[A-Z]", password):
		return False 
	if not re.search("[0-9]", password):
		return False 
	if not re.search("[!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~-]",password):
		return False 
	if len(password) < 6:
		return False 
	if len(password) > 16:
		return False

	return True

if __name__ == '__main__':
	password = input()

	if password_validate(password):
		print("Password accepted!!")
	else:
		print("Password invalid!!")