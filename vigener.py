import cipher 
import tokenizer
import detectEnglish
import cryptomath
import printer

from collections import OrderedDict


MAX_KEY_SIZE=26

def shift(l, n):
	""" Shift list to  to right by  n"""
	#n=-n
	return l[n:] + l[:n]



def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = [] #{}
    for word in dictionaryFile.read().split('\n'):
        #englishWords[word] = None
        englishWords.append(word)
    dictionaryFile.close()
    return englishWords



def loadSlovnik():
    dictionaryFile = open('slovnik.txt')
    czechWords = [] #{}
    for word in dictionaryFile.read().split('\n'):
        #englishWords[word] = None
        czechWords.append(word)
    dictionaryFile.close()
    return czechWords


def createVigenerSqrt():	
	global VIGENER_SQRT 
	VIGENER_SQRT = []
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	for i in range(0,len(alphabet)):
		VIGENER_SQRT.append(shift(alphabet,i))


	

def createAlphabetDictionary(key): # key is string, need to do list take list of alpahabets from vigener squeare
	""" create dictionaries for easy char to integer handling """
	global keyAlphabet, alphabet, kactoi,kaitoc, actoi, aitoc
	key = key.upper()
	key = "".join(OrderedDict.fromkeys(key))
	keyAlphabet = []

	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	LS = list(enumerate(alphabet))
	lsi = [(item,index) for index,item in LS]
	actoi = dict(lsi)
	aitoc = dict(LS)

	lsi = []
	for i in range(0,len(key)):
		keyAlphabet.append(VIGENER_SQRT[actoi[key[i]]])
	for i in range(0,len(key)):
		item = key[i]
		index = keyAlphabet[i]
		lsi.append([item,index])

	kactoi = dict(lsi)

	#print(lsi,"\n")
	#print(kactoi,"\n")  # char to integer, use as ctoi[char]

# create dictionary that has chars of key as keys
# create string of periodic key that is as long as message to be coded
# iterate over message to be coded and find proper char in keyAlphabet 

	
# createVigenerSqrt()
# createAlphabetDictionary("MONOKOKOLALA")


