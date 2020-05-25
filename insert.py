def insert(list,number):
    index=-1
    for i in range(len(list)):
        if(list[i]>number):
            index=i
            break
    if index==-1:
        list.append(number)
    else:
        list.insert(index,number)
        
def convertToNumbers(list):
    for i in range(len(list)):
        list[i]=int(list[i])
        
def listToStr(list,sep):
    tmp=''
    length=len(list)
    for i in range(length):
        tmp+=str(list[i])
        if(i+1!=length):
            tmp+=sep
    return tmp

def run(numbers,number):
    numbers=numbers.split('-')
    convertToNumbers(numbers)
    number=int(number)
    insert(numbers, number)
    return listToStr(numbers,'-')
    
print(run(input(),input()))
