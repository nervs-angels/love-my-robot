import json
import os.path, os

def parselmr():
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
     
def filename():
    with open('lex/test.json') as f:
        data = json.load(f)    
    request_timestamp=data['request_timestamp']
    request_timestamp="lmr_lex"+request_timestamp+".py"
    request_timestamp=request_timestamp.replace("CST","").replace(":","-").replace(" ",'_')
    request_timestamp=request_timestamp.replace("Sun",'').replace("Mon",'')
    request_timestamp=request_timestamp.replace('Jan','1').replace("Feb","2").replace("Mar","3").replace("Apr","4").replace("May","5").replace("Jun","6").replace("Jul","7").replace("Aug","8").replace("Sep","9").replace("Oct","10").replace("Nov","11").replace("Dec","12")
    return (request_timestamp)

def savefile(filename, data):
    save_path='transpiled/'
    completeName = os.path.join(save_path, filename) 
    f = open(completeName,"w")
    f.write(data)
    f.close()
    os.system(completeName)
    