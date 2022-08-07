def finder(arr1,arr2):
    # Sorting the arrays in ascending order
    arr1.sort()
    arr2.sort()


    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            print(num1)

    return arr1[-1]

# def finder(arr1,arr2):

#     sum1=sum(arr1)
#     sum2=sum(arr2)

#     difference=sum1-sum2
#     return difference

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(finder(arr1,arr2))           
