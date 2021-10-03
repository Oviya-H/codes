def Insertion_Sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        temp = None
        for j in range(i-1, -1, -1):
            if key < arr[j]:
                arr[j+1] = arr[j]
                temp = j
            else:
                break
        if temp is not None:
            arr[temp] = key
    return arr

arr=list(map(int,input("Enter the array to be sorted : ").split()))
print(arr)
res=Insertion_Sort(arr)
print("The sorted array is : " , res)
