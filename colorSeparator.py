import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():

	continueSession = True

	while (continueSession):

		#User selects an image
		pictureType = input("Choose an image: \n 1) Penguin \n 2) Giraffe \n 3) Peacock \n 4) End Session \n")

		if ((pictureType.lower() == "penguin") or (pictureType == "1") or (pictureType == "1)")):
			image = cv2.imread("./images/penguin.jpg")
		elif ((pictureType.lower() == "giraffe") or (pictureType == "2") or (pictureType == "2)")):
			image = cv2.imread("./images/giraffe.jpg")
		elif ((pictureType.lower() == "peacock") or (pictureType == "3") or (pictureType == "3)")):
			image = cv2.imread('./images/peacock.jpg')
		elif ((pictureType.lower() == "end") or (pictureType.lower() == "end session") or (pictureType == "4") or (pictureType == "4)")):
			continueSession = False
			break
		else:
		   	pictureType = input("Input not recognized. Please try again. \n Choose an image: \n 1) Penguin \n 2) Giraffe \n 3) Peacock \n")

		#User selects a color option
		versionType = input("Which color component do you want to see? \n 1) Red \n 2) Green \n 3) Blue \n 4) Original \n")
		Blue, Green, Red = cv2.split(image)
		color = ('b', 'g', 'r')
		zeroMatrix = np.zeros(image.shape[:2], dtype = "uint8")

		#Plot the colors
		for i, col in enumerate(color):
			histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
			plt.plot(histogram, color = col)
			plt.xlim([0, 256])

		if ((versionType.lower() == "red") or (versionType == "1") or (versionType == "1)")):
			plt.show()			
			cv2.imshow("Red Component", cv2.merge([zeroMatrix, zeroMatrix, Red]))
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		elif ((versionType.lower() == "green") or (versionType == "2") or (versionType == "2)")):
			plt.show()			
			cv2.imshow("Green Component", cv2.merge([zeroMatrix, Green, zeroMatrix]))
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		elif ((versionType.lower() == "blue") or (versionType == "3") or (versionType == "3)")):
			plt.show()			
			cv2.imshow("Blue Component", cv2.merge([Blue, zeroMatrix, zeroMatrix]))
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		elif ((versionType.lower() == "original") or (versionType == "4") or (versionType == "4)")):
			plt.show()			
			cv2.imshow("Original Image", cv2.merge([Blue, Green, Red]))
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		else:
			versionType = input("Which color component do you want to see? \n 1) Red \n 2) Green \n 3) Blue \n 4) Original \n")

		print("---------------------------------------------------------------------------------------------------------------------------")

	print("Thank You!")

main()
