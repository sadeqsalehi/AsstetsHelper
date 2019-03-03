import os
from pathlib import Path 
import shutil
path='Assets/vbFunctions'

mipmap=['mipmap-mdpi','mipmap-hdpi','mipmap-xhdpi','mipmap-xxhdpi','mipmap-xxxhdpi']

def cpFiles(resolution,index,ext):
    if f.find(resolution)>-1:
        f2=f.replace(resolution,'')
        shutil.copy(path+'/'+f,mipmap[index]+'/'+f2)

fileList = os.listdir(path)

for m in mipmap:
    p = Path(m)
    try:
        p.mkdir()
    except FileExistsError as exc:
        NotImplemented
        #print(exc)

for f in fileList:
    cpFiles('_mdpi',0,'.png')
    cpFiles('_hdpi',1,'.png')
    cpFiles('_xhdpi',2,'.png')
    cpFiles('_xxhdpi',3,'.png')
    cpFiles('_xxxhdpi',4,'.png')

print('done!')