# Ransomware Prevention System

This project demonstrates a basic ransomware prevention system by integrating encryption, anomaly detection, and alerting functionalities. The system encrypts sensitive data, detects anomalies in the data, and sends an alert if an anomaly is detected.

## Dependencies

The project requires the following dependencies:

- `numpy`
- `smtplib`
- `encryption_module`
- `anomaly_detection_module`
- `alert_system`

Ensure you have these dependencies installed. If the custom modules (`encryption_module`, `anomaly_detection_module`, `alert_system`) are not standard packages, make sure they are available in your project directory or installed appropriately.

## Installation

To install the required dependencies, run the following command:

```bash
pip install numpy
pip install pycryptodome scikit-learn
```

Note: Custom modules should be installed or available in your project directory.

## Usage

1. **Encryption Example**: Encrypts and decrypts a sensitive message.
2. **Anomaly Detection Example**: Trains an anomaly detector on normal data and predicts anomalies in test data.
3. **Alert System**: Sends an email alert if an anomaly is detected.

## How to Run

1. Clone the repository or download the source code.
2. Ensure you have the required dependencies installed.
3. Navigate to the project directory.
4. Run the main script:

```bash
python main.py
```

## Error Handling

The project includes error handling for the alert system to ensure the rest of the script executes smoothly even if an error occurs while sending the alert.

## Example Output

Running the script will output the following:

- Encrypted message
- Decrypted message
- Predictions of anomalies
- An error message if there is an issue sending the alert

## Troubleshooting

If you encounter any issues, ensure that:
- All custom modules are correctly installed or available in the project directory.
- The SMTP server details in `alert.py` are correctly configured.

For any other issues, please refer to the error messages printed by the script.
