def strSplit(text,separator):
    separated=[]
    
    lenStr=len(text)
    lenWord=len(separator)
    lastIndex=0
    
    for i in range(lenStr-lenWord+1):
        if(text[i:i+lenWord]==separator):
            separated.append(text[lastIndex:i])
            lastIndex=i+lenWord
            
    if(lastIndex<lenStr):
        separated.append(text[lastIndex:lenStr])
    elif lastIndex==lenStr:
        separated.append('')
        
    return separated

splited=strSplit(input(),input())
for el in splited:
    print(el)
