def SecondLargest_Method_1(array):
    array.sort()
    i = -2
    while(i<0):
        if array[-1] == array[i]:
            i-=1
        else:
            return array[i]
        
def SecondLargest_Method_2(array):
    max = array[0]
    for i in array:
        if i > max:
            old = max
            max = i
    return old
    
array = list(map(int,input().strip().split()))
print(SecondLargest_Method_1(array))
print(SecondLargest_Method_2(array))