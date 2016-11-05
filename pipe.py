#import super class 
import cipher
# import all cipher classses
import ceaser
import affine

# import printer for box printing
import printer
import cipher
import ceaser
import affine



""" creates pipe beetween two ciphers, first cipher return all bruteforced texts and then second cipher decodes it to english"""
class Pipe(cipher.Cipher):
	def __init__(self,cipher1,cipher2):
		cipher.Cipher.__init__(self)
		self.cipher1=cipher1
		self.cipher2=cipher2
		self.lResult=[]
		self.CT=""
		self.OT=""
		
	def solve(self,sentence):
		printer.box(["SOLVING IN PIPE","Cipher 1: "+type(self.cipher1).__name__,"Cipher 2: "+type(self.cipher2).__name__,"CT: "+sentence])
		self.lResult=[]
		self.CT=""
		self.OT=""


		## TODO: there is to much printing, print only for true, wait for second cipher to return true and then print first cipher information to make complete picture 

		sentence = self.prepareString(sentence); # prepare string in the right format 
		self.CT = sentence # save for letter evaluation in testResult
		lRet = self.cipher1.bruteForce(sentence)
		#print(lRet)
		#print(len(lRet[0][0]))
		allOutputs = []
		for i  in range(0,len(lRet)):
			printer.box(["Cipher 1: "+type(self.cipher1).__name__,"Key: "+str(lRet[i][1]), "OT :"+str(lRet[i][0])])
			#self.cipher1.printResult(lRet[i])
			allOutputs.append(   self.cipher2.bruteForce(lRet[i][0]))
			for s in allOutputs[-1]:
				printer.box(["Cipher 2: "+type(self.cipher2).__name__,"Key: "+str(s[1]) , "CT :"+str(s[0])])
			# if self.cipher2.solve(lRet[i][0]) == True:
			# 	printer.box(["Cipher 1: "])
			# 	self.cipher1.printResult(lRet[i])
			# 	print("\n\n")
		print("num of tables in the first cipher :"+str(len(allOutputs)))
		for i in range(0,len(allOutputs)):
			for j in range(0,len(allOutputs[i])):
				print(str(allOutputs[i][j][0])  )  #+"  "+str(allOutputs[i][j][1][0]))
		


		

