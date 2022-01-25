def programmerStrings(s):
    
    temp = list(s)
    stack = []
    print(temp)

    stack1 = ['p','r','o','g','r','a','m','m','e','r']
    stack2 = ['p','r','o','g','r','a','m','m','e','r']
    
    

    for i in range(len(temp)):
        if temp[i] in stack1:
            stack1.remove(temp[i])
            
            if len(stack1) == 0:
                index = i
    temp.sort()
    for i in range(len(temp)):
        if temp[i] in stack2:
            stack2.remove(temp[i])
            
            if len(stack1) == 0:
                index2 = i

    print(len(temp)-index2 - index)
    return len(temp)-index2 - index

programmerStrings("xprogxrammerrxproxgrammer")