IMG_SIZE = 28
    print('mirza')
    print(img)
    print('mirza')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28,28), interpolation = cv2.INTER_AREA)
    newimg1 = tf.keras.utils.normalize(resized, axis = 1)

    newimg1= np.array(newimg1).reshape(-1, IMG_SIZE, IMG_SIZE, 1)



    predictionsed1 = model.predict(newimg1)
    res = np.argmax(predictionsed1)
    print(res )