no=int(input("Enter the number of lists you want "))
i=0
while i<no:
    n=int(input("\nEnter the length of the list you want "))
    print("Enter the list ");
    list=[];                 #list is declared inside the loop since delete is used 
    j=0
    k=0
    while j<n:
        data=int(input())
        j=j+1;
        list.append(data)
    print("Input:list",i+1,list)
    print("Output ",end='')
    while k<n:
        if  list[k]>=0:
            print(list[k],end=' ')
        k=k+1
    del list
    i=i+1
