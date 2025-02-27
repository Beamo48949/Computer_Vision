def ICV_rotate_image(input_img,degree):
    
    #Convert degree to radians
    radians = math.radians(degree)
    
    #Find centre point of input image
    centre_img_x = (input_img.shape[1]//2) 
    centre_img_y = (input_img.shape[0]//2)
    
    #Find width and height that rotated image will have
    rotate_img_height = round(abs(input_img.shape[0]*math.sin(radians)))+round(abs(input_img.shape[1]*math.cos(radians)))
    rotate_img_width = round(abs(input_img.shape[1]*math.cos(radians)))+round(abs(input_img.shape[0]*math.sin(radians)))
    
    #Find centre point of the rotated image
    centre_rot_img_x = rotate_img_height//2
    centre_rot_img_y = rotate_img_width//2 
    
    #Create blank image with size that will fit the rotated image
    output_img = np.uint8(np.zeros((rotate_img_height, rotate_img_width, image.shape[2]))) #Create new image with same size as input image
    
    #Loop the entire though entire row(i) and column(j) of output image
    for i in range(output_img.shape[0]):
        for j in range(output_img.shape[1]):
            
            #Apply Rotating Matrix
            #Substract centre_x and centre_y to set origin at the centre of image
            x = (i - centre_rot_img_x) * math.cos(radians) - (j - centre_rot_img_y) * math.sin(radians)
            y = (i - centre_rot_img_x) * math.sin(radians) + (j - centre_rot_img_y) * math.cos(radians)
            
            #Add centre_x and centre_y back to return our point to orignal one
            x = round(x) + centre_img_x
            y = round(y) + centre_img_y
            
            #Put condition if x and y is in range of the input image
            if(x>=0 and y>=0 and x<input_img.shape[0] and y<input_img.shape[1]):
                
                #Transfer the calculated point on input image pixel value to the output image 
                output_img[i,j,:] = input_img[x,y,:]
    
    return output_img

#Testing(1a)
image = cv2.imread('car-1.jpg')
rotated_image = ICV_rotate_image(image,-50)
cv2.imshow("Rotated image",rotated_image)
cv2.waitKey(0)
