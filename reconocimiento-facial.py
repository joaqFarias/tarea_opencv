import cv2
import sys

print("Hola, este es un programa para deteccion de rostros\n")

otra_accion = True

while otra_accion == True:
    print(f"Escriba 'i' para detectar rostros en imagen o escriba 'w' para detectar rostros con WebCam.")
    print("Su opcion:  ?")
    opcion = input()

    if opcion == "i":
        # se toma la ruta de la imagen
        #imagePath = sys.argv[1]
        print("Por favor, ingrese la ruta la imagen: ?")
        imagePath = input()
        cascPath = "haarcascade_frontalface_default.xml"

        # se crea el clasificador de cascada con descriptores de HAAR como objeto
        faceCascade = cv2.CascadeClassifier(cascPath)

        # se lee imagen y se pasa a escala de grises
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # se detectan las caras en la imagen
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
            #flags = cv2.CV_HAAR_SCALE_IMAGE
        )

        print("Se encontraron {0} caras!".format(len(faces)))

        #  Se dibuja bounding box
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Caras encontradas", image)
        cv2.waitKey(0)
        
        print("¿Desea otra occion? (s/n)")
        resp = input()
        if resp == "s":
            otra_accion = True
        elif resp == "n":
            otra_accion = False

    elif opcion == "w":
        # reconocimiento con WebCam
        cap = cv2.VideoCapture(0)

        # se crea el clasificador de cascada con descriptores de HAAR como objeto
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        while(True):
	        # se hace la captura frame por frame
	        ret, frame = cap.read()

	        # se hace la funcion a la que sera sometido cada frame
	        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	        # se detectan las caras en el frame
	        faces = faceCascade.detectMultiScale(
		        gray,
		        scaleFactor=1.1,
		        minNeighbors=5,
		        minSize=(30, 30)
		        #flags = cv2.CV_HAAR_SCALE_IMAGE
	        )   

	        print("Se encontraron {0} caras!".format(len(faces)))

	        # Se dibuja bounding box
	        for (x, y, w, h) in faces:
	    	    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	        # se muestra el resultado
	        cv2.imshow('frame', frame)
	        if cv2.waitKey(1) & 0xFF == ord('q'):
		        break

        # Cuando todo este hecho, acaba la captura y cierra la ventana
        cap.release()
        cv2.destroyAllWindows()
        
        print("¿Desea otra occion? (s/n)")
        resp = input()
        if resp == "s":
            otra_accion = True
        elif resp == "n":
            otra_accion = False
        
    else:
        print("Ingrese opcion valida.")
        