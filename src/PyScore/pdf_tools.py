import os
import random
import string
import shutil

import fitz
import cv2


class PDF2Image:

    def __init__(self, path_to_pdf):
        self.path = path_to_pdf
        self.foldername = ".temp_" + ''.join(random.choices(string.ascii_letters, k=16))

    def __enter__(self):
        os.mkdir(self.foldername)
        # To get better resolution
        zoom_x = 1.0  # horizontal zoom
        zoom_y = 1.0  # vertical zoom
        mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

        files = []
        doc = fitz.open(self.path)  # open document
        for page in doc:  # iterate through the pages
            pix = page.get_pixmap(matrix=mat)  # render page to an image
            file = self.foldername + "/page-%i.png" % page.number
            pix.save(file)  # store image as a PNG
            files.append(file)
        return files

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.foldername)


def show_pdf(files):
    for f in files:
        img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        cv2.imshow("Score", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
