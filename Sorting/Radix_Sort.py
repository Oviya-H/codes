def Radix_sort(arr,exp):
    mini=int(min(arr))
    maxi=int(max(arr))
    ran=maxi-mini+1
    count=[0]*ran
    output=[0]*len(arr)

    for i in range(len(arr)):
        count[(arr[i]%exp)-mini]+=1

    for i in range(1,len(count)):
        count[i]+=count[i-1]

    for i in range(len(arr)):
        output[count[(arr[i]%exp)-mini]-1]=arr[i]
        count[arr[i]-mini]-=1
    return output

arr=list(map(int,input("Enter the array to be sorted : ").split()))

maxi = max(arr)
exp = 10
while maxi != 0:
    out = Radix_sort(arr, exp)
    exp *= 10
    maxi = maxi/10

print(out)
