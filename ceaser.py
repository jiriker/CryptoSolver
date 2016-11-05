import cipher 
import tokenizer
import detectEnglish
import printer

MAX_KEY_SIZE=26



class Ceaser(cipher.Cipher):

	def __init__(self):
		cipher.Cipher.__init__(self)
		self.lResult=[]
		self.CT=""
		self.OT=""
		self.rFlag=False


	def solve(self,sentence):
		"""given sentence, it uses Ceaser cipher with all possible keys to try to solve the puzzle, if it manages to find an English sentence, than it saves it as a possible result to 
		lResult list, then testResult is called and it finds the right sentence and then the result is printed. """
		# reinit all variables 
		self.rFlag=False
		self.lResult=[]
		self.CT=""
		self.OT=""


		sentence = self.prepareString(sentence); # prepare string in the right format 
		self.CT = sentence # save for letter evaluation in testResult
		self.bruteForce(sentence) # brute force solution, possible candidates are added to lResult


		return self.rFlag
		#self.testResult()  # test possible candidate in decode -encode - decode way
		#return self.printResult() # print the one result that is correct 

	def decode(self,sentence,key):
		""" Decode OT to Cipher Text with ceaser cipher and given key"""
		translated=''
		key = -key

		for c in sentence:
			i = (cipher.ctoi[c] + key)%MAX_KEY_SIZE
			translated+=cipher.itoc[i]
		
		return translated

	def encode(self, sentence,key):	
		""" Encode CT to OT with given sentence and key
		sentence has to be upper case, english alphabet and no spaces"""
		translated=''

		for c in sentence:
			i = (cipher.ctoi[c] + key)%MAX_KEY_SIZE
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
		""" Brute force attack on Ceaser cipher with any key. decode given sentence, tokenize it and if it is accessed as English sentence, then add it to candidate list 
		TODO: impleemtn candidate list"""
		# store all possible for piping
		lRet=[]

		for i in range(0,MAX_KEY_SIZE):
			sDecoded = self.decode(sentence,i)
			lRet.append([sDecoded,i])  # apppend decoded sentence to list 
			sTokenized = tokenizer.tokenize(sDecoded)
			if detectEnglish.isEnglish(sTokenized):
				self.printResult([sDecoded,i])  # to result I add sentence without whitespaces, tokenize it after the result is tested 
		return lRet
	
	def printResult(self,result):
		
		if not (result == []):  # check if there is result	
				r = result
				
				rep = printer.Report( "CEASER CIPHER",
										"CT: "+self.CT,
									    ("key : A = "+str(r[1])),
									    "OT: "+tokenizer.tokenize(r[0]))

				printer.box(rep.getReport())
				self.rFlag = True	
				return True	
		else:
			printer.box([" Ceaser cipher is not solution"])
			return False


# c = Ceaser()
# ot="ONECOULDNOTBESURETHATTHESEAANDTHEGROUNDWEREHORIZONTALHENCETHERELATIVEPOSITIONOFEVERYTHINGELSESEEMEDPHANTASMALLYVARIABLE"
# print(c.encode(ot,12))
