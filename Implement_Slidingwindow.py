def ImplementSliding_Window(arr,WindowSize):
    arraySize=len(arr)
    if arraySize<=WindowSize:
        return -1
    Window_sum=sum([arr[i] for i in range(WindowSize)])
    Max_sum=Window_sum

    for i in range(arraySize-WindowSize):
        Window_sum=window_sum-arr[i]+arr[i+WindowSize]
        Max_sum=max(window_sum,Max_sum)
    return Max_sum

arr=[90,-10,-90,100]
k=2
answer=ImplementSliding_Window(arr,k)
