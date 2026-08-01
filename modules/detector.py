from ultralytics import YOLO
import cv2

# Load YOLO model once
model = YOLO("yolov8n.pt")


def detect_objects(frame):
    """
    Detect only persons.
    Returns:
        annotated_frame
        person_count
        highest_confidence
    """

    results = model(frame, verbose=False)

    annotated_frame = frame.copy()

    person_count = 0
    highest_confidence = 0.0

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            # Only detect PERSON (COCO class 0)
            if cls != 0:
                continue

            confidence = float(box.conf[0])

            if confidence > highest_confidence:
                highest_confidence = confidence

            person_count += 1

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw green rectangle
            cv2.rectangle(
                annotated_frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            label = f"Person {confidence:.2f}"

            cv2.putText(
                annotated_frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    return annotated_frame, person_count, highest_confidence