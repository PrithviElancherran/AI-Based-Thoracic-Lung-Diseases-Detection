import os

source="E:\\tubercolosis dataset\\archive(4)\\ChinaSet_AllFiles\\ChinaSet_AllFiles\\CXR_png\\"
f=open("C:\\Users\\prith\\Downloads\\names.txt",'w')

for names in os.listdir(source):
    name=names[:-4]
    if(name[-1]=='0'):
        name+=',No finding,14'
    else:
        name+=',Pulmonary tuberculosis,15'
    f.write(name+"\n")
f.close()