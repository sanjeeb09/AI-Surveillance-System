import cv2
from datetime import datetime

from modules.detector import detect_objects
from modules.audio import get_audio_level
from modules.fusion import fusion
from modules.recorder import recorder
from modules.event_manager import event_manager
from modules.logger import log_event
from modules.alerts import send_alert


def start_camera():

    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Could not open webcam.")
        return

    print("Camera Started")
    print("Press Q to quit")

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # --------------------
        # Detection
        # --------------------

        frame, people, confidence = detect_objects(frame)

        audio = get_audio_level()

        # --------------------
        # Audio Status
        # --------------------

        if audio > 0.25:
            audio_status = "LOUD"
            audio_color = (0, 0, 255)
        else:
            audio_status = "NORMAL"
            audio_color = (0, 255, 0)

        # --------------------
        # Audio Score
        # --------------------

        if audio < 0.20:
            audio_score = 0.20
        elif audio < 0.50:
            audio_score = 0.60
        else:
            audio_score = 0.90

        # --------------------
        # Visual Score
        # --------------------

        if people == 0:
            visual_score = 0.10
        elif people == 1:
            visual_score = 0.70
        else:
            visual_score = 0.90

        # --------------------
        # Fusion
        # --------------------

        fusion_score = fusion.update(
            visual_score,
            audio_score
        )

        # --------------------
        # Event Detection
        # --------------------

        if fusion_score >= 0.75:

            system_status = "SUSPICIOUS"
            status_color = (0, 0, 255)

            if event_manager.should_trigger(fusion_score):
                recorder.start_recording(frame)

                log_event(
                    people=people,
                    confidence=confidence,
                    audio=audio,
                    fusion_score=fusion_score,
                    status="SUSPICIOUS",
                    clip=recorder.filename
                )

                send_alert(
                    people,
                    fusion_score
                )

        else:

            system_status = "SAFE"
            status_color = (0, 255, 0)

        # Continue recording if active
        recorder.update(frame)

        # --------------------
        # Draw UI
        # --------------------

        cv2.putText(
            frame,
            f"People: {people}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Confidence: {confidence:.2f}",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Audio: {audio:.2f}",
            (20, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            audio_color,
            2
        )

        cv2.putText(
            frame,
            f"Audio Status: {audio_status}",
            (20, 145),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            audio_color,
            2
        )

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        cv2.putText(
            frame,
            current_time,
            (20, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Fusion Score: {fusion_score:.2f}",
            (20, 215),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"System: {system_status}",
            (20, 250),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            status_color,
            2
        )

        # Recording indicator
        if recorder.recording:

            cv2.circle(frame, (1180, 35), 10, (0, 0, 255), -1)

            cv2.putText(
                frame,
                "REC",
                (1200, 42),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

        cv2.imshow("AI Surveillance", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()