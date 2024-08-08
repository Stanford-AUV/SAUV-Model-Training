import cv2
import os
import glob
import os
# Path to the AVI file
path = "/home/nvidia/Downloads/buoy/"
avi_files = glob.glob(os.path.join(path, '*.avi'))


for avi_file in avi_files:
    outdir = os.path.splitext(os.path.basename(avi_file))[0]

    # Directory to save frames
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # Open the video file
    cap = cv2.VideoCapture(avi_file)

    # Check if the video file opened successfully
    if not cap.isOpened():
        print(f'Error opening video file: {avi_file}')
    else:
        frame_number = 0

        # Loop through the video frames
        while True:
            ret, frame = cap.read()
        
            # Break the loop if no frames are left
            if not ret:
                break

            if frame_number % 30 == 0:
                # Construct the filename for the frame
                frame_filename = os.path.join(outdir, f'1722486543_{frame_number}.jpg')

                # Save the frame as an image file
                cv2.imwrite(frame_filename, frame)
                
                print(f'Saved {frame_filename}')
                # Increment the frame number
            frame_number += 1

        print(outdir, frame_number)
    # Release the video capture object
    cap.release()
    print('All frames saved.')
