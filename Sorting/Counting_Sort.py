def Counting_sort(arr):
    mini=int(min(arr))
    maxi=int(max(arr))
    ran=maxi-mini+1
    count=[0]*ran
    output=[0]*len(arr)

    for i in range(len(arr)):
        count[arr[i]-mini]+=1
    print(count)

    for i in range(1,len(count)):
        count[i]+=count[i-1]
    print(count)

    for i in range(len(arr)):
        output[count[arr[i]-mini]-1]=arr[i]
        print(output)
        count[arr[i]-mini]-=1
    return output

arr=list(map(int,input("Enter the array to be sorted : ").split()))
res=Counting_sort(arr)
print(res)
