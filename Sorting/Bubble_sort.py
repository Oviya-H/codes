def Bubble_sort(arr):
    swap=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                print(arr)
                swap+=1
    print(f'No. of swaps : {swap}');
    return arr

arr=list(map(int,input("Enter the array to be sorted : ").split()))
res=Bubble_sort(arr)
print(f'The sorted array is : {res}')
