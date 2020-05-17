from PIL import Image
import numpy
im=Image.open(r'c:\Users\rajes\Pythoncode\.vscode\qstp.jpg')
np_im=numpy.array(im)
invert=255-np_im
finalim=Image.fromarray(invert)
finalim.show()
finalim.save(r'c:\Users\rajes\Pythoncode\.vscode\finalqstp.jpg')
grayim=numpy.mean(np_im, axis=2)
finalgrayim=Image.fromarray(grayim)
finalgrayim=finalgrayim.convert("L")
finalgrayim.show()
finalgrayim.save(r'c:\Users\rajes\Pythoncode\.vscode\finalgrayqstp.jpg')