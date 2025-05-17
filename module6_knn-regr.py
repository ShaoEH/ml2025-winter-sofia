import numpy as np

def calculate_knn_regression(X_train, Y_train, X_test, K):
    distances = np.abs(X_train - X_test)
    nearest_neighbors = np.argsort(distances)[:K]
    return np.mean(Y_train[nearest_neighbors])

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

    Y_pred = calculate_knn_regression(X_train, Y_train, X_test, K)
    print(f"The predicted Y value is: {Y_pred}")

if __name__ == "__main__":
    main()