num=int(input())
#;fgdafjdklfdf afjklfjsdlj

for i in range(1,num+1):
    if num%i==0:
        temp=i
        count=0
        for j in range(1,i):
            if i%j==0:
                count+=1
        if count==1:
            print(i)
   