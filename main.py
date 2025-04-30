from flask import Flask, jsonify
import cv2
import face_recognition
import os
from datetime import datetime

app = Flask(__name__)

AUTHORIZED_FACE_ENCODING = None  # Load your authorized face encoding here

# Directory to store unknown face images
UNKNOWN_FACES_DIR = "unknown_faces"
os.makedirs(UNKNOWN_FACES_DIR, exist_ok=True)

def load_authorized_face():
    global AUTHORIZED_FACE_ENCODING
    image = face_recognition.load_image_file("atreya.jpg")  # Replace with your image
    AUTHORIZED_FACE_ENCODING = face_recognition.face_encodings(image)[0]

def save_unknown_face(frame):
    """Save the frame with unknown face as an image file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(UNKNOWN_FACES_DIR, f"unknown_face_{timestamp}.jpg")
    cv2.imwrite(filename, frame)

@app.route("/face_unlock", methods=["POST"])
def face_unlock():
    cap = cv2.VideoCapture(0)
    success, frame = cap.read()
    cap.release()

    if not success:
        return jsonify({"status": "ERROR"})

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([AUTHORIZED_FACE_ENCODING], face_encoding)
        if True in matches:
            return jsonify({"status": "SUCCESS"})

    # If no matches found, capture and save the unknown face
    save_unknown_face(frame)
    return jsonify({"status": "FAILURE"})

if __name__ == "__main__":
    load_authorized_face()
    app.run(host="0.0.0.0", port=5000)
