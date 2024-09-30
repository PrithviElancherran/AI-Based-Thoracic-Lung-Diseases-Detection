from PIL import Image
import os
c=0
source="E:\\tubercolosis dataset\\archive (4)\\ChinaSet_AllFiles\\ChinaSet_AllFiles\\CXR_png\\"
for names in os.listdir(source):
    name=names[:-4]
    im1 = Image.open(source+names).convert("RGB")
    im1.save('E:\\TB JPEG\\'+name+'.jpeg')
    c=c+1
    if(c%100==0):
        print("Done")
