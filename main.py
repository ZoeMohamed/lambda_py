def Tail(L):
    # Dari index 1 sampai paling belakang
    # [x:] --> akses dri index x sampai paling belakang

    return L[1:]


def FirstElement(L):
    return L[0]
def LastElement(L):
    return L[-1]
def Head(L):
    # Dari Index 0 sampai -1 artinya index paling akhirnya gak ikut  
    # [:x] dari index 0 sampai x tapi x gak ikut  
    return L[:-1]


def Konso(x,L):
    return [x] + L

def Konsi(x,L):
    return L + [x]


def isEmpty(L):
    if (L) == []:
        return True
    else:
        return False
    
def isPos(elem):
    return elem > 0

def x(f):
 return f

print(x)
def FilterList(Li,f):
    if isEmpty(Li):
        return []
    if f(FirstElement(Li)):
        # isPos(FirstElement(Li))
        return Konso(FirstElement(Li),FilterList(Tail(Li),f))
    # Konso(1,FilterList([2,3,-1],isPos()))
    else:
        return FilterList(Tail(Li),f)
    
    
x = [1,2,3,-1]
print(FilterList(x, isPos))


