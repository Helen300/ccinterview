def insertionSort1(n, arr):
    # value that we want to switch
    if n == 0: 
        return 
    curr = n-1
    insert_e = arr[curr]
    test_pass = False
    while insert_e < arr[curr-1] and curr > 0:
        modArr(arr, curr, test_pass, insert_e)
        curr -= 1
    print("arr currently after finding correct location")
    test_pass = True
    modArr(arr, curr, test_pass, insert_e)
    
def modArr(arr, curr, test_pass, insert_e):
    if not test_pass: 
        arr[curr] = arr[curr-1]
    else:
        arr[curr] = insert_e
    print(' '.join(str(x) for x in arr))
    
if __name__ == '__main__':
    n = 10

    arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

    insertionSort1(n, arr)
