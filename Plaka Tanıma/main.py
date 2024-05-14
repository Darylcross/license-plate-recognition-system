import os
import matplotlib.pyplot as plt

import cv2

"""1.diske bağlanıp fotoğrafların urlsini alacaz"""
"""2.fotoğrafın x,y,z değerlerini bu kütüphane ile inceleyecez"""

tanimli_plaka=os.listdir(("plakalar/"))

for plaka_url in tanimli_plaka:
    plaka = cv2.imread("plakalar/" + plaka_url)
    plaka=cv2.cvtColor(plaka,cv2.COLOR_BGR2RGB)
    plaka=cv2.resize(plaka,(500,500))

    plt.imshow(plaka)
    plt.show()

"""plakalara ait değerler
1.resim:
x aralığı :223
y aralığı :57      x5


2.resim:
x aralığı :165
y aralığı :42       x4

3.resim:
x aralığı :193
y aralığı :37         x6

4.resim:
x aralığı :713        x5
y aralığı :138

plakaları dikdörtgen çerceveye sığdıracaz 
arka plan beyaz 
renk değerleri 150<x<250 arası
resize ile aynı boyut içerisinde değerlendirecez


plakaların karakterlere sahip olması


ilk aşamada dikdörtgenleri tespit ediyorsun
h,w oranı 3 kat
arka plan renk değişimi 100<x<200









"""