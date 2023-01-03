import cv2
import time


Known_distance = 76.2

Known_width = 14.3


GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


fonts = cv2.FONT_HERSHEY_COMPLEX

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):

    
    focal_length = (width_in_rf_image * measured_distance) / real_width
    return focal_length


def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):

    distance = (real_face_width * Focal_Length)/face_width_in_frame

    
    return distance


def face_data(image):

    face_width = 0 

    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)

    for (x, y, h, w) in faces:

        cv2.rectangle(image, (x, y), (x+w, y+h), RED, 2)

        face_width = w

        

    return face_width


def coord(image):

    face_width = 0 

    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)

    for (x, y, h, w) in faces:

        cv2.rectangle(image, (x, y), (x+w, y+h), RED, 2)

        face_width = w

        print('x= ',x, "  y = ", y)


        if x<100:
            print('moving robot to the right')

        elif x>380:
            
            print('moving robot to the left')

        if y<100:
            
            print('moving camera down')

        elif y>300:
            
            print('moving camera up')


        #return x

    
    


ref_image = cv2.imread("Ref_image.png")


ref_image_face_width = face_data(ref_image)

Focal_length_found = Focal_Length_Finder(
    Known_distance, Known_width, ref_image_face_width)

print(Focal_length_found)


cap = cv2.VideoCapture(0)


while True:

    
    _, frame = cap.read()

    
    face_width_in_frame = face_data(frame)

    
    if face_width_in_frame != 0:
    
    
        Distance = Distance_finder(
            Focal_length_found, Known_width, face_width_in_frame)

        cv2.line(frame, (30, 30), (230, 30), RED, 32)
        cv2.line(frame, (30, 30), (230, 30), BLACK, 28)

        
        cv2.putText(
            frame, f"Distance: {round(Distance,2)} CM ", (30, 35),
        fonts, 0.6, WHITE, 2)

        #test
        print(Distance)

        #print("x,y= ", coord(frame))

        coord(frame)
        
    cv2.imshow("frame", frame)

    #time.sleep(0.05)

    
    if cv2.waitKey(1) == ord("q"):
        break

# closing the camera
cap.release()

# closing the windows that are opened
cv2.destroyAllWindows()
