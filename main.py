import numpy as np
import cv2

# ===================== #
#     BLOB_DETECTOR     #
# ===================== #

class blob_detector():
    def __init__(self):
        # initialize your detector
        pass
        
        
    def detect(self, img, params):
    # ================================================= #
    # TODO: implement your blob detecting function here
    # ================================================= #
        return blob_number, blob_plot

# Read image
img = cv2.imread('img/dots.jpeg', 0)   # zero for grayscale

# Detect blobs
detector = blob_detector()
blob_number, blob_plot = detector.detect(img)

# Display your results
print('Number of blobs:', blob_number)
cv2.imshow('Figure', blob_plot)
cv2.waitKey(0)

# Save the image with blobs and show them on the report
cv2.imwrite("dots_with_blobs.jpeg", blob_plot)

'''
For Bonus question, you can time your code using the following code

import time
from google.colab.patches import cv2_imshow

detector = YOUR_BLOB_DETECTOR
start = time.time()
blob_number, blob_plot = detector.detect(img)
end = time.time()
print('Number of blobs:', blob_number)
cv2_imshow(blob_plot)
print('Execution time:', end - start)

'''

