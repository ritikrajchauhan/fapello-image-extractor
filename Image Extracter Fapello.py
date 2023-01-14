import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# Edit these variables according to each model
count = 100                                                                             #Number of images in range 1 to 1000
name = 'ModelName'                                                                    #Name of the model
savePath = 'C:\PathExample'                                                                 #Path of the folder for saving the images and videos
link = 'https://fapello.com/content/e/l/ModelName/1000/ModelName_0001.jpg'          #Link of the model's one image

a = []
for i in range(0, count+1):
    a.append(str(i).rjust(4, '0'))

savePath += '\\' + name + '\\'
link = link[:-8]

os.mkdir(savePath)

for i in range(1, len(a)):
    call = a[i]
    url = link + call + '.jpg'
    urlVideo = link + call + '.mp4'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    reqVideo = Request(urlVideo, headers={'User-Agent': 'Mozilla/5.0'})
    if(True):
        try:
            webpage = urlopen(reqVideo).read()
            #webpage = urlopen(req).read()
            f = open(savePath + name + '_' + call + '.mp4', 'wb')
            f.write(webpage)
            f.close()
        except HTTPError as err:
            if err.code == 404:
                try:
                    webpage = urlopen(req).read()
                except HTTPError as err:
                    if err.code == 404:
                        continue
                #webpage = urlopen(req).read()
                f = open(savePath + name + '_' + call + '.jpg', 'wb')
                f.write(webpage)
                f.close()
