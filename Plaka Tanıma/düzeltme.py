"""minx=np.min(box[:,0])
       miny = np.min(box[:, 1])
       maxx = np.max(box[:, 0])
       maxy = np.min(box[:, 1])

       est_plaka=img_gray[miny:maxy,minx:maxx].copy()
       est_medyan=np.median(est_plaka)

       kon1=est_medyan>100 and est_medyan<200        #Yoğunluk bulunuyor

       kon2=h<50 and w<150             #sınır kontrolü

       kon3=w<50 and h<150"""

# ...