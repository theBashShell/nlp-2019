
# coding: utf-8

# In[9]:


def min_edit_distance(source, target):
    n = len(source)
    m = len(target)
    
    first = [0] * (m + 1)
    second = [0] * (m + 1)
    
    for i in range(len(first)):
        first[i] = i
    
    for i in range(n):
        second[0] = i + 1
        
        for j in range(m):
            cos = 0 if source[i] == target[j] else 1
            second[j +1] = min(second[j] + 1, first[j + 1] + 1, first[j] + cos)
            
        for j in range(len(first)):
            first[j] = second[j]
            
    return second[m]   

