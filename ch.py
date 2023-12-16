import numpy as np
import cv2
import requests
import firebase_admin
import os
import base64
from datetime import datetime
from firebase_admin import storage
from firebase_admin import db

def hello_pubsub(event, context):
    try:
        firebase_admin.get_app()
    except ValueError:
        app = firebase_admin.initialize_app(options={'databaseURL' : '<your-firebase-rtdb-url>'})
    ref = db.reference('dash')
    bucket = storage.bucket("<your-firebase-storage-bucket>")
    response = requests.get("https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0211.jpg")
    if response.status_code == 200:
        with open('/tmp/211.jpg', 'wb+') as f:
            f.write(response.content)
            f.close
            response.close
    else:
        response.close
        exit()

    gray_img = cv2.imread('/tmp/211.jpg', cv2.IMREAD_GRAYSCALE)

    def gray_cropp( image):
        maskg = np.zeros((1024, 1024), dtype=np.uint8)
        cv2.circle(maskg, (512, 512), 400, (1,1,1), -1, 1, 0)
        cropped = image*maskg
        return cropped


    def color_cropp8(image):
        maskc = np.zeros((1024, 1024, 3), dtype=np.uint8)
        cv2.circle(maskc, (512, 512), 400, (1, 1, 1), -1, 1, 0)
        cropped = image*maskc
        return cropped

    azImage = cv2.cvtColor(gray_cropp(gray_img), cv2.COLOR_GRAY2RGB)

    azImage[np.where((azImage == [0, 0, 0]).all(axis=2))] = [0, 0, 255]
    azImage[np.where((azImage == [1, 1, 1]).all(axis=2))] = [0, 0, 255]
    azImage[np.where((azImage == [2, 2, 2]).all(axis=2))] = [0, 0, 255]
    azImage[np.where((azImage == [3, 3, 3]).all(axis=2))] = [0, 0, 255]
    azImage[np.where((azImage == [4, 4, 4]).all(axis=2))] = [0, 0, 255]
    azImage[np.where((azImage == [5, 5, 5]).all(axis=2))] = [0, 0, 255]
    azImage[np.where((azImage == [6, 6, 6]).all(axis=2))] = [0, 0, 255]
    azImage[np.where((azImage == [7, 7, 7]).all(axis=2))] = [0, 0, 255]
    azImage[np.where((azImage == [8, 8, 8]).all(axis=2))] = [0, 0, 255]
    azImage[np.where((azImage == [9, 9, 9]).all(axis=2))] = [0, 0, 255]
    azImage[np.where((azImage == [10, 10, 10]).all(axis=2))] = [0, 24, 255]
    azImage[np.where((azImage == [11, 11, 11]).all(axis=2))] = [0, 37, 255]
    azImage[np.where((azImage == [12, 12, 12]).all(axis=2))] = [0, 47, 255]
    azImage[np.where((azImage == [13, 13, 13]).all(axis=2))] = [0, 55, 255]
    azImage[np.where((azImage == [14, 14, 14]).all(axis=2))] = [0, 63, 255]
    azImage[np.where((azImage == [15, 15, 15]).all(axis=2))] = [0, 69, 255]
    azImage[np.where((azImage == [16, 16, 16]).all(axis=2))] = [0, 76, 255]
    azImage[np.where((azImage == [17, 17, 17]).all(axis=2))] = [0, 82, 255]
    azImage[np.where((azImage == [18, 18, 18]).all(axis=2))] = [0, 87, 255]
    azImage[np.where((azImage == [19, 19, 19]).all(axis=2))] = [0, 92, 255]
    azImage[np.where((azImage == [20, 20, 20]).all(axis=2))] = [0, 98, 255]
    azImage[np.where((azImage == [21, 21, 21]).all(axis=2))] = [0, 103, 255]
    azImage[np.where((azImage == [22, 22, 22]).all(axis=2))] = [0, 107, 255]
    azImage[np.where((azImage == [23, 23, 23]).all(axis=2))] = [0, 112, 255]
    azImage[np.where((azImage == [24, 24, 24]).all(axis=2))] = [0, 117, 255]
    azImage[np.where((azImage == [25, 25, 25]).all(axis=2))] = [0, 121, 255]
    azImage[np.where((azImage == [26, 26, 26]).all(axis=2))] = [0, 126, 255]
    azImage[np.where((azImage == [27, 27, 27]).all(axis=2))] = [0, 130, 255]
    azImage[np.where((azImage == [28, 28, 28]).all(axis=2))] = [0, 134, 255]
    azImage[np.where((azImage == [29, 29, 29]).all(axis=2))] = [0, 138, 255]
    azImage[np.where((azImage == [30, 30, 30]).all(axis=2))] = [0, 142, 255]
    azImage[np.where((azImage == [31, 31, 31]).all(axis=2))] = [0, 147, 255]
    azImage[np.where((azImage == [32, 32, 32]).all(axis=2))] = [0, 151, 255]
    azImage[np.where((azImage == [33, 33, 33]).all(axis=2))] = [0, 155, 255]
    azImage[np.where((azImage == [34, 34, 34]).all(axis=2))] = [0, 158, 255]
    azImage[np.where((azImage == [35, 35, 35]).all(axis=2))] = [0, 162, 255]
    azImage[np.where((azImage == [36, 36, 36]).all(axis=2))] = [0, 166, 255]
    azImage[np.where((azImage == [37, 37, 37]).all(axis=2))] = [0, 170, 255]
    azImage[np.where((azImage == [38, 38, 38]).all(axis=2))] = [0, 174, 255]
    azImage[np.where((azImage == [39, 39, 39]).all(axis=2))] = [0, 178, 255]
    azImage[np.where((azImage == [40, 40, 40]).all(axis=2))] = [0, 181, 255]
    azImage[np.where((azImage == [41, 41, 41]).all(axis=2))] = [0, 185, 255]
    azImage[np.where((azImage == [42, 42, 42]).all(axis=2))] = [0, 189, 255]
    azImage[np.where((azImage == [43, 43, 43]).all(axis=2))] = [0, 192, 255]
    azImage[np.where((azImage == [45, 45, 45]).all(axis=2))] = [0, 196, 255]
    azImage[np.where((azImage == [46, 46, 46]).all(axis=2))] = [0, 199, 255]
    azImage[np.where((azImage == [47, 47, 47]).all(axis=2))] = [0, 203, 255]
    azImage[np.where((azImage == [48, 48, 48]).all(axis=2))] = [0, 206, 255]
    azImage[np.where((azImage == [49, 49, 49]).all(axis=2))] = [0, 210, 255]
    azImage[np.where((azImage == [50, 50, 50]).all(axis=2))] = [0, 210, 255]
    azImage[np.where((azImage == [51, 51, 51]).all(axis=2))] = [0, 210, 255]
    azImage[np.where((azImage == [52, 52, 52]).all(axis=2))] = [0, 210, 255]
    azImage[np.where((azImage == [53, 53, 53]).all(axis=2))] = [0, 210, 255]
    azImage[np.where((azImage == [54, 54, 54]).all(axis=2))] = [0, 210, 255]
    azImage[np.where((azImage == [55, 55, 55]).all(axis=2))] = [0, 210, 255]
    azImage[np.where((azImage == [56, 56, 56]).all(axis=2))] = [0, 210, 255]
    azImage[np.where((azImage == [57, 57, 57]).all(axis=2))] = [0, 210, 255]
    azImage[np.where((azImage == [58, 58, 58]).all(axis=2))] = [0, 210, 255]
    azImage[np.where((azImage == [59, 59, 59]).all(axis=2))] = [0, 210, 255]
    azImage[np.where((azImage == [60, 60, 60]).all(axis=2))] = [0, 210, 255]
    final = color_cropp8(azImage)

    cv2.imwrite('/tmp/coronalHole.jpg', final)
    with open('/tmp/coronalHole.jpg', "rb") as gop_file:
        try:
            blob = bucket.blob('coronalHole.jpg')
            blob.metadata = {'contentType': 'image/jpeg'}
            blob.make_public()
            blob.upload_from_filename('/tmp/coronalHole.jpg')
            gop_file.close()
        except Exception as e:
            print('upload_blob Error', e)
    os.remove('/tmp/coronalHole.jpg')
    os.remove('/tmp/211.jpg')
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%m-%d-%Y %H:%M:%S")
    ref.update({'chTime': timestampStr})
