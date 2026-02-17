#Write a python program to implement binary search with recursion.
def binSearch(arr,ele,m,n):
    if m>n:
        return -1
    idx=(m+n)//2
    if arr[idx]==ele:
        return idx
    if ele<arr[idx]:
        idx=binSearch(arr,ele,m,idx-1)
    else:
        idx=binSearch(arr,ele,idx+1,n)
    return idx

arr=[1,2,3,4,5]
ele=int(input("Enter the num: "))
print(f"{ele} found in index {binSearch(arr,ele,0,len(arr)-1)}")