import cipher 
import tokenizer
import detectEnglish
import cryptomath
import printer

MAX_KEY_SIZE=26

class Affine(cipher.Cipher):

	def __init__(self):
		cipher.Cipher.__init__(self)
		self.lResult=[]
		self.CT=""
		self.OT=""
		self.lKeyParts=[]


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
		""" CT to OT """
		keyA, keyB = key[0],key[1]
		translated=''
		modInverseOfKeyA = cryptomath.findModInverse(keyA, MAX_KEY_SIZE)

		if not modInverseOfKeyA is None:
			#print("inverse ok")
			for c in sentence:
				i = (cipher.ctoi[c] - keyB) * modInverseOfKeyA %MAX_KEY_SIZE
				translated+=cipher.itoc[i]
		#print(translated)
		return translated

	def encode(self, sentence,key):	
		"""OT to CT """
		keyA, keyB = key[0],key[1]
		translated = ''

		for c in sentence:
			i = (cipher.ctoi[c]* keyA + keyB) % MAX_KEY_SIZE
			translated+=cipher.itoc[i]
		
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
		self.lKeyParts=[]
		self.getKeyParts()
		#print("Brute force for win",len(self.lKeyParts))
		for i in range(0,len(self.lKeyParts)):
			#print(i)
			sDecoded = self.decode(sentence, self.lKeyParts[i])
			
			if not len(sDecoded) == 0:
				lRet.append([sDecoded, self.lKeyParts[i]])
				#print("appending")
				sTokenized = tokenizer.tokenize(sDecoded)
				#print(sTokenized)
				if detectEnglish.isEnglish(sTokenized):
					#print(sDecoded)
					self.printResult([sDecoded,self.lKeyParts[i]])  # to result I add sentence without whitespaces, tokenize it after the result is tested 
		return lRet
				
	
	def printResult(self,result):
		""" go over all possible results and if there is none, state that this cipher is not the solution"""
		#print("have result ")
		if not (result == []):  # check if there is result
		#	for i in range(0, len(self.lResult)):
				r = result
				
				rep = printer.Report( "AFFINE CIPHER",
										"CT: "+self.CT,
									    ("key : A = "+str(r[1][0])+"  B = "+str(r[1][1])),
									    "OT: "+tokenizer.tokenize(r[0]))

				printer.box(rep.getReport())	
				return True	
		else:
			printer.box([" Affine cipher is not solution"])
			# TODO : if there is no global call in solve to print result, cipher wont tell that is is not solution  
			return False


	def getKeyParts(self):
		""" get all possible combinations of keys A and B parameters """
		for i in range(0,26*26):
			keyA = i // MAX_KEY_SIZE
			keyB = i % MAX_KEY_SIZE
			self.lKeyParts.append((keyA, keyB))
		



c = Affine()
ot="EVERYONELISTENEDANDEVERYONEWASLISTENINGSTILLWHENITLUMBEREDSLOBBERINGLYINTOSIGHTANDGROPINGLYSQUEEZEDITSGELATINOUSGREENIMMENSITYTHROUGHTHEBLACKDOORWAYINTOTHETAINTEDOUTSIDEAIROFTHATPOISONCITYOFMADNESS"
print(c.encode(ot,[7,7]))
# #print(c.getAllOrders([5,6],"line"))


# ot = "LOVE IN THE TIME OF CHOLERA WAS REALLY A HARD HARD THING AND A LOT OF PEOPLE DIED BECAUSE OF THAT AND THAT IS SAD "
# ot = c.prepareString(ot)
# print(ot)

# print(len(ot))
# ct = c.encode(ot,[2,3])
# print(ct)
# #c.solve(ct)
# ct = "YJWTBUJGLDKJUJCHUCJYJWTBUJFHDGLDKJULUXDKLGGFEJULKGRNOJWJCDGBOOJWLUXGTLUKBDLXEKHUCXWBILUXGTDPRJJAJCLKDXJGHKLUBRDXWJJULNNJUDLKTKEWBRXEKEJOGHVZCBBWF"
# c.solve(ct)
# #print(c.decode(ct,[2,3]))