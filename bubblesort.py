import random
import time
arr=[]
for x in xrange(0,100):
	rand = int(random.random()*10000)
	arr.append(rand)
	
print arr
start = time.time()
count = 0
num = 0
for x in xrange(0,len(arr)):
	count+=1
	flag = True
	for i in xrange(0,len(arr)-count):
		if arr[i+1]<arr[i]:
			temp = arr[i]
			arr[i]=arr[i+1]
			arr[i+1]=temp
			num+=1
			flag = False
	if flag == True:
		break
			
print arr
print ("---%s seconds---" % (time.time()-start))