class GestureRecogniser:

    def __init__(self):
        self.previous_x = None
        self.palm_active = False
        self.non_palm_frames = 0
        self.palm_reset_frames = 5

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

    def is_open_palm(self, hand_landmarks):
        landmarks = hand_landmarks.landmark

        return (
            landmarks[8].y < landmarks[6].y
            and landmarks[12].y < landmarks[10].y
            and landmarks[16].y < landmarks[14].y
            and landmarks[20].y < landmarks[18].y
        )

    def recognise(self, results):
        threshold = 0.08

        if not results.multi_hand_landmarks:
            self.previous_x = None

            if self.palm_active:
                self.non_palm_frames += 1

                if self.non_palm_frames >= self.palm_reset_frames:
                    self.palm_active = False
                    self.non_palm_frames = 0

            return None

        hand_landmarks = results.multi_hand_landmarks[0]

        if self.is_open_palm(hand_landmarks):
            self.previous_x = None
            self.non_palm_frames = 0

            if not self.palm_active:
                self.palm_active = True
                return "TOGGLE_PAUSE"

            return None

        if self.palm_active:
            self.non_palm_frames += 1

            if self.non_palm_frames < self.palm_reset_frames:
                return None

            self.palm_active = False
            self.non_palm_frames = 0

        if not self.is_only_index_extended(hand_landmarks):
            self.previous_x = None
            return None

        current_x = hand_landmarks.landmark[8].x

        if self.previous_x is None:
            self.previous_x = current_x
            return None

        difference = current_x - self.previous_x
        self.previous_x = current_x

        if difference > threshold:
            return "SWIPE_RIGHT"

        if difference < -threshold:
            return "SWIPE_LEFT"

        return None
