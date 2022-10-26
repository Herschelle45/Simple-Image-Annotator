import cv2 
import csv 

filepath = input('Image path: ')
csvfile = open('annotations.csv', 'w')
write = csv.writer(csvfile)

#reading and showing image 
img = cv2.imread(filepath)
cv2.imshow('Image', img)    

#store coordinates to be written in csv file 
coords = []

#mouse click 
def m_click(event, x, y, flags, param):
    coordinates = f'({x}, {y})'
    if event==cv2.EVENT_LBUTTONDOWN:
        print(coordinates)
        cv2.putText(img, '+ ' + coordinates, (x,y),cv2.FONT_HERSHEY_PLAIN,1,(51, 255, 51))
        cv2.imshow('Image', img)
        if cv2.waitKey(0) == ord('w'):
            coords.append([x, y])

# mouse callback 
cv2.setMouseCallback('Image', m_click)

#close when pressed esc; esc = 27
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

#write csvfile 
write.writerows(coords)
csvfile.close()
