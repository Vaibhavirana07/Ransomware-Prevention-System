import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)

    def train(self, data):
        self.model.fit(data)

    def predict(self, data):
        return self.model.predict(data)

# Example usage
if __name__ == "__main__":
    detector = AnomalyDetector()
    # Generate some training data
    normal_data = np.random.normal(0, 1, (100, 2))
    detector.train(normal_data)

    # Generate some test data
    test_data = np.random.normal(0, 1, (20, 2))
    anomalies = np.random.uniform(-5, 5, (5, 2))
    test_data = np.vstack([test_data, anomalies])

    predictions = detector.predict(test_data)
    print("Predictions:", predictions)
