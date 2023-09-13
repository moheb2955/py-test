import argparse
import pyexiv2
import sys # to access the system
import cv2

#read img *************************************************************
# img = cv2.imread("zzz.jpg", cv2.IMREAD_ANYCOLOR)
#
# while True:
#     cv2.imshow("zzz", img)
#     cv2.waitKey(0)
#     sys.exit()  # to exit from all the processes
#
# cv2.destroyAllWindows()





img = pyexiv2.Image(r'Canon_40D.jpg')
data = img.read_exif()
img.clear_exif()
img.close()
print(data)

# def clearAllMetadata(imgName):
#     metadata = pyexiv2.ImageData(imgName)
#     metadata.read_exif()
#     metadata.clear_exif()
#     metadata.read_exif()
#     print(metadata)


# clearAllMetadata(img)