class Vigener(cipher.Cipher):

	def __init__(self):
		cipher.Cipher.__init__(self)
		self.lResult=[]
		self.CT=""
		self.OT=""
		self.WORDS = loadSlovnik() + loadDictionary()
		filter(lambda a: a != "", self.WORDS)
		createVigenerSqrt()

		

	def solve(self,sentence):
		"""given sentence, it uses Ceaser cipher with all possible keys to try to solve the puzzle, if it manages to find an English sentence, than it saves it as a possible result to 
		lResult list, then testResult is called and it finds the right sentence and then the result is printed. """
		# reinit all variables 
		self.lResult=[]
		self.CT=""
		self.OT=""
		


		sentence = self.prepareString(sentence); # prepare string in the right format 
		self.CT = sentence # save for letter evaluation in testResult
		self.bruteForce(sentence) # brute force solution, possible candidates are added to lResult
		#result = self.testResult()  # test possible candidate in decode -encode - decode way
		return self.printResult() # print the one result that is correct 

	def createPeriodicKey(self,sentences,key):
		senLen = len(sentences)
		keyLen = len(key)
		mult = int(senLen/keyLen)
		residu = int(senLen%keyLen)
		perKey = mult*key + key[0:residu]
		return perKey




	def decode(self,sentence,key):
		""" CT to OT"""
		translated=''
		createAlphabetDictionary(key)
		if len(key) == 0:
			return ""
		periodicKey = self.createPeriodicKey(sentence,key)

		for i in range(0,len(sentence)):
			#print(kactoi)
			codeAlphabet = kactoi[periodicKey[i]]
			#print(codeAlphabet)
			tmpLS = list(enumerate(codeAlphabet))
			tmplsi = [(item,index) for index,item in tmpLS]
			tmpctoi = dict(tmplsi)
			iOT = tmpctoi[ sentence[i]]     # take from normal alphabet index of char to be coded 
			
			# take char from OT, loook at his index, take indexed char from kactoi alphabet

			translated+=alphabet[iOT]
		
		return translated

	def encode(self, sentence,key):	
		""" OT to CT """
		
		translated=''
		createAlphabetDictionary(key)
		periodicKey = self.createPeriodicKey(sentence,key)

		for i in range(0,len(sentence)):
			#print(kactoi)
			codeAlphabet = kactoi[periodicKey[i]]
			#print(codeAlphabet)
			iOT = actoi[  sentence[i]   ]     # take from normal alphabet index of char to be coded 
			
			# take char from OT, loook at his index, take indexed char from kactoi alphabet

			translated+=codeAlphabet[iOT]
		
		return translated

	def testResult(self):
		""" take given ST, encode it, if it is english text, decode it and check if it is the same as given ST """
		for i in range(0,len(self.lResult)):
			sDecoded = self.lResult[i][0]
			key = self.lResult[i][1] 
			
			if self.encode(sDecoded,key) != self.CT:  # if decode - encode - decode does not match, there  is a problem in implementation ! 
				raise NotImplementedError("Subclass must implement abstract method")
	def addToResult(self,sentence,key):
		""" if eng sentence is detected, add it as possible result sentence, more sentence can be detected as english sentences, it has to be tested """
		result= [sentence,key];
		self.lResult.append(result)

	def bruteForce(self, sentence):
		""" Brute force attack on Ceaser cipher with any key. decode given sentence, tokenize it and if it is accessed as English sentence, then add it to candidate list """
		lRet=[]
		for i in range(0,len(self.WORDS)):

			if i%1000==0:
				print("Step "+str(i))

			sDecoded = self.decode(sentence, self.WORDS[i])
			#print(i)
			if not len(sDecoded) == 0:
				lRet.append([sDecoded, self.WORDS[i]])
				sTokenized = tokenizer.tokenize(sDecoded)
				if detectEnglish.isEnglish(sTokenized):
					#self.addToResult(sDecoded,self.WORDS[i])  # to result I add sentence without whitespaces, tokenize it after the result is tested 
					self.printResult([sDecoded,self.WORDS[i]])
		return lRet
				
	
	def printResult(self,result):
		""" go over all possible results and if there is none, state that this cipher is not the solution"""
		
		#if not (self.lResult == []):  # check if there is result
		if not (result == []):  # check if there is result
			#for i in range(0, len(self.lResult)):
				r = result #self.lResult[i]
				
				rep = printer.Report( "Vigener KEY CIPHER",
										"CT: "+self.CT,
									    "key :"+ r[1],
									    "OT: "+tokenizer.tokenize(r[0]))

				printer.box(rep.getReport())
				return True
		else:
			printer.box([" Vigener cipher is not solution"])
			return False

	def getKeyParts(self):
		""" get all possible combinations of keys A and B parameters """
		for i in range(0,26*26):
			keyA = i // MAX_KEY_SIZE
			keyB = i % MAX_KEY_SIZE
			self.lKeyParts.append((keyA, keyB))
		



# m = Vigener()
# key = "MATKAPLUKU"
# createAlphabetDictionary(key)
# print(kactoi)

# ot ="ATTACKATDAWNANDBRING ME ALL THEIR WOMEN AND MAN AND KIDS AND FUCK THEM THEIR ARSES AND DO IT HARD AND QUICKLY AND DIRTY AND I HAVE A HARD TIME LALA%%%44"
# periodicKey = m.createPeriodicKey(ot,key)
# print(periodicKey)




# # m.createPeriodicKey(ct,key);
# # # s="TKCOY MQFLK FPKLI LKBTO QDTEU PFKTP PLAGU PQBLV TOKJT KQSKR PMFTP QDTSE FIFQY QLPSA TIYTK COYMQ CLJJU KFCSQ FLKPF PVTOY FJMLO QSKQQ LSKYL KTWDL UPTPQ DTFKQ TOKTQ WDTKP LJTEL RYMUO CDSPT PAOLJ SKLKI FKTPQ LOTQD TYUPT SCOTR FQCSO RKUJE TOQDT KUJET OJUPQ ETTKC OYMQT RPLQD SQLKI YQDTP QLOTC SKPTT FQSKR FQCSK KLQET FKQTO CTMQTREYQD FORMS OQFTP QDSQJ FBDQU PTQDT KUJET OWFQD LUQQD TCSOR DLIRT OPMTO JFPPF LK"
# ot = m.prepareString(ot)
# # # #k=m.WORDS[37108]
# ct = m.encode(ot,key)
# print(ct)
# x = m.decode(ct,key)
# print(x)
# # print(m.encode(ot,key))
# # # print(m.WORDS[37108])



