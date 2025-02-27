def convolute_img(input_img,kernel):
    
    #Create black image size of input image with extra one row and column  
    input_img_black = np.uint8(np.zeros((input_img.shape[0]+2, input_img.shape[1]+2, input_img.shape[2])))
    
    #Transfer input image to the created black image
    #We create a input image with surrounded by black(null) pixels
    #So that we can convolute the pixels at the border
    for i in range(input_img.shape[0]):
        for j in range(input_img.shape[1]):
            
            x = i
            y = j
            
            if(x>=0 and y>=0 and x<input_img.shape[0] and y<input_img.shape[1]):
                input_img_black[i+1,j+1,:] = input_img[x,y,:]
    
    #Create black image same size as input image
    output_img = np.uint8(np.zeros(input_img.shape))
    
    #minus 1 to ignore the last row and column that are black pixel
    for i in range(output_img.shape[0]):
        for j in range(output_img.shape[1]):

            x = i+1
            y = j+1
            
            (b, g, r) = input_img_black[x-1,y-1]
            (p1_b, p1_g, p1_r) = (b*kernel[0][0], g*kernel[0][0], r*kernel[0][0])
            
            (b, g, r) = input_img_black[x-1,y]
            (p2_b, p2_g, p2_r) = (b*kernel[0][1], g*kernel[0][1], r*kernel[0][1])
            
            (b, g, r) = input_img_black[x-1,y+1]
            (p3_b, p3_g, p3_r) = (b*kernel[0][2], g*kernel[0][2], r*kernel[0][2])
            
            (b, g, r) = input_img_black[x,y-1]
            (p4_b, p4_g, p4_r) = (b*kernel[1][0], g*kernel[1][0], r*kernel[1][0])
            
            (b, g, r) = input_img_black[x,y]
            (p5_b, p5_g, p5_r) = (b*kernel[1][1], g*kernel[1][1], r*kernel[1][1])
            
            (b, g, r) = input_img_black[x,y+1]
            (p6_b, p6_g, p6_r) = (b*kernel[1][2], g*kernel[1][2], r*kernel[1][2])
            
            (b, g, r) = input_img_black[x+1,y-1]
            (p7_b, p7_g, p7_r) = (b*kernel[2][0], g*kernel[2][0], r*kernel[2][0])
            
            (b, g, r) = input_img_black[x+1,y]
            (p8_b, p8_g, p8_r) = (b*kernel[2][1], g*kernel[2][1], r*kernel[2][1])
            
            (b, g, r) = input_img_black[x+1,y+1]
            (p9_b, p9_g, p9_r) = (b*kernel[2][2], g*kernel[2][2], r*kernel[2][2])
            
            (p_result_b, p_result_g, p_result_r) = ((p1_b+p2_b+p3_b+p4_b+p5_b+p6_b+p7_b+p8_b+p9_b),
                                                    (p1_g+p2_g+p3_g+p4_g+p5_g+p6_g+p7_g+p8_g+p9_g),
                                                    (p1_r+p2_r+p3_r+p4_r+p5_r+p6_r+p7_r+p8_r+p9_r))
            
            print(p_result_b, p_result_g, p_result_r)
            
            if(x>=0 and y>=0 and x<output_img.shape[0]+1 and y<output_img.shape[1]+1):
                output_img[i][j] = (p_result_b, p_result_g, p_result_r)
    
    print(kernel)
    return output_img

k =[[0,0,0],[0,1,0],[0,0,0]]

image = cv2.imread('car-1.jpg')
C_image = convolute_img(image,k)
cv2.imshow('image', C_image)
cv2.waitKey(0)           
