import os
import sys

listDic = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
special_char =  " [@_!#$%^&*()<>?/|}{~:].,\""

def encrypt_func(key,text):
	cipher_text = ""
	for z in list(text):
		Flag = False
		if z.isupper() == True:
			Flag = True	
		if z in special_char:
			cipher_text += z
			continue
		if (unicode(z,'utf-8')).isnumeric() == True:
			cipher_text += z
			continue
		z = z.lower()				
		max_ = listDic[z] + key
		if max_ > 25:
			min_ = max_ - 26
			cipher_text += check_Upper(Flag,listDic.keys()[listDic.values().index(min_)])
		else:
			z = z.lower()	
			cipher_text += check_Upper(Flag,listDic.keys()[listDic.values().index(max_)])
	return cipher_text

def decrypt_func(key,cipher_text):
	text = ""
	for z in list(cipher_text):
		Flag = False
		if z.isupper() == True:
			Flag = True
		if (unicode(z,'utf-8')).isnumeric() == True:
			text += z
			continue		
		if z in special_char:
			text += z
			continue
		z = z.lower()	
		min_ = listDic[z] - key
		if min_ < 0:
			max_ = 26 + min_ 
			text += check_Upper(Flag,listDic.keys()[listDic.values().index(max_)])
		else:
			text += check_Upper(Flag,listDic.keys()[listDic.values().index(min_)])	
	return text

def check_Upper(Flag,digit):
	if Flag == True:
		return digit.upper()
	else:
		return digit

def menu():
	print "============================="
	print "				oOo MENU oOo"
	print "1. Encrypt Messenge"
	print "2. Decrypt Cipher text"
	print "3. Exit"
	print "============================="

if __name__ == '__main__':
	while True:
		menu()
		choose = raw_input("You choose: ")
		if int(choose) == 1:
			text = raw_input("Input message:")
			key = raw_input("Input key:")
			print "[+] Cipher text is: " + encrypt_func(int(key),text)
		if int(choose) == 2:	
			cipher_text = raw_input("Input Cipher text:")
			key = raw_input("Input key:")
			print "[+] Message is: " + decrypt_func(int(key),cipher_text)
		if int(choose) == 3:
			sys.exit()
