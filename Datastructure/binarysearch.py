def BinarySearch(list,key):
    low=0
    high=len(list)-1
    Found=False
    while low<=high and not Found:
        mid=(low+high)//2
        if key==list[mid]:
            Found=True
        elif key>list[mid]:
            low=mid+1
        else:
           high=mid-1
    if Found==True:
        print("key is found at",format(mid+1))
    else:
        print("Key is not found")
num=int(input("enter no of elements:"))
list=[int(input()) for i in range(num)]
list.sort()
print(list)
key=int(input("enter elements:"))
BinarySearch(list,key)
 
