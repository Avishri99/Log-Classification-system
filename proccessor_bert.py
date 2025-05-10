from sentence_transformers import SentenceTransformer
import joblib
import numpy as np

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the saved classifier
classifier = joblib.load('models/log_classifier.joblib')


def classify_with_bert(log_messages):

    # Encode the log messages
    embeddings = model.encode(log_messages)
    probababilities = classifier.predict_proba([embeddings])[0]
    if max(probababilities) < 0.5:
        return "Unknown"
    # Classify the log messages
    predictions = classifier.predict([embeddings])[0]

    return predictions

if __name__ == "__main__":
    # Test the function
    log_messages = [
    "Server 18 went offline unexpectedly during data parsing.",
    "Critical failure found in main application component.",
    "Unauthorized user 2968 tried to access restricted API.",
    "Module X failed to process input due to formatting error.",
    "Server 36 faced an unanticipated shutdown during data upload.",
    "Unrecoverable issue found in vital application module.",
    "Detection of multiple disk faults in RAID setup.",
    "Essential system part malfunction: part ID Component97.",
    "Warning: IP 192.168.151.28 may be compromised.",
    "Potential security risk from 192.168.81.123 identified.",
    "Hey bro chill"
    ]

    for log in log_messages:
        label = classify_with_bert(log)
        print(log, "->", label)
