'''l = [3,1,6,5,2]
print("before sorting",format(l))
l.sort()
print("after sorting",format(l))'''
def getsum(a,b):
	return(a+b)

def getdiff(a,b):
	if isinstance(a,(int,float)):
		return a-b
	else:
		print("pass either int or float")

def getvalues(a, pi=3.141, c=None):
	if c is not None:
		print(c)
		return a+pi+c
	return a+pi

#print("hi")
if __name__=='__main__':
	a=22
	b=11
	#print(getdiff(a,b))
	#print(getsum(a,b))
	print(getvalues(5,4,5))