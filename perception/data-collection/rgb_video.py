#!/usr/bin/env python3

import cv2
import depthai as dai

# Create pipeline
pipeline = dai.Pipeline()

# Define source and output
camRgb = pipeline.create(dai.node.ColorCamera)
xoutVideo = pipeline.create(dai.node.XLinkOut)

xoutVideo.setStreamName("video")

# Properties
camRgb.setBoardSocket(dai.CameraBoardSocket.CAM_A)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)

frame_w=1920
frame_h=1080

size = (frame_w, frame_h) 
camRgb.setVideoSize(frame_w, frame_h)

import datetime
filename = f"{int(datetime.datetime.now().timestamp())}.avi"

result = cv2.VideoWriter(f"/workspace/videos/{filename}",  
                         cv2.VideoWriter_fourcc(*'MJPG'), 
                         10, size) 

xoutVideo.input.setBlocking(False)
xoutVideo.input.setQueueSize(1)

# Linking
camRgb.video.link(xoutVideo.input)

# Connect to device and start pipeline
with dai.Device(pipeline) as device:

    video = device.getOutputQueue(name="video", maxSize=1, blocking=False)

    while True:
        videoIn = video.get()

        # Get BGR frame from NV12 encoded video frame to show with opencv
        # Visualizing the frame on slower hosts might have overhead
        frame = videoIn.getCvFrame()
        cv2.imshow("video", frame)
        result.write(frame)

        if cv2.waitKey(1) == ord('q'):
            break
result.release() 
    
# Closes all the frames 
cv2.destroyAllWindows() 
   
print(f"The video was successfully saved to {filename}") 
