import cv2 as cv
import numpy as np
import os

while true:
    cv.imshow('Image', img)





    if cv.waitkey(1) == ord('q'):
        cv.destroyAllWindows()
        break



print("DONE!")