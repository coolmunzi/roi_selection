# importing the module
import cv2
import numpy as np
import csv
import os


# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
    img2 = img.copy()
    # checking for left mouse clickspyt
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates on the Shell
        # print(x, ' ', y)
        #
        # # displaying the coordinates on the image window
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(img, str(x) + ',' +
        #             str(y), (x, y), font,
        #             0.5, (255, 0, 0), 2)
        pts.append((x, y))
        cv2.circle(img, (x, y), 2, (255, 0, 0), 2)
        cv2.imshow('image', img)

    # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        # Deleting last point
        pts.pop()
        cv2.imshow('image', img)

    if event == cv2.EVENT_MBUTTONDOWN:
        mask = np.zeros(img.shape, np.uint8)
        points = np.array(pts, np.int32)
        points = points.reshape((-1, 1, 2))

        mask = cv2.polylines(mask, [points], True, (255, 255, 255), 2)
        mask2 = cv2.fillPoly(mask.copy(), [points], (255, 255, 255))  # for ROI
        mask3 = cv2.fillPoly(mask.copy(), [points], (0, 255, 0))  # for displaying images on the desktop

        show_image = cv2.addWeighted(src1=img, alpha=0.8, src2=mask3, beta=0.2, gamma=0)

        cv2.imshow("mask", mask2)
        cv2.imshow("show_img", show_image)

        ROI = cv2.bitwise_and(mask2, img)
        cv2.imshow("ROI", ROI)
        cv2.waitKey(0)

        if len(pts) > 0:
            # Draw the last point in pts
            cv2.circle(img2, pts[-1], 3, (0, 0, 255), -1)

        if len(pts) > 1:
            #
            for i in range(len(pts) - 1):
                cv2.circle(img2, pts[i], 5, (0, 0, 255), -1)  # x ,y is the coordinates of the mouse click place
            cv2.line(img=img2, pt1=pts[i], pt2=pts[i + 1], color=(255, 0, 0), thickness=2)

        print("pts =", pts)

        #Storing the coordinates in a csv file
        for pt in pts:
            with open(r'roi_coordinates.csv', 'a', newline='') as csvfile:
                headers = ['x_coordinate', 'y_coordinate']
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                if csvfile.tell() == 0:
                    writer.writeheader()
                writer.writerow({'x_coordinate': pt[0], 'y_coordinate': pt[1]})

        cv2.imshow('image', img2)


if __name__ == "__main__":
    pts = []
    if os.path.exists('roi_coordinates.csv'):
        os.remove('roi_coordinates.csv')
    # reading the image
    img = cv2.imread('image.jpg', 1)

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse hadler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event, param=pts)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
