

def CountingSort(Input):
    k = len(Input)
    max1 = max(Input)
    count = [0]*(max1+1)
    output = [0]*k
    
    for i in range(len(Input)):
        count[Input[i]] += 1
        
    for i in range(1, len(count)):
        count[i] += count[i-1]
        
    for i in range(len(Input)-1, -1, -1):
        output[count[Input[i]] - 1] = Input[i]
        count[Input[i]] -= 1
        
    return output


def RadixSort(arr):
 
    a = CountingSort(arr)
    
    return a


def bucketSort(arr, n):
    maximum = max(arr)
    minimum = min(arr)
  
    rnge = (maximum - minimum) / n
  
    bucket = []
  
    for i in range(n):
        bucket.append([])
  
    for i in range(len(arr)):
        diff = (arr[i] - minimum) / rnge - int((arr[i] - minimum) / rnge)
  
        if(diff == 0 and arr[i] != minimum):
            bucket[int((arr[i] - minimum) / rnge) - 1].append(arr[i])
  
        else:
            bucket[int((arr[i] - minimum) / rnge)].append(arr[i])
  
    for i in range(len(bucket)):
        if len(bucket[i]) != 0:
            bucket[i].sort()
  
    k = 0
    for i in bucket:
        for j in i:
            arr[k] = j
            k += 1


def main():
    arr1 = [1,3,0,7,8,7,3,5,2,1,7]
    arr2 = [110, 45, 65,50, 90, 602, 24, 2, 66]
    arr3 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print("Counting Sort: " , CountingSort(arr1))
    print("Radix Sort: " , RadixSort(arr2))
    bucketSort(arr3, len(arr3))
    print("Bucket Sort: " , arr3)

if __name__ == "__main__":
    main()