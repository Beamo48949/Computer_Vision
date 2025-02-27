def ICV_greyscale_img(input_img):

    output_img = np.uint8(np.zeros((input_img.shape)))
    
    for i in range(output_img.shape[0]):
        for j in range(output_img.shape[1]):
            
            (b, g, r) = input_img[i,j]
            grey = (0.114*b)+(0.587*g)+(0.2989*r)
            
            if(i>=0 and j>=0 and i<output_img.shape[0] and j<output_img.shape[1]):
                output_img[i,j,:] = grey

    return output_img

image = cv2.imread('car-1.jpg')
grey_image = ICV_greyscale_img(image)
cv2.imshow('image', grey_image)
cv2.waitKey(0)   
