def factorial(n):
	f = 1
	for i in range(1,n):
		f*=i
	return f


print(factorial(18))
comb = factorial(18)
comb *= 12*24
print(comb)
print(comb/1024/1024/1024)

ot = "TWHCNENWVAITIXIHSINEEFFOGWIAOSOFESTYSTENIDERTCOAVECOHGHAEUTADIECTHNBDEREDPRPEREITLTRRMTTOOAYRIETTTWHPYEPEGEATTOERAOALDNTOSTALAHPOOSNLHHGICONISMNIH"
print(len(ot))