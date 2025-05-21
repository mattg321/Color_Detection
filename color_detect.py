import pandas as pd
import cv2 as cv
import math

# Import csv using pandas
colors_csv = pd.read_csv(r'C:\Users\mattg\OneDrive\Desktop\Data_Science_Projects\Color_Detection\colors.csv', header = None)
# Rename columns
colors_csv.columns = ['color_name','Color Name', 'Hex', 'R', 'G', 'B']

clicked = False
r = g = b = xpos = ypos = 0

def select_color(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        global r, g, b, xpos, ypos, clicked     
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y,x]
        r = int(r)
        g = int(g)
        b = int(b)

def getColorName(R,G,B):
    min = 10000
    for i in range(len(colors_csv)):
        distance = math.sqrt(((R - int(colors_csv.loc[i, 'R']))**2 + (G - int(colors_csv.loc[i, 'G']))**2 + (B - int(colors_csv.loc[i, 'B']))**2))
        if distance < min:
            min = distance
            colorname = colors_csv.loc[i, 'Color Name']
    return colorname


# Import vegetables image and set mouse callback
img_path = r'C:\Users\mattg\OneDrive\Desktop\Data_Science_Projects\Color_Detection\vegetables.jpg'
img = cv.imread(img_path) 
cv.namedWindow('Vegetables')
cv.setMouseCallback('Vegetables', select_color)

while (1):
    cv.imshow('Vegetables', img)
    if (clicked):
        cv.rectangle(img, (20,20), (750,60), (b,g,r), -1)   
        # Create a text string for display + RGB numbers
        text = getColorName(r,g,b) +  ' R = ' + str(r) + ' G = ' + str(g) + ' B = ' + str(b)
        #                     start  font fontScale color thickness lineType
        cv.putText( img, text, (50,50), 3, 0.8, (255,255,255), 2, cv.LINE_AA)
        # For very light colors, display text in black
        if (r + g + b >= 600):
            cv.putText( img, text, (50,50), 3, 0.8, (0,0,0), 2, cv.LINE_AA)
        
        clicked = False
    
    # Break the loop whenever user presses 'esc'
    if cv.waitKey(20) & 0xFF == 27:  # ESC key
        break

cv.destroyAllWindows()
