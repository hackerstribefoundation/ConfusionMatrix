def calcConfusionMatrixBinary():
	modelPredictions = tP + fP
	precision = tP/ modelPredictions
	groundTruth = tP + fN
	recall = tP /  groundTruth
	f1 = 2*(precision * recall)/(precision + recall)
	print("Precision score is - " + str(precision*100) + "%")
	print("Recall score is - " + str(recall*100) + "%")
	print("F1 score is - " + str(f1*100) + "%")

def calcConfusionMatrixMulti():
	modelPredictions = tP + fP
	precision = tP/ modelPredictions
	groundTruth = tP + fN
	recall = tP /  groundTruth
	f1 = 2*(precision * recall)/(precision + recall)
	print("Precision score is - " + str(precision*100) + "%")
	print("Recall score is - " + str(recall*100) + "%")
	print("F1 score is - " + str(f1*100) + "%")

classfierType = input("Is this a binary type classification?(Y/N) - ")

if classfierType == "Y":
	tP = float(input("Enter value of True Positive: "))
	fP = float(input("Enter value of False Positive: "))
	tN = float(input("Enter value of True Negative: "))
	fN = float(input("Enter value of False Negative: "))
	print("Confusion Matrix is:\n")
	print("\t\t\t" +"Predicted" + "\t" + "Predicted")
	print("\t\t\t" +"Class 1" + "\t\t" + "Class 2")
	print("Ground Truth Class 1" + "\t[" + str(tP) + "\t\t" + str(fN) + "]")
	print("Ground Truth Class 2" + "\t[" + str(fP) + "\t\t" + str(tN)+ "]\n")
	calcConfusionMatrixBinary()
else:
	# from sklearn import metrics

	print("NOTE - After entering each value press Enter")
	print("Enter values for first column from Left to Right")
	x11 = float(input(""))
	x12 = float(input(""))
	x13 = float(input(""))
	x1sum = x11+x12+x13
	print("Enter values for second column from Left to Right")
	x21 = float(input(""))
	x22 = float(input(""))
	x23 = float(input(""))
	x2sum = x21+x22+x23
	print("Enter values for third column from Left to Right")
	x31 = float(input(""))
	x32 = float(input(""))
	x33 = float(input(""))
	x3sum = x31+x32+x33

	# True values
	y_true = [x1sum, x2sum, x3sum]
	print(y_true)
	# Predicted values
	y_pred = [x11,x12,x13, x21,x22,x23, x31,x32,x33]
	print(y_pred)

	print("Confusion Matrix would look :\n")
	print("\t\t\t" +"Predicted" + "\t" + "Predicted" + "\t" + "Predicted")
	print("\t\t\t" +"Class 1" + "\t\t" + "Class 2" + "\t\t" + "Class 3")
	print("Ground Truth Class 1" + "\t[" + str(x11) + "\t\t" + str(x12) + "\t\t" + str(x13) + "]")
	print("Ground Truth Class 2" + "\t[" + str(x21) + "\t\t" + str(x22) + "\t\t" + str(x23) + "]")
	print("Ground Truth Class 3" + "\t[" + str(x31) + "\t\t" + str(x32) + "\t\t" + str(x33) + "]\n")

	calcConfusionMatrixMulti()

	# Print the confusion matrix
	# print(metrics.confusion_matrix(y_true, y_pred))

	# Print the precision and recall, among other metrics
	# print(metrics.classification_report(y_true, y_pred, digits=3))
