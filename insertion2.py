def insertarion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while j>= 0 and key< arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key

arr = [12, 23, 11, 30, 27]
print("Desordenado" + str(arr))
insertarion(arr)
print("Ordenado" + str(arr))