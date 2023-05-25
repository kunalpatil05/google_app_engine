n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements in the array: ").split()))
min_ind = 0
for i in range(n-1):
    min_ind = i
    for j in range(i+1, n):
        if(arr[j] < arr[min_ind]):
            min_ind = j
    
        arr[i],arr[min_ind] = arr[min_ind], arr[i]
print("Sorted array is:")
print(arr)
