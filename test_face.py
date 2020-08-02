import cv2
import face_recognition
import os

Allowed_extensions = {'png', 'jpg', 'jpeg'}

def face_rec(k_i, uk_i):
    match = False
    if os.path.splitext(uk_i)[1][1:] in Allowed_extensions:

        known_image = face_recognition.load_image_file(k_i)
        unknown_image = face_recognition.load_image_file(uk_i)
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        try:
            unknown_encodings = face_recognition.face_encodings(unknown_image)
            results = face_recognition.compare_faces(biden_encoding,unknown_encodings)
        except:
            results = [False]
        if True in results:
            match = True
        return match
    else:
        print("not allowed extension")
        return match


#print(face_rec("dual2.jpg", "test2.txt"))



def face_detect(image):
    if os.path.splitext(image)[1][1:] in Allowed_extensions:
        original_image = cv2.imread(image)
        face_classifier=cv2.CascadeClassifier("haar-face.xml")
        gray=cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        faces=face_classifier.detectMultiScale(gray,1.3,5)
        no_face=len(list(faces))
        if no_face==0:
            return False
        else:
            return True
    else :
        print("not allowed extension")
        return False
#print(face_detect("test.txt"))
