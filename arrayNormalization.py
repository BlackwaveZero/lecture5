def getList(text):#splits string based (,) literal
    return text.split(',')
    
def calc(diff,min,data):
    return round(((data-min)*100/diff),6)
    
def convertToReadable(array):#converts a list to readable string
    text=''
    length=len(array)
    
    for i in range(length):
        text+=str(array[i])
        if i+1!=length:
            text+=','
            
    return text
    
    
def normalize(array):#gets a list(must be sorted or u get invalid output) and returns that list which every element is normalized 
    if len(array) == 2:
        return [0.0,100.0 ]
    min=int(array[0])
    max=int(array[0])
    
    for i in range(len(array)):
        array[i]=int(array[i])
        if array[i]>max:
            max=array[i]
        if array[i]<min:
            min=array[i]
      
    diff=max-min
    normalized=[]
    
    for el in array:
        normalized.append(calc(diff,min,el))
        
    return normalized
    
    
def run(text):
    array=getList(text)
    array.sort()
    array=normalize(array)
    return convertToReadable(array)
    
print(run(input()))
