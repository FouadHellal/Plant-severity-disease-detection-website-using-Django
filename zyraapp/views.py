from django.shortcuts import render
from .forms import UploadImageForm
from .utils import load_and_prepare_image
from .utils import load_and_prepare_image,create_mask
import cv2
import numpy as np
from .models import UploadedImage
from django.conf import settings
from tensorflow.keras.models import load_model
from rembg import remove
model = load_model('zyraapp/modelunetcoffee.h5')
import os
TF_ENABLE_ONEDNN_OPTS=0

from django.shortcuts import render
from django.http import HttpResponse
import google.generativeai as genai
API_KEY='AIzaSyD408QlleK4lAcTCZcU3kKzPWmIuC30oRI'

def chat_view(request):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    #instruction = 'explain like you are a scientist and i am a scientist '

    if request.method == 'POST':
        question = request.POST.get('question')
        if question.strip() != '':
            response = chat.send_message(question)
            return HttpResponse(response.text)
    return render(request, 'chat.html')


def about(request):
    return render(request, 'about.html')


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Enregistrer le fichier téléchargé sur le disque
            uploaded_file = request.FILES['image']
            file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            
            with open(file_path, 'wb') as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)
            
            # Passer le chemin du fichier enregistré à la fonction remove_background
            image = cv2.imread(file_path)
            resized_image = cv2.resize(image, (224, 224))

            # Image sans background
            rgb_no_bg = remove(resized_image)
            
            # Calculer la surface de la feuille
            surface = np.sum(rgb_no_bg[:, :, 3] != 0)
            # Créer un masque pour les pixels où l'alpha est différent de zéro
            alpha_mask = (rgb_no_bg[:, :, 3] != 0)

            # Préparer l'image pour la prédiction
            image_to_predict = load_and_prepare_image(file_path)

            # Prédire le masque
            predicted_mask = model.predict(image_to_predict)[0]

            # Binariser le masque
            binarized_mask = (predicted_mask > 0.5).astype(int)

            # Calculer le nombre de pixels malades
            num_white_pixels = np.sum((binarized_mask[:,:,0] == 1) & alpha_mask[True])

            # Calculer le pourcentage de zone malade sur la surface de la feuille
            severityy = (num_white_pixels / surface) * 100
            severity = round(severityy, 1)
            print("Sévérité U-net : {:.2f}%".format(severity))
            
            # Créer le nouveau masque
            new_mask = create_mask(rgb_no_bg, binarized_mask, alpha_mask)
            
            uploaded_image = UploadedImage(image=uploaded_file, percentage=severity)
            uploaded_image.save()

            image_url = os.path.join(settings.MEDIA_URL, uploaded_file.name)
            mask_malade_url = os.path.join(settings.MEDIA_URL, 'mask_malade_' + uploaded_file.name)
            
            # Enregistrer le nouveau masque sur le disque
            cv2.imwrite(os.path.join(settings.MEDIA_ROOT, 'mask_malade_' + uploaded_file.name), new_mask)

            # Passer les données au modèle de template
            return render(request, 'upload_result.html', {'image_url': image_url,
                                                           'pourcentage_pixels_zone_malade': severity,
                                                           'mask_malade_url': mask_malade_url})
    else:
        form = UploadImageForm()
    return render(request, 'upload_form.html', {'form': form})