import cv2
from openvino.runtime import Core
import numpy as np

# Define the paths to the model files
model_xml_path = "resources/models/person-vehicle-bike-detection-crossroad-1016.xml"
model_bin_path = "resources/models/person-vehicle-bike-detection-crossroad-1016.bin"

# Initialize the Inference Engine and load the model
ie = Core()
device = "MYRIAD"
model = ie.read_model(model=model_xml_path)
compiled_model = ie.compile_model(model=model, device_name=device)

# Get the input and output layers of the model
input_layer_ir = compiled_model.input(0)
output_layer_ir = compiled_model.output(0)

# Open the video file
cap = cv2.VideoCapture("resources/videos/crosswalk.gif")

# Initialize the FPS counter
fps_start_time = cv2.getTickCount()
fps_frame_count = 0
fps_text = ""

while True:
    # Read the next frame from the video file
    ret, frame = cap.read()
    if not ret:
        break
    
    # Preprocess the frame for inference
    N, C, H, W = input_layer_ir.shape
    resized_frame = cv2.resize(frame, (W, H))
    input_frame = np.expand_dims(resized_frame.transpose(2, 0, 1), 0)
    
    # Perform inference on the frame
    result = compiled_model.infer_new_request({0: input_frame})
    prediction = next(iter(result.values()))

    # Draw bounding boxes around the detected objects
    color = (0, 255, 0)  # Green
    thickness = 2
    for pred in prediction[0][0]:
        _, _, conf, x_min, y_min, x_max, y_max = pred
        x_min = int(x_min * frame.shape[1])
        y_min = int(y_min * frame.shape[0])
        x_max = int(x_max * frame.shape[1])
        y_max = int(y_max * frame.shape[0])
        if (conf > 0.7):
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, thickness)

    # Calculate the FPS of the video
    fps_frame_count += 1
    if fps_frame_count == 10:
        fps_end_time = cv2.getTickCount()
        fps = cv2.getTickFrequency() / (fps_end_time - fps_start_time) * fps_frame_count
        fps_text = "FPS: {:.2f}".format(fps)
        fps_frame_count = 0
        fps_start_time = fps_end_time

    # Draw the FPS text on the frame
    cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video file and close all windows
cap.release()
cv2.destroyAllWindows()