import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

plaka_adresler=os.listdir("plakalar/")
img=cv2.imread("plakalar/" + plaka_adresler[14])
img=cv2.resize(img,(500,500))

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.show()

img_bgr=img
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(img_gray,cmap="gray")
plt.show()


#plakayı görsele almak için dikdörtenin kenarlıklarıının piksel farkını vereceğiz

#piksel eleme
pik_img=cv2.medianBlur(img_gray,5)
pik_img=cv2.medianBlur(img_gray,5)
plt.imshow(pik_img,cmap="gray")
plt.show()

medyan=np.median(pik_img)
low=0.67*medyan
high=1.33*medyan

#John F. Canny algoritması,Canny Edge Detection
kenarlar=cv2.Canny(pik_img,low,high)

plt.imshow(kenarlar,cmap="gray")

plt.show()






kenarlar=cv2.dilate(kenarlar,np.ones((3,3),np.uint8),iterations=1)

####Gürültü ekleme kısmı
contours, _ = cv2.findContours(kenarlar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)







plt.imshow(kenarlar,cmap="gray")
plt.show()


#Hiyerarşik --> cv2.RETR_TREE
#CHAIN_APPROX_SIMPLE --> kosegenleri aldık,tüm pıkseller yerine
cnt=cv2.findContours(kenarlar,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt=cnt[0]
cnt=sorted(cnt,key=cv2.contourArea,reverse=True)

"""H,W=500,500
plaka=None

for c in cnt:
    rect=cv2.minAreaRect(c)  #Dikdörtgen yapıda alıyor
    (x,y),(w,h),r=rect
    if (w>h and w>h*2) or (h>w and h>2*2): #oran en az iki

        box=cv2.boxPoints(rect)
        box=np.int64(box)


       

        minx = np.min(box[:, 0])
        miny = np.min(box[:, 1])
        maxx = np.max(box[:, 0])
        # Düzeltme: Maksimum y koordinatını alın.
        maxy = np.max(box[:, 1])
        # Düzeltme: Maksimum y koordinatını alın.

        est_plaka = img_gray[miny:maxy, minx:maxx].copy()
        est_medyan = np.median(est_plaka)

        kon1 = est_medyan > 100 and est_medyan < 200

        # Düzeltme: Boyut kontrollerini düzgün şekilde yapın
        # Düzeltme: Boyut kontrollerini düzgün şekilde yapın
        kon2 = (w < 50 and h < 150) or (h < 50 and w < 150)

        kon3 = h < 50 and w < 150

        # ...

        print(f"est_plaka medyan:{est_medyan} genişlik: {w} yukseklik: {h}")

        plt.figure()
        kon=False
        plt.close()



        if (kon1 and (kon2 or kon3)):
            #plaka'dır
            cv2.drawContours(img,[box],0,(0,255,0),2)
            cv2.rectangle(img, (minx, miny), (maxx, maxy), (0, 255, 0), 2)
            plaka=[int(i) for i in [minx,miny,w,h]]

            plt.title("plaka okundu")
            kon=True


        else:
            cv2.drawContours(img,[box],0,(0,0,255),2)

            plt.title("plaka okunamadı")

        plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

        if(kon):
            break
plt.show()
"""


# ...

H, W = 500, 500
plaka = None

for c in cnt:
    area = cv2.contourArea(c)  # Kontur alanını hesaplayın

    if area < 1000:  # Kontur alanı eşiğinin altındaysa geç
        continue

    rect = cv2.minAreaRect(c)
    (x, y), (w, h), r = rect

    if (w > h and w > h * 2) or (h > w and h > 2 * w):
        box = cv2.boxPoints(rect)
        box = np.int64(box)

        minx = np.min(box[:, 0])
        miny = np.min(box[:, 1])
        maxx = np.max(box[:, 0])
        maxy = np.max(box[:, 1])

        est_plaka = img_gray[miny:maxy, minx:maxx].copy()
        est_medyan = np.median(est_plaka)

        kon1 = 100 < est_medyan < 200
        kon2 = (w < 50 and h < 150) or (h < 50 and w < 150)

        if kon1 and kon2:
            cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
            cv2.rectangle(img, (minx, miny), (maxx, maxy), (0, 255, 0), 2)  # Dikdörtgen ekleyin
            plaka = [minx, miny, w, h]
            plt.title("plaka okundu")
        else:
            cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
            plt.title("plaka okunamadı")

        plt.figure()
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.close()

        if plaka is not None:
            break

# Title'ı sonrasına taşıyın ve görseli gösterin
plt.title("Sonuç")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()



