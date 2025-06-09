import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    N = int(input("Please enter N (number of training points): "))
    if N <= 0:
        print("Please input a positive integer for N.")
        return

    trainS = []

    for i in range(N):
        x_val = float(input(f"Enter x value for training point {i+1}: "))
        y_val = int(input(f"Enter y value for training point {i+1}: "))
        trainS.append((x_val, y_val))

    trainS = np.array(trainS)
    X_train = trainS[:, 0].reshape((-1, 1))
    Y_train = trainS[:, 1].astype(int)

    M = int(input("Please enter M (number of test points): "))
    if M <= 0:
        print("Please input a positive integer for M.")
        return

    testS = []

    for i in range(M):
        x_test = float(input(f"Enter x value for test point {i+1}: "))
        y_test = int(input(f"Enter y value for test point {i+1}: "))
        testS.append((x_test, y_test))

    testS = np.array(testS)
    X_test = testS[:, 0].reshape((-1, 1))
    Y_test = testS[:, 1].astype(int)

    bestK = 1
    bestAccuracy = 0.0

    print("\nTesting accuracy for k = 1 to", min(10, N))
    print("------------------------------------")

    for k in range(1, min(11, N + 1)):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, Y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(Y_test, y_pred)
        print(f"k = {k}: Accuracy = {accuracy:.4f}")
        if accuracy > bestAccuracy or (accuracy == bestAccuracy and k > bestK):
            bestAccuracy = accuracy
            bestK = k

    print("------------------------------------")
    print(f"Best K is: {bestK}")
    print(f"Best Accuracy is: {bestAccuracy:.4f}")


if __name__ == "__main__":
    main()