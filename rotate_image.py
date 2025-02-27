def rotate_image(input_img,degree):

    radians = math.radians(degree) #Convert degree to radians
            
    centre_img_x = (input_img.shape[1]//2) #Find centre point in x
    centre_img_y = (input_img.shape[0]//2) #Find centre point in y
    
    rotate_img_height = round(abs(image.shape[0]*math.sin(radians)))+round(abs(image.shape[1]*math.cos(radians)))
    rotate_img_width = round(abs(image.shape[1]*math.cos(radians)))+round(abs(image.shape[0]*math.sin(radians)))
    
    centre_rot_img_x = rotate_img_height//2
    centre_rot_img_y = rotate_img_width//2 
    
    output_img = np.uint8(np.zeros((rotate_img_height, rotate_img_width, image.shape[2]))) #Create new image with same size as input image
    
    #Loop the entire though entire row(i) and column(j)
    for i in range(output_img.shape[0]):
        for j in range(output_img.shape[1]):
            
            #Apply Rotating Matrix
            #Substract centre_x and centre_y to set origin at the centre of image
            x = (i - centre_rot_img_x) * math.cos(radians) + (j - centre_rot_img_y) * math.sin(radians)
            y = -(i - centre_rot_img_x) * math.sin(radians) + (j - centre_rot_img_y) * math.cos(radians)
            
            #Add centre_x and centre_y back to return our point to orginal one
            x = round(x) + centre_img_x
            y = round(y) + centre_img_y
            
            #Put condition so that any rotated points that goes beyond size of original image will be ignored  
            if(x>=0 and y>=0 and x<image.shape[0] and y<image.shape[1]):
                output_img[i,j,:] = input_img[x,y,:]
    
    #inter_img = cv2.resize(output_img,None, fx=10, fy=10, interpolation = cv2.INTER_NEAREST)
    
    return output_img

image = cv2.imread('car-1.jpg')
rotated_image = rotate_image(image,16)
cv2.imshow("rotated image", rotated_image)
cv2.waitKey(0)
