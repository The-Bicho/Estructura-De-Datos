def burbuja(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
            if(swapped is False):
                break
        
arr =  [12, 23, 45, 11, 13, 98]
print("Desordenado" + str(arr))
burbuja(arr)
print("Ordenado" + str(arr))