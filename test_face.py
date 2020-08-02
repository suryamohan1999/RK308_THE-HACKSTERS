import cv2
import face_recognition
import os

Allowed_extensions = {'png', 'jpg', 'jpeg'}

def face_rec(k_i, uk_i):
    match = False

    if os.path.splitext(k_i)[1][1:] and os.path.splitext(uk_i)[1][1:] in Allowed_extensions:

        result_list = []

        def face_count(image):
            original_image = cv2.imread(image)
            face_classifier = cv2.CascadeClassifier("haar-face.xml")
            gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            no_face = len(list(faces))
            #print(no_face)
            return no_face

        known_image = face_recognition.load_image_file(k_i)
        unknown_image = face_recognition.load_image_file(uk_i)

        for i in range(0, face_count(k_i)):
            biden_encoding = face_recognition.face_encodings(known_image)[i]
            try:
                # locations=face_recognition.face_locations(unknown_image,model="hog")  #hog or cnn
                unknown_encodings = face_recognition.face_encodings(unknown_image)  # ,locations
                results = face_recognition.compare_faces(biden_encoding, unknown_encodings)
                for j in results:
                    result_list.append(j)
            except Exception as e:
                result_list.append(False)
                #print("error occured in recognizing")
                #print(e)

        print(result_list)
        if True in result_list:
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
