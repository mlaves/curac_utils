# -*- coding: utf-8 -*-

import urllib.request
from skimage import io, img_as_float
from skimage.util import invert
import numpy as np


class Uebung_0():
    
    @staticmethod
    def aufg_1():
        """
        Diese Funktion gibt das Ergebnis der Aufgabe 1 aus.
        """
        print("Herzlichen Glückwunsch! Du hast Aufgabe 1 der Zusatzübung erfolgreich abgeschlossen.")

    @staticmethod
    def aufg_2_get_ct():
        """
        Diese Funktion lädt ein CT-Scan von https://commons.wikimedia.org/wiki/File:Renal_cyst_MRI.jpg herunter
        und gibt diesen als Numpy Array zurück.

        :return: CT-Scan als Numpy array
        """

        urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Renal_cyst_MRI.jpg/480px-Renal_cyst_MRI.jpg",
                                   "480px-Renal_cyst_MRI.jpg")

        return img_as_float(io.imread("480px-Renal_cyst_MRI.jpg", as_gray=True))

    @staticmethod
    def aufg_2_test(input_img):
        """
        Diese Funktion testet, ob Aufgabe 2 korrekt gelöst wurde. Als Parameter erwartet sie den invertierten CT-Scan.

        :param input_img: Numpy Array des invertierten CT-Scans
        :return: True wenn die Aufgabe korrekt gelöst wurde, ansonsten False
        """

        return np.allclose(input_img, invert(Uebung_0.aufg_2_get_ct()))
