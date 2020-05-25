def isWhite(ch):
    if ch == ' ' or ch == '\t':
        return True
    return False

def removeWhiteSpaces(text):
    if len(text) == 0:
        return ''
    tmp = ''
    flag = isWhite(text[0])
    for ch in text:
        if flag:
            if not isWhite(ch):
                tmp+=ch
                flag=False
        else:
            if isWhite(ch):
                tmp+=' '
                flag=True
            else:
                tmp+=ch
    if flag:
        return tmp[0:len(tmp)-1]
    return tmp
data=input()
if(len(data))!=0:
    print(removeWhiteSpaces(data))
