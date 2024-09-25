""" 
This prorgam crop the images based on the points 
selected using the mouse clicks and crop these selected 
image and transform it so as to it will look like the 
merror image of the selected points.
"""

import cv2 as cv
import numpy as np

# generateing the blank image 
circle = np.zeros((4, 2), int)
counter = 0

def cropImage(image):
#reading the image
    img = cv.imread(image)

    # tracking the mouse events
    def mouseEvent(event, x, y, flags, params):
        global counter
        if event == cv.EVENT_LBUTTONDOWN:
            print(x, y)
            circle[counter] = x, y
            counter += 1
            print(circle)

    while True:
        if counter == 4:
            width, height = 250, 350
            pts1 = np.float32(circle)
            pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            matrix = cv.getPerspectiveTransform(pts1, pts2)
            imgoutput = cv.warpPerspective(img, matrix, (width, height))
            cv.imshow("Output", imgoutput)

        # displaying the selected points else sets as zero
        for x in range(0, 4):
            cv.circle(img, (circle[x][0], circle[x][1]), 3, (0, 255, 0), cv.FILLED)

        cv.imshow("img", img)
        cv.setMouseCallback("img", mouseEvent)

        if cv.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break
        
        
if __name__ == "__main__":
    image = input("Enter the image name/path \n:- ")
    cropImage(image)
    cv.destroyAllWindows()
