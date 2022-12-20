import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError


a = []
count = 1000 #Number of images
for i in range(0, count+1):
    a.append(str(i).rjust(4, '0'))

name = 'example' #Name of the folder (Name of the model)

os.mkdir('F:/' + name + '/') #Path of the folder to be created

for i in range(1, len(a)):
    call = a[i]
    url = 'https://fapello.com/content/h/a/example/1000/example_' + call + '.jpg' #URL of the images excluding the "number.jpg"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        webpage = urlopen(req).read()
    except HTTPError as err:
        if err.code == 404:
            continue
    #webpage = urlopen(req).read()
    f = open('F:/' + name + '/' + name + '_' + call + '.jpg', 'wb') #Path of the folder + name of the folder + name of the image
    f.write(webpage)
    f.close()
