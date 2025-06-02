import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Please enter N (number of points): "))
    if N <= 0:
        print("Please input a positive integer for N.")
        return

    x_train = np.zeros(N, dtype=int)
    y_predict = np.zeros(N, dtype=int)

    for i in range(N):
        x_val = int(input(f"Enter ground truth X for point {i+1} (0 or 1): "))
        while x_val not in (0, 1):
            print("Invalid input. Please enter 0 or 1.")
            x_val = int(input(f"Enter ground truth X for point {i+1} (0 or 1): "))

        y_val = int(input(f"Enter predicted Y for point {i+1} (0 or 1): "))
        while y_val not in (0, 1):
            print("Invalid input. Please enter 0 or 1.")
            y_val = int(input(f"Enter predicted Y for point {i+1} (0 or 1): "))

        x_train[i] = x_val
        y_predict[i] = y_val

    precision = precision_score(x_train, y_predict, zero_division=0)
    recall = recall_score(x_train, y_predict, zero_division=0)

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
