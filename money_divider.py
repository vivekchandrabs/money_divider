import time
l=[1,2,5,10,20,50,100,200,500,2000]
sum1=eval(input("enter the amount"))
print(time.ctime())
num=[]
t=0
d={}
val=2000
ex=[]
re=0
h=0
q=0

def clc(t):
	while (sum(num)!=sum1):



		max_num=max(l)
			# print(max_num)
		diff=t-max_num
		if diff<0:
				
				
			l.remove(max_num)
		else:

			num.append(max_num)
				#l.remove(max_num)

		if diff in l:
			num.append(diff)
				# print(num)
		else:
			if diff<0:
				pass
			else:
				
				diff=abs(diff)
				# print(diff)
				t=diff





while (sum(num)!=sum1):
	
	
	if (sum1>=2000):
		if sum1%val==0:
			while sum1%val==0:
				f=int(sum1/val)
				
				if val*f==sum1:
					g=int(val/2000)
					
					h=int(g*f)			

				val=int(val*10)
			ex.append(2000)
			ex=ex*h
			
			num.extend(ex)

		else :
			
			while ((sum1-t)%2000!=0):
				
				t=sum1%val
				q=sum1-t
				val=val*10

			val=2000

			while q%val==0:
				
				f=int(q/val)
					
				if val*f==q:
					g=(val/2000)
						
					h=int(g*f)			

				val=(val*10)
			ex.append(2000)
			ex=ex*h
				
			num.extend(ex)
			clc(t)
			

	else:

		clc(sum1)
		


for i in num:
	if i in d:
		d[i]+=1
	else:
		d[i]=1


print(" \n")
print("You have to pay")

for i,j in d.items():
	print("RS ",i  ,"  x  ", j ," NOS" )


print(" \n")
print(time.ctime())
