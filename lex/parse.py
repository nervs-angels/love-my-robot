import json

def parse():
    with open('lex/test.json') as f:
        data = json.load(f)
    
    data2= data['lmr'].split('\n')
    print(data2)
    
    array = []
    for i in data2:
        array.append(i)

    array2=[]
    j=0     

    for i in array:
        data2[j]=i.split(',')
        array2.append(data2[j])
        j=j+1
    
    return array2
    
parse()    
