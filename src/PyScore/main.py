import time

import cv2
import pdf_tools

FILEPATH = "../../examples/moonlight_sonata.pdf"

with pdf_tools.PDF2Image(FILEPATH) as files:
    for f in files:
        img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        cv2.imshow("Score", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()