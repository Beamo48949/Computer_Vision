def ICV_hist_intersection(hist_blue1, hist_green1, hist_red1, hist_blue2, hist_green2, hist_red2):
    
    min_blue = np.double(np.zeros(256))
    min_green = np.double(np.zeros(256))
    min_red = np.double(np.zeros(256))
    
    #Find intersection between two histogram
    for i in range(0,256):
        if(hist_blue1[i]<=hist_blue2[i]):
            min_blue[i] = hist_blue1[i]
        else:
            min_blue[i] = hist_blue2[i]
            
    for i in range(0,256):
        if(hist_green1[i]<=hist_green2[i]):
            min_green[i] = hist_green1[i]
        else:
            min_green[i] = hist_green2[i]
            
    for i in range(0,256):
        if(hist_red1[i]<=hist_red2[i]):
            min_red[i] = hist_red1[i]
        else:
            min_red[i] = hist_red2[i]
    
    #Summation of intersection individual RGB
    total_blue = np.sum(min_blue)
    total_green = np.sum(min_green)
    total_red = np.sum(min_red)    
    
    return total_blue, total_green, total_red, min_blue, min_green, min_red
