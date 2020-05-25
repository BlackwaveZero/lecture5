def inOperator(text,word):
    lenStr=len(text)
    lenWord=len(word)

    for i in range(lenStr-lenWord+1):
        if(text[i:i+lenWord]==word):
            return 'True'
            
    return 'False'
    
print(inOperator(input(),input()))
