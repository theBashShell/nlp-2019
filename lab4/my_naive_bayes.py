
# coding: utf-8

# In[64]:


import math

def open_file(data):
    return open(data, 'r')
    

def count_doc(data):
    a = 0
    file = open_file(data)
    for lines in file:
        a += 1
    return a
    

def count_cat(data, cat): 
    a = 0
    file = open_file(data)
    for line in file:
        label = line[-2]
        line = line[:-2].strip('\n\t').split(" ")
        if(label == cat):
            a += 1
    return a
        

def get_vocab(data):
    line1 = []
    file = open_file(data)
    for line in file: 
        line1. extend(line[:-2].strip('\n\t').split(" "))
    return set(line1)    
    
    
def get_bigdoc(data):
    positive = []
    negative = []
    file = open_file(data)
    for line in file:
        label = line[-2]
        line = line[:-2].strip('\n\t').split(" ")
        if(label == '0'):
            negative.extend(line) 
        else:
            positive.extend(line)
    return (negative, positive)
            
        
    
def get_count_count(bigdoc, cat, w):   
    return bigdoc.count(w)
        

def get_vcc(V, bigdoc):
    a = 0
    for w in V:
        a += bigdoc.count(w)
    return a
        


def trainer(data, cat=['0', '1']):
    loglikelihood = {}
    logprior = {}
    for i in cat:
        ndoc = count_doc(data) 
        nc = count_cat(data, i)
        logprior[i] = math.log10(nc/ndoc) 
        V = list(get_vocab(data));
        bigdoc = get_bigdoc(data)[int(i)]
        cc = 0
        vcc = get_vcc(V, bigdoc);
                
        for w in V:
            cc = get_count_count(bigdoc, i, w)       
            calc = (cc + 1) / (vcc + 1)
            loglikelihood[str(w)+str(i)] = math.log10(calc)
    return (logprior, loglikelihood, V)        
        

def test(data, logprior, loglikelihood, C, V):
    summ = {}
    for i in C:   
        summ[i] = logprior[i]        
        file = open_file(data)
        
        for line in file:
            word = line
            if word in V:
                summ[i] = summ[i] + loglikelihood[word+c] 
    return max(summ)
                
    

## Function to run program
def run(data):
    ans = trainer(data)
    cat = ('0', '1')
    test(data, ans[0], ans[1], cat, ans[2])

