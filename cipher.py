import printer

MAX_KEY_SIZE=26
 
def createAlphabetDictionary():
	""" create dictionaries for easy char to integer handling """
	global alphabet, LS,lsi,ctoi,itoc
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	LS = list(enumerate(alphabet))
	lsi = [(item,index) for index,item in LS]
	ctoi = dict(lsi)
	itoc = dict(LS)
	#print(alphabet,"\n")
	#print(LS,"\n")
	#print(lsi,"\n")
	#print(ctoi,"\n")  # char to integer, use as ctoi[char]
	#print(itoc,"\n")  # integer to char, use as itoc[integer]



class Cipher:
	def __init__(self):
		createAlphabetDictionary()
	def solve(self,sentence):
		raise NotImplementedError("Subclass must implement abstract method")
	def decode(self,sentence):
		raise NotImplementedError("Subclass must implement abstract method")
	def encode(self, sentence):
		raise NotImplementedError("Subclass must implement abstract method")
	def addToResult(self,sentence):
		raise NotImplementedError("Subclass must implement abstract method")
	def bruteForce(self, sentence):
		raise NotImplementedError("Subclass must implement abstract method")
	def testResult(self):
		raise NotImplementedError("Subclass must implement abstract method")
	def printResult(self):
		raise NotImplementedError("Subclass must implement abstract method")

	def prepareString(self,sentence):
		""" Erase spaces, make upper case and delete not alphabetical character"""
		#print("Preparing string for decode/encode: ",sentence)
		tmp = sentence.replace(" ", "")
		tmp = tmp.upper()
		tmp = self.deleteSpecialCharacters(tmp)
		#print("Prepared string for decode/encode: ",tmp)
		return tmp

	def deleteSpecialCharacters(self,sentence):
		""" checks if there are only characters from eng alphabet in sentence, if there 
		is a differencet character, delete it"""
		l_not_char=[]
		for i in range(0,len(sentence)):
			
			if sentence[i] not in alphabet:
				l_not_char.append(sentence[i])

		for i in range(0,len(l_not_char)):
			if l_not_char[i] in sentence:
				sentence = sentence.replace(l_not_char[i],"")

		return sentence
