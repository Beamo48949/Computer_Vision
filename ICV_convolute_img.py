def ICV_convolute_img(input_img,kernel):
    
    #Create padding size of input image with extra one row and column  
    input_img_black = np.uint8(np.zeros((input_img.shape[0]+2, input_img.shape[1]+2, input_img.shape[2])))
    
    #Transfer input image to the created black image
    #We create a input image with surrounded by black(null) pixels
    #So that we can convolute the pixels at the border
    for i in range(input_img.shape[0]):
        for j in range(input_img.shape[1]):
                
            #Transfer input image on the padding
            if(i>=0 and j>=0 and i<input_img.shape[0] and j<input_img.shape[1]):
                input_img_black[i+1,j+1,:] = input_img[i,j,:]
    
    #Create black image same size as input image
    output_img = np.uint8(np.zeros(input_img.shape))
    
    
    
    #For 3*3 kernel
    if len(kernel[1]) == 3 and len(kernel[0]) == 3:   
        
        #Summation of all value in kernel
        kernel_total = abs(kernel[0][0])+abs(kernel[0][1])+abs(kernel[0][2])+abs(kernel[1][0])+abs(kernel[1][1])+\
                        abs(kernel[1][2])+abs(kernel[2][0])+abs(kernel[2][1])+abs(kernel[2][2])
        
        #Loop the entire though entire row(i) and column(j) of output image
        for i in range(output_img.shape[0]):
            for j in range(output_img.shape[1]):
                
                #For ignoring the first row and column, which is black pixels
                x = i+1
                y = j+1
                
                #For row 1 and column 1
                #store BGR value from input image
                (b, g, r) = input_img_black[x-1,y-1]
                #multiply kernel to the BGR values
                (p1_b, p1_g, p1_r) = (b*kernel[0][0], g*kernel[0][0], r*kernel[0][0])
                
                #For row 1 and column 2
                (b, g, r) = input_img_black[x-1,y]
                (p2_b, p2_g, p2_r) = (b*kernel[0][1], g*kernel[0][1], r*kernel[0][1])
                
                #For row 1 and column 3
                (b, g, r) = input_img_black[x-1,y+1]
                (p3_b, p3_g, p3_r) = (b*kernel[0][2], g*kernel[0][2], r*kernel[0][2])
                
                #For row 2 and column 1
                (b, g, r) = input_img_black[x,y-1]
                (p4_b, p4_g, p4_r) = (b*kernel[1][0], g*kernel[1][0], r*kernel[1][0])
                
                #For row 2 and column 2
                (b, g, r) = input_img_black[x,y]
                (p5_b, p5_g, p5_r) = (b*kernel[1][1], g*kernel[1][1], r*kernel[1][1])
                
                #For row 2 and column 3
                (b, g, r) = input_img_black[x,y+1]
                (p6_b, p6_g, p6_r) = (b*kernel[1][2], g*kernel[1][2], r*kernel[1][2])
                
                #For row 3 and column 1
                (b, g, r) = input_img_black[x+1,y-1]
                (p7_b, p7_g, p7_r) = (b*kernel[2][0], g*kernel[2][0], r*kernel[2][0])
                
                #For row 3 and column 2
                (b, g, r) = input_img_black[x+1,y]
                (p8_b, p8_g, p8_r) = (b*kernel[2][1], g*kernel[2][1], r*kernel[2][1])
                
                #For row 3 and column 3
                (b, g, r) = input_img_black[x+1,y+1]
                (p9_b, p9_g, p9_r) = (b*kernel[2][2], g*kernel[2][2], r*kernel[2][2])
                
                #Summation of convolution 
                (p_result_b, p_result_g, p_result_r) = (p1_b+p2_b+p3_b+p4_b+p5_b+p6_b+p7_b+p8_b+p9_b),\
                                                        (p1_g+p2_g+p3_g+p4_g+p5_g+p6_g+p7_g+p8_g+p9_g),\
                                                        (p1_r+p2_r+p3_r+p4_r+p5_r+p6_r+p7_r+p8_r+p9_r)
                
                #Divide the result with total of kernel elements
                (p_result_b, p_result_g, p_result_r) = (p_result_b/kernel_total, p_result_g/kernel_total,\
                                                        p_result_r/kernel_total)
                
                #Transfer result onto image
                if(x>=0 and y>=0 and x<output_img.shape[0]+1 and y<output_img.shape[1]+1):
                    output_img[i][j] = (p_result_b, p_result_g, p_result_r)
               
            
        
    #For 5*5 kernel
    if len(kernel[1]) == 5 and len(kernel[0]) == 5:   
        
        #Summation of all value in kernel
        kernel_total = abs(kernel[0][0])+abs(kernel[0][1])+abs(kernel[0][2])+abs(kernel[0][3])+abs(kernel[0][4])\
                        +abs(kernel[1][0])+abs(kernel[1][1])+abs(kernel[1][2])+abs(kernel[1][3])+abs(kernel[1][4])\
                        +abs(kernel[2][0])+abs(kernel[2][1])+abs(kernel[2][2])+abs(kernel[2][3])+abs(kernel[2][4])
        
        #Loop the entire though entire row(i) and column(j) of output image
        for i in range(output_img.shape[0]):
            for j in range(output_img.shape[1]):
                
                #For ignoring the first row and column, which is black pixels
                x = i+2
                y = j+2
                
                #For row 1 
                #column 1
                (b, g, r) = input_img_black[x-2,y-2]
                (p1_b, p1_g, p1_r) = (b*kernel[0][0], g*kernel[0][0], r*kernel[0][0])
                
                #column 2
                (b, g, r) = input_img_black[x-2,y-1]
                (p2_b, p2_g, p2_r) = (b*kernel[0][1], g*kernel[0][1], r*kernel[0][1])
                
                #column 3
                (b, g, r) = input_img_black[x-2,y]
                (p3_b, p3_g, p3_r) = (b*kernel[0][2], g*kernel[0][2], r*kernel[0][2])
                
                #column 4
                (b, g, r) = input_img_black[x-2,y+1]
                (p4_b, p4_g, p4_r) = (b*kernel[0][3], g*kernel[0][3], r*kernel[0][3])
                
                #column 5
                (b, g, r) = input_img_black[x-2,y+2]
                (p5_b, p5_g, p5_r) = (b*kernel[0][4], g*kernel[0][4], r*kernel[0][4])
                
                
                #For row 2
                #column 1
                (b, g, r) = input_img_black[x-1,y-2]
                (p6_b, p6_g, p6_r) = (b*kernel[1][0], g*kernel[1][0], r*kernel[1][0])
                
                #column 2
                (b, g, r) = input_img_black[x-1,y-1]
                (p7_b, p7_g, p7_r) = (b*kernel[1][1], g*kernel[1][1], r*kernel[1][1])
                
                #column 3
                (b, g, r) = input_img_black[x-1,y]
                (p8_b, p8_g, p8_r) = (b*kernel[1][2], g*kernel[1][2], r*kernel[1][2])
                
                #column 4
                (b, g, r) = input_img_black[x-1,y+1]
                (p9_b, p9_g, p9_r) = (b*kernel[1][3], g*kernel[1][3], r*kernel[1][3])
                
                #column 5
                (b, g, r) = input_img_black[x-1,y+2]
                (p10_b, p10_g, p10_r) = (b*kernel[1][4], g*kernel[1][4], r*kernel[1][4])
                
                
                #For row 3
                #column 1
                (b, g, r) = input_img_black[x,y-2]
                (p11_b, p11_g, p11_r) = (b*kernel[2][0], g*kernel[2][0], r*kernel[2][0])
                
                #column 2
                (b, g, r) = input_img_black[x,y-1]
                (p12_b, p12_g, p12_r) = (b*kernel[2][1], g*kernel[2][1], r*kernel[2][1])
                
                #column 3
                (b, g, r) = input_img_black[x,y]
                (p13_b, p13_g, p13_r) = (b*kernel[2][2], g*kernel[2][2], r*kernel[2][2])
                
                #column 4
                (b, g, r) = input_img_black[x,y+1]
                (p14_b, p14_g, p14_r) = (b*kernel[2][3], g*kernel[2][3], r*kernel[2][3])
                
                #column 5
                (b, g, r) = input_img_black[x,y+2]
                (p15_b, p15_g, p15_r) = (b*kernel[2][4], g*kernel[2][4], r*kernel[2][4])
                
                
                #For row 4
                #column 1
                (b, g, r) = input_img_black[x+1,y-2]
                (p16_b, p16_g, p16_r) = (b*kernel[3][0], g*kernel[3][0], r*kernel[3][0])
                
                #column 2
                (b, g, r) = input_img_black[x+1,y-1]
                (p17_b, p17_g, p17_r) = (b*kernel[3][1], g*kernel[3][1], r*kernel[3][1])
                
                #column 3
                (b, g, r) = input_img_black[x+1,y]
                (p18_b, p18_g, p18_r) = (b*kernel[3][2], g*kernel[3][2], r*kernel[3][2])
                
                #column 4
                (b, g, r) = input_img_black[x+1,y+1]
                (p19_b, p19_g, p19_r) = (b*kernel[3][3], g*kernel[3][3], r*kernel[3][3])
                
                #column 5
                (b, g, r) = input_img_black[x+1,y+2]
                (p20_b, p20_g, p20_r) = (b*kernel[3][4], g*kernel[3][4], r*kernel[3][4])
                
                
                #For row 5
                #column 1
                (b, g, r) = input_img_black[x+2,y-2]
                (p21_b, p21_g, p21_r) = (b*kernel[4][0], g*kernel[4][0], r*kernel[4][0])
                
                #column 2
                (b, g, r) = input_img_black[x+2,y-1]
                (p22_b, p22_g, p22_r) = (b*kernel[4][1], g*kernel[4][1], r*kernel[4][1])
                
                #column 3
                (b, g, r) = input_img_black[x+2,y]
                (p23_b, p23_g, p23_r) = (b*kernel[4][2], g*kernel[4][2], r*kernel[4][2])
                
                #column 4
                (b, g, r) = input_img_black[x+1,y+1]
                (p24_b, p24_g, p24_r) = (b*kernel[4][3], g*kernel[4][3], r*kernel[4][3])
                
                #column 5
                (b, g, r) = input_img_black[x+2,y+2]
                (p25_b, p25_g, p25_r) = (b*kernel[4][4], g*kernel[4][4], r*kernel[4][4])
                
                #Summation of convolution 
                (p_result_b, p_result_g, p_result_r) = (p1_b+p2_b+p3_b+p4_b+p5_b+p6_b+p7_b+p8_b+p9_b+p10_b\
                                                        +p11_b+p12_b+p12_b+p14_b+p15_b+p16_b+p17_b+p18_b+p19_b\
                                                        +p20_b+p21_b+p22_b+p23_b+p24_b+p25_b),\
                                                        (p1_g+p2_g+p3_g+p4_g+p5_g+p6_g+p7_g+p8_g+p9_g+p10_g\
                                                        +p11_g+p12_g+p12_g+p14_g+p15_g+p16_g+p17_g+p18_g+p19_g\
                                                        +p20_g+p21_g+p22_g+p23_g+p24_g+p25_g),\
                                                        (p1_r+p2_r+p3_r+p4_r+p5_r+p6_r+p7_r+p8_r+p9_r+p10_r\
                                                        +p11_r+p12_r+p12_r+p14_r+p15_r+p16_r+p17_r+p18_r+p19_r\
                                                        +p20_r+p21_r+p22_r+p23_r+p24_r+p25_r)
                
                #Divide the result with total of kernel elements
                (p_result_b, p_result_g, p_result_r) = (p_result_b/kernel_total, p_result_g/kernel_total,\
                                                        p_result_r/kernel_total)
                
                #Transfer result onto image
                if(x>=0 and y>=0 and x<output_img.shape[0]+2 and y<output_img.shape[1]+2):
                    output_img[i][j] = (p_result_b, p_result_g, p_result_r)
    
    
    
    #For 7*7 kernel
    if len(kernel[1]) == 7 and len(kernel[0]) == 7:   
        
        #Summation of all value in kernel
        kernel_total = abs(kernel[0][0])+abs(kernel[0][1])+abs(kernel[0][2])+abs(kernel[0][3])+abs(kernel[0][4])+abs(kernel[0][5])+abs(kernel[0][6])\
                        +abs(kernel[1][0])+abs(kernel[1][1])+abs(kernel[1][2])+abs(kernel[1][3])+abs(kernel[1][4])+abs(kernel[1][5])+abs(kernel[1][6])\
                        +abs(kernel[2][0])+abs(kernel[2][1])+abs(kernel[2][2])+abs(kernel[2][3])+abs(kernel[2][4])+abs(kernel[2][5])+abs(kernel[2][6])
        
        #Loop the entire though entire row(i) and column(j) of output image
        for i in range(output_img.shape[0]):
            for j in range(output_img.shape[1]):
                
                #For ignoring the first row and column, which is black pixels
                x = i+3
                y = j+3
                
                #For row 1 
                (b, g, r) = input_img_black[x-3,y-3]
                (p1_b, p1_g, p1_r) = (b*kernel[0][0], g*kernel[0][0], r*kernel[0][0])
                
                (b, g, r) = input_img_black[x-3,y-2]
                (p2_b, p2_g, p2_r) = (b*kernel[0][1], g*kernel[0][1], r*kernel[0][1])
                
                (b, g, r) = input_img_black[x-3,y-1]
                (p3_b, p3_g, p3_r) = (b*kernel[0][2], g*kernel[0][2], r*kernel[0][2])
                
                (b, g, r) = input_img_black[x-3,y]
                (p4_b, p4_g, p4_r) = (b*kernel[0][3], g*kernel[0][3], r*kernel[0][3])
                
                (b, g, r) = input_img_black[x-3,y+1]
                (p5_b, p5_g, p5_r) = (b*kernel[0][4], g*kernel[0][4], r*kernel[0][4])
                
                (b, g, r) = input_img_black[x-3,y+2]
                (p6_b, p6_g, p6_r) = (b*kernel[0][5], g*kernel[0][5], r*kernel[0][5])
                
                (b, g, r) = input_img_black[x-3,y+3]
                (p7_b, p7_g, p7_r) = (b*kernel[0][6], g*kernel[0][6], r*kernel[0][6])
                
                
                #For row 2
                (b, g, r) = input_img_black[x-2,y-3]
                (p8_b, p8_g, p8_r) = (b*kernel[1][0], g*kernel[1][0], r*kernel[1][0])
                
                (b, g, r) = input_img_black[x-2,y-2]
                (p9_b, p9_g, p9_r) = (b*kernel[1][1], g*kernel[1][1], r*kernel[1][1])
                
                (b, g, r) = input_img_black[x-2,y-1]
                (p10_b, p10_g, p10_r) = (b*kernel[1][2], g*kernel[1][2], r*kernel[1][2])
                
                (b, g, r) = input_img_black[x-2,y]
                (p11_b, p11_g, p11_r) = (b*kernel[1][3], g*kernel[1][3], r*kernel[1][3])
                
                (b, g, r) = input_img_black[x-2,y+1]
                (p12_b, p12_g, p12_r) = (b*kernel[1][4], g*kernel[1][4], r*kernel[1][4])
                
                (b, g, r) = input_img_black[x-2,y+2]
                (p13_b, p13_g, p13_r) = (b*kernel[1][5], g*kernel[1][5], r*kernel[1][5])
                
                (b, g, r) = input_img_black[x-2,y+3]
                (p14_b, p14_g, p14_r) = (b*kernel[1][6], g*kernel[1][6], r*kernel[1][6])
                
                
                #For row 3
                (b, g, r) = input_img_black[x-1,y-3]
                (p15_b, p15_g, p15_r) = (b*kernel[2][0], g*kernel[2][0], r*kernel[2][0])
                
                (b, g, r) = input_img_black[x-1,y-2]
                (p16_b, p16_g, p16_r) = (b*kernel[2][1], g*kernel[2][1], r*kernel[2][1])
                
                (b, g, r) = input_img_black[x-1,y-1]
                (p17_b, p17_g, p17_r) = (b*kernel[2][2], g*kernel[2][2], r*kernel[2][2])
                
                (b, g, r) = input_img_black[x-1,y]
                (p18_b, p18_g, p18_r) = (b*kernel[2][3], g*kernel[2][3], r*kernel[2][3])
                
                (b, g, r) = input_img_black[x-1,y+1]
                (p19_b, p19_g, p19_r) = (b*kernel[2][4], g*kernel[2][4], r*kernel[2][4])
                
                (b, g, r) = input_img_black[x-1,y+2]
                (p20_b, p20_g, p20_r) = (b*kernel[2][5], g*kernel[2][5], r*kernel[2][5])
                
                (b, g, r) = input_img_black[x-1,y+3]
                (p21_b, p21_g, p21_r) = (b*kernel[2][6], g*kernel[2][6], r*kernel[2][6])
                
                
                #For row 4
                (b, g, r) = input_img_black[x,y-3]
                (p22_b, p22_g, p22_r) = (b*kernel[3][0], g*kernel[3][0], r*kernel[3][0])
                
                (b, g, r) = input_img_black[x,y-2]
                (p23_b, p23_g, p23_r) = (b*kernel[3][1], g*kernel[3][1], r*kernel[3][1])
                
                (b, g, r) = input_img_black[x,y-1]
                (p24_b, p24_g, p24_r) = (b*kernel[3][2], g*kernel[3][2], r*kernel[3][2])
                
                (b, g, r) = input_img_black[x,y]
                (p25_b, p25_g, p25_r) = (b*kernel[3][3], g*kernel[3][3], r*kernel[3][3])
                
                (b, g, r) = input_img_black[x,y+1]
                (p26_b, p26_g, p26_r) = (b*kernel[3][4], g*kernel[3][4], r*kernel[3][4])
                
                (b, g, r) = input_img_black[x,y+2]
                (p27_b, p27_g, p27_r) = (b*kernel[3][5], g*kernel[3][5], r*kernel[3][5])
                
                (b, g, r) = input_img_black[x,y+3]
                (p28_b, p28_g, p28_r) = (b*kernel[3][6], g*kernel[3][6], r*kernel[3][6])
                
                
                #For row 5
                (b, g, r) = input_img_black[x+1,y-3]
                (p29_b, p29_g, p29_r) = (b*kernel[4][0], g*kernel[4][0], r*kernel[4][0])
                
                (b, g, r) = input_img_black[x+1,y-2]
                (p30_b, p30_g, p30_r) = (b*kernel[4][1], g*kernel[4][1], r*kernel[4][1])
                
                (b, g, r) = input_img_black[x+1,y-1]
                (p31_b, p31_g, p31_r) = (b*kernel[4][2], g*kernel[4][2], r*kernel[4][2])
                
                (b, g, r) = input_img_black[x+1,y]
                (p32_b, p32_g, p32_r) = (b*kernel[4][3], g*kernel[4][3], r*kernel[4][3])
                
                (b, g, r) = input_img_black[x+1,y+1]
                (p33_b, p33_g, p33_r) = (b*kernel[4][4], g*kernel[4][4], r*kernel[4][4])

                (b, g, r) = input_img_black[x+1,y+2]
                (p34_b, p34_g, p34_r) = (b*kernel[4][5], g*kernel[4][5], r*kernel[4][5])
                
                (b, g, r) = input_img_black[x+1,y+3]
                (p35_b, p35_g, p35_r) = (b*kernel[4][6], g*kernel[4][6], r*kernel[4][6])
                
                
                #For row 6
                (b, g, r) = input_img_black[x+2,y-3]
                (p36_b, p36_g, p36_r) = (b*kernel[5][0], g*kernel[5][0], r*kernel[5][0])
                
                (b, g, r) = input_img_black[x+2,y-2]
                (p37_b, p37_g, p37_r) = (b*kernel[5][1], g*kernel[5][1], r*kernel[5][1])
                
                (b, g, r) = input_img_black[x+2,y-1]
                (p38_b, p38_g, p38_r) = (b*kernel[5][2], g*kernel[5][2], r*kernel[5][2])
                
                (b, g, r) = input_img_black[x+2,y]
                (p39_b, p39_g, p39_r) = (b*kernel[5][3], g*kernel[5][3], r*kernel[5][3])
                
                (b, g, r) = input_img_black[x+2,y+1]
                (p40_b, p40_g, p40_r) = (b*kernel[5][4], g*kernel[5][4], r*kernel[5][4])

                (b, g, r) = input_img_black[x+2,y+2]
                (p41_b, p41_g, p41_r) = (b*kernel[5][5], g*kernel[5][5], r*kernel[5][5])
                
                (b, g, r) = input_img_black[x+2,y+3]
                (p42_b, p42_g, p42_r) = (b*kernel[5][6], g*kernel[5][6], r*kernel[5][6])
                
                
                #For row 7
                (b, g, r) = input_img_black[x+3,y-3]
                (p43_b, p43_g, p43_r) = (b*kernel[6][0], g*kernel[6][0], r*kernel[6][0])
                
                (b, g, r) = input_img_black[x+3,y-2]
                (p44_b, p44_g, p44_r) = (b*kernel[6][1], g*kernel[6][1], r*kernel[6][1])
                
                (b, g, r) = input_img_black[x+3,y-1]
                (p45_b, p45_g, p45_r) = (b*kernel[6][2], g*kernel[6][2], r*kernel[6][2])
                
                (b, g, r) = input_img_black[x+3,y]
                (p46_b, p46_g, p46_r) = (b*kernel[6][3], g*kernel[6][3], r*kernel[6][3])
            
                (b, g, r) = input_img_black[x+3,y+1]
                (p47_b, p47_g, p47_r) = (b*kernel[6][4], g*kernel[6][4], r*kernel[6][4])

                (b, g, r) = input_img_black[x+3,y+2]
                (p48_b, p48_g, p48_r) = (b*kernel[6][5], g*kernel[6][5], r*kernel[6][5])
                
                (b, g, r) = input_img_black[x+3,y+3]
                (p49_b, p49_g, p49_r) = (b*kernel[6][6], g*kernel[6][6], r*kernel[6][6])
                
                
                #Summation of convolution 
                (p_result_b, p_result_g, p_result_r) = (p1_b+p2_b+p3_b+p4_b+p5_b+p6_b+p7_b+p8_b+p9_b+p10_b\
                                                        +p11_b+p12_b+p12_b+p14_b+p15_b+p16_b+p17_b+p18_b+p19_b+p20_b\
                                                        +p21_b+p22_b+p23_b+p24_b+p25_b+p26_b+p27_b+p28_b+p29_b+p30_b\
                                                        +p31_b+p32_b+p33_b+p34_b+p35_b+p36_b+p37_b+p38_b+p39_b+p40_b
                                                        +p41_b+p42_b+p43_b+p44_b+p45_b+p46_b+p47_b+p48_b+p49_b),\
                                                        (p1_g+p2_g+p3_g+p4_g+p5_g+p6_g+p7_g+p8_g+p9_g+p10_g\
                                                        +p11_g+p12_g+p12_g+p14_g+p15_g+p16_g+p17_g+p18_g+p19_g\
                                                        +p20_g+p21_g+p22_g+p23_g+p24_g+p25_g+p26_g+p27_g+p28_g+p29_g+p30_g\
                                                        +p31_g+p32_g+p33_g+p34_g+p35_g+p36_g+p37_g+p38_g+p39_g+p40_g
                                                        +p41_g+p42_g+p43_g+p44_g+p45_g+p46_g+p47_g+p48_g+p49_g),\
                                                        (p1_r+p2_r+p3_r+p4_r+p5_r+p6_r+p7_r+p8_r+p9_r+p10_r\
                                                        +p11_r+p12_r+p12_r+p14_r+p15_r+p16_r+p17_r+p18_r+p19_r+p20_r\
                                                        +p21_r+p22_r+p23_r+p24_r+p25_r+p26_r+p27_r+p28_r+p29_r+p30_r\
                                                        +p31_r+p32_r+p33_r+p34_r+p35_r+p36_r+p37_r+p38_r+p39_r+p40_r
                                                        +p41_r+p42_r+p43_r+p44_r+p45_r+p46_r+p47_r+p48_r+p49_r)
                
                #Divide the result with total of kernel elements
                (p_result_b, p_result_g, p_result_r) = (p_result_b/kernel_total, p_result_g/kernel_total,\
                                                        p_result_r/kernel_total)
                
                #Transfer result onto image
                if(x>=0 and y>=0 and x<output_img.shape[0]+3 and y<output_img.shape[1]+3):
                    output_img[i][j] = (p_result_b, p_result_g, p_result_r)
    
    return output_img

