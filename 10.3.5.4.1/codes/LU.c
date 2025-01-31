#include <stdio.h>
#include <stdlib.h>

// Function to perform LU Decomposition and solve Ax = B
void solve_lu(double A[2][2], double B[2], double X[2]) {
    double L[2][2] = { {1, 0}, {0, 0} };
    double U[2][2] = { {0, 0}, {0, 0} };
    double Y[2]; // Intermediate solution
    
    // LU Decomposition
    U[0][0] = A[0][0];
    U[0][1] = A[0][1];
    L[1][0] = A[1][0] / U[0][0];
    U[1][1] = A[1][1] - L[1][0] * U[0][1];
    L[1][1] = 1;

    // Forward substitution: Solve LY = B
    Y[0] = B[0];
    Y[1] = B[1] - L[1][0] * Y[0];

    // Backward substitution: Solve UX = Y
    X[1] = Y[1] / U[1][1];
    X[0] = (Y[0] - U[0][1] * X[1]) / U[0][0];
}

void solve(double *result) {
    double A[2][2] = { {1, 20}, {1, 26} };
    double B[2] = { 1000, 1080 };
    double X[2];

    solve_lu(A, B, X);

    result[0] = X[0];
    result[1] = X[1];
}

