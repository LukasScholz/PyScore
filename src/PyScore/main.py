import time

import cv2
import pdf_tools

FILEPATH = "../../examples/moonlight_sonata.pdf"

#with pdf_tools.PDF2Image(FILEPATH) as files:
#    for f in files:
#        img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
#        cv2.imshow("Score", img)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()

with pdf_tools.PDF2Image(FILEPATH) as files:
    for f in files:
        # Load image, convert to grayscale
        image = cv2.imread(f)
        result = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # Detect horizontal lines
        kernel_length = 60
        kernel_width = 1
        horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, kernel_width))
        detect_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
        cnts = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            cv2.drawContours(result, [c], -1, (36, 255, 12), 2)

        cv2.imshow('result', result)
        cv2.waitKey()