import cv2
import numpy as np
# import matplotlib.pyplot as plt

# img = cv2.imread('sample-frame.png')
# img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB) #convert it to RGB channel

def main():
    video_path = "test.mp4"
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    ave_image = np.zeros((100, 100, 3), np.uint8)

    while True:
        ret, frame = cap.read()

        if not ret:
            cap.release()
            cap = cv2.VideoCapture(video_path)  # Reset to the beginning of the video
            continue

        cv2.imshow("Video", frame)
        crop_img = frame[375:400, 145:170] #crop the image
        cv2.imshow("Cropped Frame", crop_img)

        mean_px = np.mean(crop_img, axis=(0,1)) #calculate the mean of the image
        # /print(mean_px)

        ave_image[:] = mean_px
        cv2.imshow("Frame Activity", ave_image)        

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

# cv2.imshow("Current Frame", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

