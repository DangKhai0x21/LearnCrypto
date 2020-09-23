import string

list_ = string.ascii_lowercase

if __name__ == '__main__':
	cipher = input("Input cipher text: ")
	cipherToLower = cipher.lower()
	listCipher = list(cipherToLower)
	for i in range(0,26):
		count = 0
		letter = list_[i]
		for m in range(0,len(cipherToLower)):
			if letter == cipherToLower[m]:
				count +=1
		print ("[" + letter + "] :" + str(count))		

