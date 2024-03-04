def calcConfusionMatrixBinary():
    # Calculate confusion matrix for binary classification
    tP = float(input("Enter value of True Positive: "))
    fP = float(input("Enter value of False Positive: "))
    tN = float(input("Enter value of True Negative: "))
    fN = float(input("Enter value of False Negative: "))
    
    precision = tP / (tP + fP)
    recall = tP / (tP + fN)
    f1 = 2 * (precision * recall) / (precision + recall)
    
    print("Precision score is - " + str(precision * 100) + "%")
    print("Recall score is - " + str(recall * 100) + "%")
    print("F1 score is - " + str(f1 * 100) + "%")
    
    # Prepare confusion matrix
    confusion_matrix = [[tN, fP], [fN, tP]]
    return confusion_matrix

def calcConfusionMatrixMulti():
    # Calculate confusion matrix for multi-class classification
    # You can modify this part to accept input for multi-class confusion matrix
    pass

classifierType = input("Is this a binary type classification?(Y/N) - ")

if classifierType == "Y":
    confusion_matrix = calcConfusionMatrixBinary()
else:
    confusion_matrix = calcConfusionMatrixMulti()

print("Confusion Matrix is:")
for row in confusion_matrix:
    print(row)

# Display confusion matrix in HTML
print('<script>document.getElementById("output").style.display = "block";</script>')
print('<script>updateConfusionMatrix(' + str(confusion_matrix) + ');</script>')
