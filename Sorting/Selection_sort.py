def Selection_sort(num):

    for i in range(len(num)-1):
        j=num.index(min(num[i + 1:len(num)]))
        if num[i]>min(num[i+1:len(num)]):
            num[i],num[j]=num[j],num[i]
            print(num)

    return num
arr=list(map(int,input("Enter the array to be sorted : ").split()))
res=Selection_sort(arr)
print(f'The sorted array is : {res}')
