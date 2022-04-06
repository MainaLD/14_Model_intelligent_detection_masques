import numpy as np
import cv2
import matplotlib.pyplot as plt

liste_label = ['sans masque', 'avec masque']

def appli_tps_reel(loaded_model):
    # definie un objet de capture vidéo
    vid = cv2.VideoCapture(0)

    # Condition/boucle while que tant que la viéo capture
    while(True):
        # Capturer l'image vidéo
        # par cadre
        ret, frame = vid.read()
        
        imgr = cv2.resize(frame,(224,224), interpolation = cv2.INTER_AREA)
        img_exp = np.expand_dims(np.array(imgr)/255.0, axis=0)

        prediction = loaded_model.predict(img_exp)
        resultat = liste_label[np.argmax(prediction)]

        image_pred = cv2.putText(frame, resultat, (120, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255,0,0))
    
        # Affiche le résultat
        cv2.imshow('frame', image_pred)
        
        # the 'q' button is set as the, 
        # quitting button you may use any desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()