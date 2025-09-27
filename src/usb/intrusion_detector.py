import cv2
import time
import os

def record_intrusion(output_dir="intrusions", duration=5):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Webcam not accessible!")
        return None

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(output_dir, f"intrusion_{timestamp}.avi")

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))

    start_time = time.time()
    while(int(time.time() - start_time) < duration):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break

    cap.release()
    out.release()
    print(f"Intrusion recorded: {filename}")
    return filename
