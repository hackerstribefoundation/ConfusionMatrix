def calcConfusionMatrixBinary(tP, fP, tN, fN):
    modelPredictions = tP + fP
    precision = tP / modelPredictions
    groundTruth = tP + fN
    recall = tP / groundTruth
    f1 = 2 * (precision * recall) / (precision + recall)
    print("Precision score is - " + str(precision * 100) + "%")
    print("Recall score is - " + str(recall * 100) + "%")
    print("F1 score is - " + str(f1 * 100) + "%")

def calcConfusionMatrixMulti(x11, x12, x13, x21, x22, x23, x31, x32, x33):
    modelPredictions = x11 + x12 + x13 + x21 + x22 + x23 + x31 + x32 + x33
    precision = (x11 + x22 + x33) / modelPredictions
    groundTruth = sum([x11 + x21 + x31, x12 + x22 + x32, x13 + x23 + x33])
    recall = (x11 + x22 + x33) / groundTruth
    f1 = 2 * (precision * recall) / (precision + recall)
    print("Precision score is - " + str(precision * 100) + "%")
    print("Recall score is - " + str(recall * 100) + "%")
    print("F1 score is - " + str(f1 * 100) + "%")

classifierType = input("Is this a binary type classification? (Y/N): ")

if classifierType == "Y":
    tP = float(input("Enter value of True Positive: "))
    fP = float(input("Enter value of False Positive: "))
    tN = float(input("Enter value of True Negative: "))
    fN = float(input("Enter value of False Negative: "))
    print("Confusion Matrix is:\n")
    print("\t\t\t" + "Predicted" + "\t" + "Predicted")
    print("\t\t\t" + "Class 1" + "\t\t" + "Class 2")
    print("Ground Truth Class 1" + "\t[" + str(tP) + "\t\t" + str(fN) + "]")
    print("Ground Truth Class 2" + "\t[" + str(fP) + "\t\t" + str(tN) + "]\n")
    calcConfusionMatrixBinary(tP, fP, tN, fN)
else:
    print("NOTE: After entering each value, press Enter.")
    x11 = float(input("Enter value for True Positive in Class 1: "))
    x12 = float(input("Enter value for False Positive in Class 1: "))
    x13 = float(input("Enter value for False Negative in Class 1: "))
    x21 = float(input("Enter value for False Positive in Class 2: "))
    x22 = float(input("Enter value for True Positive in Class 2: "))
    x23 = float(input("Enter value for False Negative in Class 2: "))
    x31 = float(input("Enter value for False Negative in Class 3: "))
    x32 = float(input("Enter value for False Positive in Class 3: "))
    x33 = float(input("Enter value for True Positive in Class 3: "))
    print("Confusion Matrix is:\n")
    print("\t\t\t" + "Predicted" + "\t" + "Predicted" + "\t" + "Predicted")
    print("\t\t\t" + "Class 1" + "\t\t" + "Class 2" + "\t\t" + "Class 3")
    print("Ground Truth Class 1" + "\t[" + str(x11) + "\t\t" + str(x12) + "\t\t" + str(x13) + "]")
    print("Ground Truth Class 2" + "\t[" + str(x21) + "\t\t" + str(x22) + "\t\t" + str(x23) + "]")
    print("Ground Truth Class 3" + "\t[" + str(x31) + "\t\t" + str(x32) + "\t\t" + str(x33) + "]\n")
    calcConfusionMatrixMulti(x11, x12, x13, x21, x22, x23, x31, x32, x33)
