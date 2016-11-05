import cipher 
import tokenizer
import detectEnglish
import cryptomath
import printer

from collections import OrderedDict


MAX_KEY_SIZE=26

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


def createAlphabetDictionary(key):
	""" create dictionaries for easy char to integer handling """
	global keyAlphabet, alphabet, kactoi,kaitoc, actoi, aitoc
	key = key.upper()
	#print(key)
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	keyAlphabet = key+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	#print(keyAlphabet)
	keyAlphabet = "".join(OrderedDict.fromkeys(keyAlphabet))
	#print(keyAlphabet)

	LS = list(enumerate(keyAlphabet))
	lsi = [(item,index) for index,item in LS]
	kactoi = dict(lsi)
	kaitoc = dict(LS)

	LS = list(enumerate(alphabet))
	lsi = [(item,index) for index,item in LS]
	actoi = dict(lsi)
	aitoc = dict(LS)
	#print(alphabet,"\n")
	# print(LS,"\n")
	# print(lsi,"\n")
	# print(ctoi,"\n")  # char to integer, use as ctoi[char]
	# print(itoc,"\n")  # integer to char, use as itoc[integer]

createAlphabetDictionary("MONOKOKOLALA")


class MonoWithKey(cipher.Cipher):

	def __init__(self):
		cipher.Cipher.__init__(self)
		self.lResult=[]
		self.CT=""
		self.OT=""
		self.WORDS = loadDictionary() #  loadSlovnik() +

		

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
		#return self.printResult() # print the one result that is correct 

	def decode(self,sentence,key):
		""" Decode OT to Cipher Text with clas name cipher and given key"""
		translated=''
		createAlphabetDictionary(key)

		for c in sentence:
			i = kactoi[c] 
			translated+=alphabet[i]
		
		return translated

	def encode(self, sentence,key):	
		""" Encode CT to OT with given sentence and key
		sentence has to be upper case, english alphabet and no spaces"""
		
		translated = ''
		createAlphabetDictionary(key)

		for c in sentence:
			i = actoi[c]
			translated+=keyAlphabet[i]
		
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
			# print something sometimes to let me know that you are working and how fast you are working
			if i%1000==0:
				print("Step "+str(i))


			sDecoded=self.decode(sentence, self.WORDS[i])
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
				
				rep = printer.Report( "MONO WITH KEY CIPHER",
										"CT: "+self.CT,
									    "key :"+ r[1],
									    "OT: "+tokenizer.tokenize(r[0]))

				printer.box(rep.getReport())
				return True
		else:
			printer.box([" Mono with key cipher is not solution"])
			return False

	def getKeyParts(self):
		""" get all possible combinations of keys A and B parameters """
		for i in range(0,26*26):
			keyA = i // MAX_KEY_SIZE
			keyB = i % MAX_KEY_SIZE
			self.lKeyParts.append((keyA, keyB))
		



# m = MonoWithKey()
# #ot = "GODWHATWONDERTHATACROSSTHEEARTHAGREATARCHITECTWENTMADANDPOORWILCOXRAVEDWITHFEVERINTHATTELEPATHICINSTANTTHETHINGOFTHEIDOLSTHEGREENSTICKYSPAWNOFTHESTARSHADAWAKEDTOCLAIMHISOWNTHESTARSWERERIGHTAGAINANDWHATANAGEOLDCULTHADFAILEDTODOBYDESIGNABAN"
# #ct = "BKTVDSQVKJTYNQDSQSONKPPQDYYSNQDSBNYSQSNODEQYOQVYJQISTSJTLKKNVEHOKWNSUYTVEQDAYUYNEJQDSQQYHYLSQDEOEJPQSJQQDYQDEJBKAQDYETKHPQDYBNYYJPQEOGXPLSVJKAQDYPQSNPDSTSVSGYTQKOHSEIDEPKVJQDYPQSNPVYNYNEBDQSBSEJSJTVDSQSJSBYKHTORHQDSTASEHYTQKTKCXTYPEBJSCSJTKAEJJKOYJQPSEHKNPDSTTKJYCXSOOETYJQ"
# ot= "CRYMEARIVERANDTHENKILLSOMEINDIANSFORME"
# ct=m.encode(ot,"SCOTTY")
# print(m.encode(ot,"SCOTTY"))

# # s="TKCOY MQFLK FPKLI LKBTO QDTEU PFKTP PLAGU PQBLV TOKJT KQSKR PMFTP QDTSE FIFQY QLPSA TIYTK COYMQ CLJJU KFCSQ FLKPF PVTOY FJMLO QSKQQ LSKYL KTWDL UPTPQ DTFKQ TOKTQ WDTKP LJTEL RYMUO CDSPT PAOLJ SKLKI FKTPQ LOTQD TYUPT SCOTR FQCSO RKUJE TOQDT KUJET OJUPQ ETTKC OYMQT RPLQD SQLKI YQDTP QLOTC SKPTT FQSKR FQCSK KLQET FKQTO CTMQTREYQD FORMS OQFTP QDSQJ FBDQU PTQDT KUJET OWFQD LUQQD TCSOR DLIRT OPMTO JFPPF LK"
# # s = m.prepareString(s)
# # #k=m.WORDS[37108]
# # #x = m.encode(s,k)
# # #print(x)
# print(m.decode(ct,"SCOTTY"))
# # print(m.WORDS[37108])
