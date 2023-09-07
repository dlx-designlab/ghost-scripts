import cv2
import numpy as np
# import matplotlib.pyplot as plt

# img = cv2.imread('sample-frame.png')
# img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB) #convert it to RGB channel



def main():
    aoes = [[375,400,145,170]] #areas of interest
    # electrodes_data = []
    
    video_path = "test.mp4"
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    ave_image = np.zeros((10, 10, 3), np.uint8)
    electrodes_values = np.zeros((10,10,3), np.uint8)
    hist = np.zeros((10, 10, 3), np.uint8)
    hist[:] = [0,255,0]

    while True:
        ret, frame = cap.read()

        # Loop back to the beginning of the video file when video ends
        if not ret:
            break
            # cap.release()
            # cap = cv2.VideoCapture(video_path)  # Reset to the beginning of the video
            # continue
        

        for aoe in aoes:
            # crop frame around the AOE
            crop_img = frame[aoe[0]:aoe[1], aoe[2]:aoe[3]] #crop the image

            # get average pixel color
            mean_px = np.mean(crop_img, axis=(0,1)) #calculate the mean of the image
            # electrodes_data.append(mean_px)
            
            ave_image[:] = mean_px
            electrodes_values = np.concatenate((electrodes_values, ave_image), axis=1)
            hist = np.concatenate((hist, ave_image), axis=1)
            # print(mean_px)

            # Draw a rechtange around the AOE
            frame = cv2.rectangle(frame, (aoe[2], aoe[0]), (aoe[3], aoe[1]), (0, 255, 0), 1)
            
            cv2.imshow("Frame Activity", ave_image)
            cv2.imshow("Cropped Frame", crop_img)
        
        # show all the frames
        cv2.imshow("Video", frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # print(electrodes_data)
    cv2.imshow("Histogram", hist)
    cap.release()
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

# cv2.imshow("Current Frame", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

