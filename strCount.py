def strCount(sentence,word):

    count=0
    lenStr=len(sentence)
    lenWord=len(word)

    for i in range(lenStr-lenWord+1):
        if(sentence[i:i+lenWord]==word):
            count+=1

    return count

print(strCount(input(),input()))
