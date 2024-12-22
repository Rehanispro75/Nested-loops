input = 2
end = 10000
for num in range(input,end+1,1 ):

    flag = True 
    for i in range(2, num, 1):
        if( num%i==0):
            flag=False
            break
    if(flag):
        print(num , end=" , ")

