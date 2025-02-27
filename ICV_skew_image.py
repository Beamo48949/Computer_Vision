def ICV_skew_image(input_img,degree):
    
    #Convert degree to radians
    radians = math.radians(degree)
    
    #Calculate the width that will be added from skewing 
    extra_width = round(input_img.shape[0]*math.tan(radians))
    
    #Add the above calculated width to original image
    new_width = input_img.shape[1]+extra_width
    
    #Create blank image with same height as original image but with width of original+extra_width
    output_img = np.uint8(np.zeros((input_img.shape[0], new_width, input_img.shape[2])))
    
    #Loop the entire though entire row(i) and column(j) of output image
    for i in range(output_img.shape[0]):
        for j in range(output_img.shape[1]):
            
            #Apply shear transformation matrix to the input image
            x = (i-input_img.shape[1])
            y = (i-input_img.shape[1])*math.tan(radians)+(j-input_img.shape[0])
            
            #Round up the above calculated x,y
            x = round(x+input_img.shape[1])
            y = round(y+input_img.shape[0])
            
            #Put condition if x and y is in range of the input image
            if(x>=0 and y>=0 and x<input_img.shape[0] and y<input_img.shape[1]):
                
                #Transfer the calculated point on input image pixel value to the output image
                output_img[i,j,:] = input_img[x,y,:]   
    
    return output_img

#Testing(1b)
image = cv2.imread('car-1.jpg')
skewed_image = ICV_skew_image(image,60)
cv2.imshow("Skewed image",skewed_image)
cv2.waitKey(0)