#kernels
k =[[0,0,0],[0,1,0],[0,0,0]]
Spatial_kernel =[[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]
kernel_A = [[1,2,1],[2,4,2],[1,2,1]]
kernel_B = [[1,1,0],[1,-4,1],[0,1,0]]

#Testing(2b)
image = cv2.imread('car-1.jpg')
convo_image = ICV_convolute_img(image,Spatial_kernel)
cv2.imshow('image', convo_image)
cv2.waitKey(0)

#Testing(2c)
image = cv2.imread('car-1.jpg')
convo_image = ICV_convolute_img(image,kernel_A)
cv2.imshow('image', convo_image)
cv2.waitKey(0)

image = cv2.imread('car-1.jpg')
convo_image = ICV_convolute_img(image,kernel_B)
cv2.imshow('image', convo_image)
cv2.waitKey(0)

#Testing(2d)
#(i)
image = cv2.imread('car-1.jpg')
convo_image = ICV_convolute_img(image,kernel_A)
convo_image2 = ICV_convolute_img(convo_image,kernel_A)
cv2.imshow('image', convo_image2)
cv2.waitKey(0)

#(ii)
image = cv2.imread('car-1.jpg')
convo_image = ICV_convolute_img(image,kernel_A)
convo_image2 = ICV_convolute_img(convo_image,kernel_B)
cv2.imshow('image', convo_image2)
cv2.waitKey(0)

#(iii)
image = cv2.imread('car-1.jpg')
convo_image = ICV_convolute_img(image,kernel_B)
convo_image2 = ICV_convolute_img(convo_image,kernel_A)
cv2.imshow('image', convo_image2)
cv2.waitKey(0) 
