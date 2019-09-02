import cv2
import numpy

from PIL import Image
from PIL import ImageCms

# force opening truncated/corrupt image files
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

img = "cropped.jpg"

img = Image.open(img)
if img.mode == "CMYK":
    # color profiles can be found at C:\Program Files (x86)\Common Files\Adobe\Color\Profiles\Recommended
    img = ImageCms.profileToProfile(img, "USWebCoatedSWOP.icc", "sRGB_Color_Space_Profile.icm", outputMode="RGB")
# PIL image -> OpenCV image; see https://stackoverflow.com/q/14134892/2202732
img = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)

## (1) Convert to gray, and threshold
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

## (2) Morph-op to remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

## (3) Find the max-area contour
cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
cnt = sorted(cnts, key=cv2.contourArea)[-1]

## (4) Crop and save it
x,y,w,h = cv2.boundingRect(cnt)
dst = img[y:y+h, x:x+w]

# add border/padding around the cropped image
# dst = cv2.copyMakeBorder(dst, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255,255,255])

cv2.imwrite('cropped.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()