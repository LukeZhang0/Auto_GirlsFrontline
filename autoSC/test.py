from autoSC import *

time.sleep(0.5)
img = getImage(CHOOSE_CCIV_IMAGE_BOX)
img.show()
time.sleep(1)

img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
#cv2.imwrite("initial_IMG/_CCIV1.png", img)
