#Testing(3a)
cap = cv2.VideoCapture('DatasetB.avi')
clip_num_frame = round(cap.get(cv2.CAP_PROP_FRAME_COUNT))

ret, frame = cap.read()

width = frame.shape[1]*clip_num_frame

output_img = np.uint8(np.zeros((frame.shape[0], width, frame.shape[2])))
img1 = np.uint8(np.zeros((frame.shape[0], frame.shape[1], frame.shape[2])))
img2 = np.uint8(np.zeros((frame.shape[0], frame.shape[1], frame.shape[2])))

#For storing video into one long image
for i in range (0,clip_num_frame):
    ret, frame = cap.read()
    
    if ret == False:
        break
    
    for j in range(frame.shape[0]):
        for k in range(frame.shape[1]):
            
            #Put condition if x and y is in range of the input image
            if(j>=0 and k>=0 and j<frame.shape[0] and k<frame.shape[1]):
                
                    output_img[j,k+(frame.shape[1]*i),:] = frame[j,k,:]
    
    if cv2.waitKey(33)==27:
        break

#Access frame 2 in output image
num = img1.shape[1]*1
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        
        if(i>=0 and j>=0 and i<img1.shape[0] and j<img1.shape[1]):
                img1[i,j,:] = output_img[i,j+num,:]

                
#Access frame 50 in output image
num2 = img2.shape[1]*49
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        
        if(i>=0 and j>=0 and i<img2.shape[0] and j<img2.shape[1]):
                img2[i,j,:] = output_img[i,j+num2,:]
                             
#Frame 1
#call function histogram
histogram_blue, histogram_green, histogram_red = ICV_histogram_img(img1)

#check image
#cv2.imshow("image1",img1)
#cv2.waitKey(0)

#tilte ana label
plt.figure(1)
plt.xlabel('0-255')
plt.ylabel('Frequency')
plt.title('Histogram at frame 1')

#plot frame 1
plt.bar(range(len(histogram_blue)),histogram_blue, width = 1.0, color='blue', alpha = 0.5)
plt.bar(range(len(histogram_green)),histogram_green,width = 1.0, color='green', alpha = 0.5)
plt.bar(range(len(histogram_red)),histogram_red,width = 1.0, color='red', alpha = 0.5)

#Frame 2
#call function histogram
histogram_blue, histogram_green, histogram_red = ICV_histogram_img(img2)

#check image
#cv2.imshow("image2",img2)
#cv2.waitKey(0)

#tilte ana label
plt.figure(2)
plt.xlabel('0-255')
plt.ylabel('Frequency')
plt.title('Histogram at frame 50')

#plot frame 2
plt.bar(range(len(histogram_blue)),histogram_blue, width = 1.0, color='blue', alpha = 0.5)
plt.bar(range(len(histogram_green)),histogram_green,width = 1.0, color='green', alpha = 0.5)
plt.bar(range(len(histogram_red)),histogram_red,width = 1.0, color='red', alpha = 0.5)
