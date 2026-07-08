import cv2


class Camera:

    def __init__(self):
        self.capture = None

    def open(self):
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            raise RuntimeError("Could not access webcam")

    def show_feed(self):
        while True:
            ret, frame = self.capture.read()

            if not ret:
                print("Failed to read frame")
                break

            cv2.imshow("Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.release()

    def release(self):
        self.capture.release()
        cv2.destroyAllWindows()
