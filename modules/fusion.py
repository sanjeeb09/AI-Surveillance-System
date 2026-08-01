from filterpy.kalman import KalmanFilter
import numpy as np


class SensorFusion:
    def __init__(self):
        self.kf = KalmanFilter(dim_x=1, dim_z=1)

        # State
        self.kf.x = np.array([[0.0]])

        # State transition
        self.kf.F = np.array([[1]])

        # Measurement function
        self.kf.H = np.array([[1]])

        # Uncertainty
        self.kf.P *= 10

        # Measurement noise
        self.kf.R = 0.05

        # Process noise
        self.kf.Q = 0.01

    def update(self, visual_score, audio_score):
        measurement = (visual_score + audio_score) / 2

        self.kf.predict()
        self.kf.update(measurement)

        return float(self.kf.x[0][0])


fusion = SensorFusion()