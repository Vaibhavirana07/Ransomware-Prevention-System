from encryption_module.encryption import encrypt, decrypt
from anomaly_detection_module.anomaly_detection import AnomalyDetector
from alert_system.alert import send_alert
import numpy as np
import os

def main():
    # Encryption example
    key = os.urandom(32)
    message = "Sensitive data that needs encryption"
    encrypted_message = encrypt(message, key)
    print("Encrypted:", encrypted_message)
    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted:", decrypted_message)

    # Anomaly Detection example
    detector = AnomalyDetector()
    normal_data = np.random.normal(0, 1, (100, 2))
    detector.train(normal_data)

    test_data = np.random.normal(0, 1, (20, 2))
    anomalies = np.random.uniform(-5, 5, (5, 2))
    test_data = np.vstack([test_data, anomalies])

    predictions = detector.predict(test_data)
    print("Predictions:", predictions)

    if -1 in predictions:
        try:
            send_alert("Anomaly Detected", "An anomaly was detected in the system.", "recipient@example.com")
        except Exception as e:
            print("Error sending alert:", e)

if __name__ == "__main__":
    main()
