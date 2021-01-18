import numpy as np
import imutils
import cv2

image = cv2.imread('next.png')
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detector = cv2.MSER_create()
kps = detector.detect(gray)

print('# of the keypoints: {}'.format(len(kps)))

for kp in kps:
    r = int(0.5 * kp.size)
    (x, y) = np.int0(kp.pt)
    cv2.circle(image, (x, y), r, (0, 255, 255), 2)

cv2.imshow('Image', image)
cv2.waitKey(0)