def arraysIntersection(arr1,arr2,arr3):
    res = []
    if arr1 == None or arr2 == None or arr3 == None:
        return res
    i,j,k =0,0,0
    while(i<len(arr1) and j<len(arr2) and k<len(arr3)):
        if arr1[i]==arr2[j]==arr3[k]:
            res.append(arr1[i])
            i+=1
            j+=1
            k+=1
        elif arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr3[k]:
            j+=1
        else:
            k+=1
    return res

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

res = arraysIntersection(arr1,arr2,arr3)
print(res)