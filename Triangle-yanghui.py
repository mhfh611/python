from functools import reduce
b = False
k = 1
    
def str2float(s):
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}[s]
    def cals(x,y):
        global b
        global k
        if(y == -1):
            b = True
            return x
        if(b == False):
            return x * 10 + y
        else:
            k = k * 0.1
            return x + y * k
            
    return reduce(cals, map(char2num, s))

print('\nstr2float(\'123.456\') =',str2float('123.456'))
