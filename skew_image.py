def skew_image(input_img,degree):

    radians = math.radians(degree) #Convert degree to radians
    
    extra_width = input_img.shape[0]*math.tan(radians)    
    new_width = round(input_img.shape[1]+extra_width)
    
    output_img = np.uint8(np.zeros((input_img.shape[0], new_width, input_img.shape[2])))
    
  #Loop the entire though entire row(i) and column(j)
    for i in range(output_img.shape[0]):
        for j in range(output_img.shape[1]):
            
            x = (i-input_img.shape[1])
            y = (i-input_img.shape[1])*radians+(j-input_img.shape[0])
            
            x = round(x+input_img.shape[1])
            y = round(y+input_img.shape[0])
              
            if(x>=0 and y>=0 and x<input_img.shape[0] and y<input_img.shape[1]):
                output_img[i,j,:] = input_img[x,y,:]   
    
    return output_img
    
image = cv2.imread('car-1.jpg')
skewed_image = skew_image(image,40)
cv2.imshow("skewed image", skewed_image)
cv2.waitKey(0)
