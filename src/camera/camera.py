import cv2
from detection.handdetection import HandDetector
from gestures.gesturerecogniser import GestureRecogniser


class Camera:

    def __init__(self):
        self.capture = None
        self.detector = HandDetector()
        self.recogniser = GestureRecogniser()

    def open(self):
        self.capture = cv2.VideoCapture(0)

        if not self.capture.isOpened():
            raise RuntimeError("Could not access webcam")

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Camera", 1000, 750)

    def show_feed(self):
        while True:
            ret, frame = self.capture.read()

            if not ret:
                print("Failed to read frame")
                break

            results = self.detector.detect(frame)
            self.recogniser.recognise(results)
            frame = self.detector.draw(frame, results)

            cv2.imshow("Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.release()

    def release(self):
        if self.capture:
            self.capture.release()

        cv2.destroyAllWindows()
