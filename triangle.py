import math
def triangle(expr):
    num=''
    if('sin' in expr):
        num=int(expr[expr.find('(')+1:len(expr)-1])%360
        if num==0 or num==180 :
            num='0.0'
        else:
            num=math.sin(math.radians(num))
    elif('cos' in expr):
        num=int(expr[expr.find('(')+1:len(expr)-1])%360
        if num==90 or num==270:
            num='0.0'
        else:
            num=math.cos(math.radians(num))
    elif ('tan' in expr):
        num=int(expr[expr.find('(')+1:len(expr)-1])
        tmp=num%360
        if tmp==90 or tmp==270:
            num='invalid angle'
        elif tmp==0 or tmp==180 :
            num='0.0'
        elif tmp==45 or tmp==225:
            num='1.0'
        elif tmp==135 or tmp==315:
            num='-1.0'
        else:
            num=math.tan(math.radians(int(expr[expr.find('(')+1:len(expr)-1])))
    elif ('cot' in expr):
        num=int(expr[expr.find('(')+1:len(expr)-1])
        tmp=num%360
        if tmp==0 or tmp==180 :
            num='invalid angle'
        elif tmp==90 or tmp==270:
            num='0.0'
        elif tmp==45 or tmp==225:
            num='1.0'
        elif tmp==135 or tmp==315:
            num='-1.0'
        else:
            num=1/math.tan(math.radians(int(expr[expr.find('(')+1:len(expr)-1])))
    else:
        num="invalid function"
    return num
print(triangle(input()))
