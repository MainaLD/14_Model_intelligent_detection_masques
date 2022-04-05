# Model_Intelligent_detection_masques
Transfer learning (VGG16) pour la détection des masques


## Contexte du projet
Ce brief a pour objectif d’appliquer le Transfer Learning sur une base de données.
Dans ce brief, nous appliquons un apprentissage supervisé pour identifier si la personne porte un masque.

**************************************************************************************************************
**Challenges**
- Manipulation des images.
- Analyse, prétraitement et visualisation des images.
- Manipulation et l’exploitation de la Bibliothèque Tensorflow.
- Charger un modèle CNN à partir de Tensorflow.
- Appliquer le Transfer Learning (sur VGG16).
- Faire des tests à partir de la webcam


**************************************************************************************************************
## Documents dans ce GitHub :
### 1 notebook Model_detection_Model_CNN.ipynb :
pour définir le meilleur modèle de CNN en appliquant le transfer learning (VGG16), et en sauvegardant le meilleur modèle *.h5

### 1 notebook Model_detection_Appli_detection.ipynb :
qui contient 3 type de détection, après avoir chargé le meilleur model :
- détection sur 1 image
- détection sur plusieurs images
- détction avec la webcam
le tout en affichant sur l'image ou la vidéo si la personne porte un masque ou non

### le rapport *.pdf :
qui documente et explique les différentes étapes du notebook

### le dossier images test,
pour la détection des masques

### le dossiers ggdrive [à télécharger](https://drive.google.com/drive/folders/1C9Yq25lcc4nKPqkkK4NYR8eefvlwho7S?usp=sharing) :
- **dossier Mask_Data** contenant le jeu d'images
- **model_mask.h5** : sauvegarde du meilleur modèle








