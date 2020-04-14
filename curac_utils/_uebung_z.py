# -*- coding: utf-8 -*-

import urllib.request
from skimage import io, img_as_float


class UebungZ():
    
    @staticmethod
    def aufgabe_1():
        """
        Diese Funktion gibt das Ergebnis der Aufgabe 1 aus.
        """
        print("Herzlichen Glückwunsch! Du hast Aufgabe 1 der Zusatzübung erfolgreich abgeschlossen.")

    @staticmethod
    def aufgabe_2():
        """
        Diese Funktion lädt ein CT-Scan von https://commons.wikimedia.org/wiki/File:Renal_cyst_MRI.jpg herunter
        und gibt diesen als Numpy Array zurück.
        :return: CT-Scan als Numpy array
        """

        urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Renal_cyst_MRI.jpg/480px-Renal_cyst_MRI.jpg",
                                   "480px-Renal_cyst_MRI.jpg")

        return img_as_float(io.imread("480px-Renal_cyst_MRI.jpg", as_gray=True))
