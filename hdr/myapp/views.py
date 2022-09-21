from pickle import GET
from urllib import response
from urllib.robotparser import RequestRate
from django.shortcuts import render
from django.http import HttpResponse
from email.mime import image
from PIL import Image;
import tensorflow as tf
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from django.core.files.storage import FileSystemStorage
model = tf.keras.models.load_model('./MLModels/hdr.h5')

# Create your views here.

def index(request ):
    return render(request, 'index.html') 

def recognize(request):
    
    
    

    if request.method == 'POST':
        # data = request.POST
         print('yepp')
         request_file = request.FILES['file'] if 'file' in request.FILES else None
         if request_file:
            # save attached file
 
            # create a new instance of FileSystemStorage
            fs = FileSystemStorage()
            file = fs.save(request_file.name, request_file)
           
            fileurl = fs.url(file)
            print(fileurl)
            img = cv2.imread('./static/'+fileurl)
            
           
        
            IMG_SIZE = 28
           
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            resized = cv2.resize(gray, (28,28), interpolation = cv2.INTER_AREA)
            newimg1 = tf.keras.utils.normalize(resized, axis = 1)

            newimg1= np.array(newimg1).reshape(-1, IMG_SIZE, IMG_SIZE, 1)



            predictionsed1 = model.predict(newimg1)
            res = np.argmax(predictionsed1)
            print(res )
            return render(request, 'result.html', {'res': res})

        # return render(request, 'index.html') 
    return render(request, 'index2.html') 

   
# recognize()
