
def binary_search(lst,target):
    start=0
    middle=0
    end=len(lst)
    steps=0
    lst.sort()
    while start<=end:
        print("step:", steps, "list",lst[start:end+1])
        steps=steps+1
        middle=(start+end)//2
        if middle==target:
            return middle
                    
        if middle>target:
            end=middle-1
        
        else:
            start=middle+1
            
    return -1
        
lst=[1,2,3,4,5,6,7,8,9,10]
target=8
a=binary_search(lst,target)



