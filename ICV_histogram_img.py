def ICV_histogram_img(input_img):
    
    #Dict for storing of how many time each 0-255 value occur 
    histogram_blue = np.double(np.zeros(256)) 
    histogram_green = np.double(np.zeros(256))
    histogram_red = np.double(np.zeros(256))
    
    #Loop though rows(i) and columns(j) of input image
    for i in range(input_img.shape[0]):
        for j in range(input_img.shape[1]):
        
            #Store RGB value of the input image
            (b, g, r) = input_img[i,j] 
            
            # +1 to that specific pixel value in dict
            histogram_blue[b] = histogram_blue[b]+1
            histogram_green[g] = histogram_green[g]+1
            histogram_red[r] = histogram_red[r]+1
    
    #return dict of pixel intensity frequency for RGB
    return histogram_blue, histogram_green, histogram_red

#Testing
image = cv2.imread('car-1.jpg')
hist_blue, hist_green, hist_red = ICV_histogram_img(image)
