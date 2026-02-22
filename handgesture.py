# handgesture.py

import cv2
import mediapipe as mp
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class GestureVolumeController:
    def __init__(self, det_conf=0.7, trk_conf=0.7, max_hands=1):

        # MediaPipe setup
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=det_conf,
            min_tracking_confidence=trk_conf
        )

        # Audio setup
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        self.volume_ctrl = cast(interface, POINTER(IAudioEndpointVolume))
        self.min_vol, self.max_vol = self.volume_ctrl.GetVolumeRange()[:2]

    def process_frame(self, frame):
        """
        Process a single video frame.
        Returns: processed_frame, volume_percent, hand_detected
        """
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        volume_percent = None
        hand_detected = False

        if results.multi_hand_landmarks:
            hand_detected = True
            hand = results.multi_hand_landmarks[0]

            h, w, _ = frame.shape
            lm = [(int(p.x * w), int(p.y * h)) for p in hand.landmark]

            # Thumb tip & Index tip
            x1, y1 = lm[4]
            x2, y2 = lm[8]

            # Distance
            distance = np.hypot(x2 - x1, y2 - y1)
            distance = np.clip(distance, 40, 180)

            # Map distance to system volume
            vol = np.interp(distance, [40, 180], [self.min_vol, self.max_vol])
            self.volume_ctrl.SetMasterVolumeLevel(vol, None)

            volume_percent = int(np.interp(distance, [40, 180], [0, 100]))

            # Draw visuals
            self.mp_draw.draw_landmarks(
                frame, hand, self.mp_hands.HAND_CONNECTIONS
            )
            cv2.circle(frame, (x1, y1), 10, (255, 0, 255), -1)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 255), -1)
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

        return frame, volume_percent, hand_detected