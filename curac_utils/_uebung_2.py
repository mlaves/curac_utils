# -*- coding: utf-8 -*-

import urllib.request
from skimage import io, img_as_ubyte, img_as_uint
import numpy as np
import pkg_resources


class Uebung_2():

    @staticmethod
    def aufg_1_get_grayscale():
        """
        Diese Funktion lädt einen histologischen Schnitt von
        https://commons.wikimedia.org/wiki/File:Histo_Lungenpest.jpg herunter und gibt diesen als Liste von
         Numpy Arrays der einzelnen Farbkanäle [R, G, B] zurück.

        :return: [R, G, B] Liste von RGB-Farbkanälen
        """

        urllib.request.urlretrieve(
            "https://upload.wikimedia.org/wikipedia/commons/d/d7/Histo_Lungenpest.jpg")

        img = img_as_ubyte(io.imread("Histo_Lungenpest.jpg", as_gray=False))

        return img[:, :, 0], img[:, :, 1], img[:, :, 2]

    @staticmethod
    def aufg_4_get_img():
        """
        Diese Funktion lädt einen 16-Bit CT-Scan und gibt diesen als uint16 Numpy Arrays zurück.

        :return: uint16 ndarray
        """

        img_path = pkg_resources.resource_filename(__name__, 'data/a2gray.tiff')
        img = img_as_uint(io.imread(img_path))

        return img
