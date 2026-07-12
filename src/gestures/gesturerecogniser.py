class GestureRecogniser:

    def __init__(self):
        self.previous_x = None

    def is_only_index_extended(self, hand_landmarks):
        landmarks = hand_landmarks.landmark

        index_extended = landmarks[8].y < landmarks[6].y
        middle_folded = landmarks[12].y > landmarks[10].y
        ring_folded = landmarks[16].y > landmarks[14].y
        pinky_folded = landmarks[20].y > landmarks[18].y

        return (
            index_extended
            and middle_folded
            and ring_folded
            and pinky_folded
        )

    def recognise(self, results):
        threshold = 0.08

        if not results.multi_hand_landmarks:
            self.previous_x = None
            return

        hand_landmarks = results.multi_hand_landmarks[0]

        if not self.is_only_index_extended(hand_landmarks):
            self.previous_x = None
            return

        current_x = hand_landmarks.landmark[8].x

        if self.previous_x is None:
            self.previous_x = current_x
            return

        difference = current_x - self.previous_x

        if difference > threshold:
            print("Swipe right")

        elif difference < -threshold:
            print("Swipe left")

        self.previous_x = current_x