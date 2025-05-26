import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    N = int(input("Please enter N (number of points): "))
    if N <= 0:
        print("Please input a positive integer for N.")
        return

    K = int(input("Please enter K (number of neighbors): "))
    if K <= 0:
        print("Please input a positive integer for K.")
        return

    X_train = np.zeros(N)
    Y_train = np.zeros(N)

    for i in range(N):
        X_val = float(input(f"Please enter the X value for point {i+1}: "))
        Y_val = float(input(f"Please enter the Y value for point {i+1}: "))
        X_train[i] = X_val
        Y_train[i] = Y_val

    X_test = float(input(f"Please enter the X value you want to predict: "))

    if K > N:
        print("Please enter the number K that is not greater than N.")
        return

    knn = KNeighborsRegressor(n_neighbors=K)
    knn.fit(X_train.reshape(-1, 1), Y_train)
    Y_pred = knn.predict(np.array([[X_test]]))

    print(f"The predicted Y value is: {Y_pred[0]}")

    variance = np.var(Y_train)
    print(f"Variance of labels: {variance}")

if __name__ == "__main__":
    main()