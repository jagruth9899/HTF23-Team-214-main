# pip install cmake
# pip install face_recognition
# pip install opencv-python


import face_recognition
import cv2
import numpy as np
import csv

from datetime import datetime
video_capture = cv2.VideoCapture(0)

# load known faces

srk_image = face_recognition.load_image_file("C:/Users/gangareddy/Downloads/face-recogniton-attendance-system-main/face-recogniton-attendance-system-main/FaceRecognitionAttendanceSystem/recogized_faces/srk.jpg")
srk_encoding = face_recognition.face_encodings(srk_image)[0]

salman_image = face_recognition.load_image_file("C:/Users/gangareddy/Downloads/face-recogniton-attendance-system-main/face-recogniton-attendance-system-main/FaceRecognitionAttendanceSystem/recogized_faces/Salman.jpg")
salman_encoding = face_recognition.face_encodings(salman_image)[0]

jag_image = face_recognition.load_image_file("C:/Users/gangareddy/Downloads/face-recogniton-attendance-system-main/face-recogniton-attendance-system-main/FaceRecognitionAttendanceSystem/recogized_faces/jag.jpg")
jag_encoding = face_recognition.face_encodings(jag_image)[0]

tus_image = face_recognition.load_image_file("C:/Users/gangareddy/Downloads/face-recogniton-attendance-system-main/face-recogniton-attendance-system-main/FaceRecognitionAttendanceSystem/recogized_faces/tus.jpg")
tus_encoding = face_recognition.face_encodings(tus_image)[0]

sam_altman_image = face_recognition.load_image_file("C:/Users/gangareddy/Downloads/face-recogniton-attendance-system-main/face-recogniton-attendance-system-main/FaceRecognitionAttendanceSystem/recogized_faces/samaltman.jpeg")
sam_altman_encoding = face_recognition.face_encodings(sam_altman_image)[0]

sundar_image = face_recognition.load_image_file("C:/Users/gangareddy/Downloads/face-recogniton-attendance-system-main/face-recogniton-attendance-system-main/FaceRecognitionAttendanceSystem/recogized_faces/sundar_pichai.jpeg")
sundar_encoding = face_recognition.face_encodings(sundar_image)[0]

elon_image = face_recognition.load_image_file("C:/Users/gangareddy/Downloads/face-recogniton-attendance-system-main/face-recogniton-attendance-system-main/FaceRecognitionAttendanceSystem/recogized_faces/elon_musk.jpeg")
elon_encoding = face_recognition.face_encodings(elon_image)[0]

known_face_encodings = [srk_encoding, salman_encoding, jag_encoding, tus_encoding,sam_altman_encoding,sundar_encoding,elon_encoding]
known_face_names = ["srk", "salman", "jagruth", "tushar","sam_altman","sundar","elon_musk"]

# list of students
students = known_face_names.copy()

face_locations = []
face_encodings =[]

# getting current date and time

now = datetime.now()
current_date = now.strftime("%d-%m-%y")

f = open(f'{current_date}', 'w+', newline="")
lnwriter = csv.writer(f)

while True :
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognizing faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)

        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        # add text if the person is present
            if name in known_face_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCorner = (10, 100)
                fontScale = 1.5
                fontColor = (0, 0, 222)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name+" present", bottomLeftCorner, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])
    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows()
f.close()