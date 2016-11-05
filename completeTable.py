import cipher 
import tokenizer
import detectEnglish
import cryptomath
import printer
from functools import reduce
from math import sqrt
import itertools

MAX_KEY_SIZE=26

class CompleteTable(cipher.Cipher):

	def __init__(self):
		cipher.Cipher.__init__(self)
		self.lResult=[]
		self.CT=""
		self.OT=""
		self.rFlag=False
		


	def solve(self,sentence,):
		### !!! ORDER cannot be easily bruteforced, in current implementation I run out of memory pretty quickly 

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


		#result = self.testResult()  # test possible candidate in decode -encode - decode way
		#return self.printResult() # print the one result that is correct 

	def decode(self,sentence,key, way, order=[]):
		# key is size of table [m n ]
		# way of writing to table  
			# column - write to columns, read lines
			# line - write to lines, read column
		# order of reading from 
			# if given, read in that order, there is x! where x is num of lines or columns 

		""" CT to OT"""
		m, n = key[0],key[1] # m - rows, n - columns 
		translated=''
		table = []
		# check if there is no password, that means order is set to blank list
		if not order == []:
			if way=="column":
				if not len(order) == m:
					raise NotImplementedError("order length is different than number of columns") 
			else:
				if not len(order) == n:
					raise NotImplementedError("order length is different than number of rows") 

		# write to table 
		# in given or normal order 
		if order == []:
			if way == "column":
				order = list(range(0,m))
			else:
				order = list(range(0,n))
		#print(order)

		# write to table according to  order 
		if way == "column":
			for i in range(0,m):
					#translated += table[j][ order[i] ]
					table.append(sentence[order[i]*n : order[i]*n+n])
		else:
			for i in range(0,n):
				
					#translated += table[j][order[i]]
					table.append(sentence[order[i]*m : order[i]*m+m])

		#print(table)

		# read in another negative way 
		if way == "column":
			for i in range(0,n):
				for j in range(0,m):
					translated += table[j][ i ]
		else:
			for i in range(0,m):
				for j in range(0,n):
					translated += table[j][i]



		## TODO : IMPLEMENT DECODE 
		
		return translated

	def encode(self,sentence,key, way, order=[]):	
		""" OT to CT """
		
		m, n = key[0],key[1] # m - rows, n - columns 
		translated=''
		table = []
		# check if there is no password, that means order is set to blank list
		if not order == []:
			if way=="column":
				if not len(order) == m:
					raise NotImplementedError("order length is different than number of columns") 
			else:
				if not len(order) == n:
					raise NotImplementedError("order length is different than number of rows") 

		# write to table 
		# write in given way, than read in another way in given or normal order
		if way == "column":
			for i in range(0,n):
				table.append(sentence[i*m : i*m+m])
				
		else:
			for i in range(0,m):
				table.append(sentence[i*n : i*n+n])


		# rebuild sentence in given or normal order 
		if order == []:
			if way == "column":
				order = list(range(0,m))
			else:
				order = list(range(0,n))
		#print(order)
		#print(table)

		# read in given order in negative way than given to function
		if way == "column":
			for i in range(0,m):
				for j in range(0,n):
					translated += table[j][ order[i] ]
		else:
			for i in range(0,n):
				for j in range(0,m):
					translated += table[j][order[i]]

		
		#print(translated)


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



	def bruteForce(self, sentence, order=False):
		""" Brute force attack on Ceaser cipher with any key. decode given sentence, tokenize it and if it is accessed as English sentence, then add it to candidate list """

		## TODO : IMPLEMENT BRUTE FORCE 
		# all key m n pairs, both way
		# possibly all orders, brute force should have more parameters in order to know what to use 
		lRet=[]
		tables = self.getTables(sentence)
		l=lWay = ["column"]#,"line"]


		for i in range(0,len(tables)): # over all tables
			# no order implementation for now 
			for way in lWay: # over two ways of writing to table
				
				if way == "column":
					lOrder = [list(range(0,tables[i][0]))]
				else:
					lOrder = [list(range(0,tables[i][1]))]
				#print(i)
				#print(lOrder)
				for o in lOrder:
					sDecoded = self.decode(sentence, tables[i],way,o)
					if not len(sDecoded) == 0:
						lRet.append([sDecoded, [tables[i], way, o]])
						#print(sDecoded,tables[i], way,"\n")
						sTokenized = tokenizer.tokenize(sDecoded)
						#print(sTokenized)
						if detectEnglish.isEnglish(sTokenized):
							print(sTokenized)
							self.printResult([sDecoded,[tables[i], way, o]])  # to result I add sentence without whitespaces, tokenize it after the result is tested 
		return lRet
				
	
	def printResult(self,result):
		""" go over all possible results and if there is none, state that this cipher is not the solution"""
		
		if not (result == []):  # check if there is result
			
				r = result
				
				rep = printer.Report( "COMPLETE TABLE CIPHER",
										"CT: "+self.CT,
									    ("key : M = "+str(r[1][0][0])+" |  N = "+str(r[1][0][1]) + " | Way of encoding = "+r[1][1] + " | Password is : "+str(r[1][2])),
									    "OT: "+tokenizer.tokenize(r[0]))

				printer.box(rep.getReport())	
				self.rFlag=True
		else:
			# TODO : this is never called 
			printer.box([" Complete table cipher is not solution"])
			return False


	def getTables(self, sentence):
		""" Return all possible tables for lenght of sentece """
		n = len(sentence)
		step = 2 if n%2 else 1
		factors = list(reduce(list.__add__,([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
		tables = []
		for i in range(0,len(factors)):
			for j in range(0,len(factors)):
				match = factors[i] * factors[j]
				if match == n:
					if factors[i] > 2 and factors[j] > 2:
						tables.append([factors[i], factors[j] ])
		#print(tables)
		return tables

	def getAllOrders(self,key,way):
		m , n = key[0], key[1]
		#print(m,n)
		if way is "column":
			l = list(range(0,m))
		else:
			l = list(range(0,n))
		return list(itertools.permutations(l))




# c = CompleteTable()

# # #print(c.getAllOrders([5,6],"line"))
# # ct = "HDKEIDOABSTLCRAILMEYGHKSWBGTICEFLOTPUTHOEOPTYUNTWIAEOEWASINOAVARTESWAUPHPSTHHNBTUSINATORNEFIHRTANNESLTREIHYHLCTDCYNTTRTLISINDDDIAHASLISEDRHFCICHSTESSOLDSIMNCAPISSSWBEFRUSEEAHRTMNLPLDOLEVPNTBOOYARERSMVIETOIEBRAONOSEEKWLRRNMINSUOILSHRNAEAYLONHBDIIAELOIGZENRGEPEMIRLNACLEEEBNTCLDWNHY"
# #ct = "ASTONRENPMITSEKDVENESDGAVGRAEIKOAEERICYEITIAOTVVARCSLISUSLMIENTIEESGCIYSMRTFPNWDEOBSSAEGTKSIEOLGIICNUBENPNRSITMREMNMTASASITEESNYPEMOGPISISSZADASFMRSENMROSNEMANTTSOAOTNIAONEEDETCOASRNVATTIVOTSUNIEENSMAIBIONIFSSPTOLFDSAGDLNRTNITOOANEFMSTEEIGIAGNOBNNSVEASIMSSONITFAJADRECNSOEAHPGNHOCERTILTASNNMIERIERHCIHSSIGS"

# ct = "WTEOIOAOASTMNYITIOAOSAMTILYESPPAPTTNHERRNRTNKOHESWCHNRTNTNIETWSEARRTREIHAVFMFMITEREABHHEFMIIRSTDAANDPOIEOCOH"
# print(len(ct))
# # # ot = "LOVE IN"
# # # ot = c.prepareString(ot)
# # # print(ot)
# # # print(c.getTables(ot))
# # # print(len(ot))
# # # ct = c.encode(ot,[2,3],"column",[1,0])
# # # print(ct)
# c.solve(ct)

	

