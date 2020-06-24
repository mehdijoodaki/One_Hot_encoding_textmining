import numpy as np
stats=[]
path='filename'
file_in=open(path,'r')    
#Read file and write onto a list   
while(True):
    
    line=file_in.readline()
    
    if line == '':
        break
    
    for l in line.rstrip('\n').split('.'):
        
        stats.append(l)
#Creat a dic
token={}
#Read each sentence and split to words ,after that write each word with its index((key ,value))
for stat in stats:
    for word in stat.split():
        if word not in token :
            token[word]=len(token)+1


    

max_length=100 #We want consider just 100 words for each sentence.
lenghth_words=len(token.keys())
shape=(len(stats),max_length,lenghth_words+1)
results=np.zeros(shape)

#For giving index
for i,stat in enumerate(stats):
    for j,word in list(enumerate(stat.split()))[:max_length]:
        index=token[word]
        results[i,j,index]=1.
        

    
   
    

