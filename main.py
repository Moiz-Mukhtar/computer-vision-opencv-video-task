import cv2

# 1. Read the input video
cap = cv2.VideoCapture('video.mp4')

# Get the original video properties to ensure the output matches
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 2. Configure the output video writer
# 'mp4v' is the codec used for standard .mp4 files
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# 3. Loop through every frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break # Video has ended

    # Draw a green rectangle: image, top-left corner, bottom-right corner, color(BGR), thickness
    cv2.rectangle(frame, (50, 50), (400, 300), (0, 255, 0), 3)

    # Draw red text: image, text, bottom-left corner, font, scale, color(BGR), thickness
    cv2.putText(frame, 'Video Task Complete', (60, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Save the modified frame to the new video
    out.write(frame)

# 4. Clean up resources
cap.release()
out.release()
cv2.destroyAllWindows()
print("Video processing complete. Check output.mp4!")