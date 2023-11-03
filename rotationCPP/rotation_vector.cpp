#include <iostream>
#include <cmath>
#include <vector>

// Function to normalize a 3D vector
std::vector<double> normalizeVector(const std::vector<double>& vec) {
    double norm = 0;
    for (double value : vec) {
        norm += value * value;
    }
    norm = std::sqrt(norm);

    std::vector<double> normalized;
    for (double value : vec) {
        normalized.push_back(value / norm);
    }
    return normalized;
}

// Function to rotate a 3D vector to another 3D vector
std::vector<double> rotateVectorToVector(const std::vector<double>& v, const std::vector<double>& target) {
    std::vector<double> normalizedV = normalizeVector(v);
    std::vector<double> normalizedTarget = normalizeVector(target);

    
    if (normalizedV[0] * normalizedTarget[0] + normalizedV[1] * normalizedTarget[1] + normalizedV[2] * normalizedTarget[2] < 0){
        normalizedTarget[0] = -1 * normalizedTarget[0];
        normalizedTarget[1] = -1 * normalizedTarget[1];
        normalizedTarget[2] = -1 * normalizedTarget[2];
    }

    // Calculate the cross product
    std::vector<double> crossProduct;
    crossProduct.push_back(normalizedV[1] * normalizedTarget[2] - normalizedV[2] * normalizedTarget[1]);
    crossProduct.push_back(normalizedV[2] * normalizedTarget[0] - normalizedV[0] * normalizedTarget[2]);
    crossProduct.push_back(normalizedV[0] * normalizedTarget[1] - normalizedV[1] * normalizedTarget[0]);

    double norm_cross_product = std::sqrt(crossProduct[0]* crossProduct[0] + crossProduct[1]*crossProduct[1]+crossProduct[2]*crossProduct[2]);
    crossProduct[0] = crossProduct[0] / norm_cross_product;
    crossProduct[1] = crossProduct[1] / norm_cross_product;
    crossProduct[2] = crossProduct[2] / norm_cross_product;

    // Calculate the dot product
    double dotProduct = normalizedV[0] * normalizedTarget[0] + normalizedV[1] * normalizedTarget[1] + normalizedV[2] * normalizedTarget[2];

    // Calculate the angle and adjust for angles greater than 90 degrees
    # define M_PI  3.14159265358979323846  /* pi */
    double angle = acos(dotProduct);

    // Calculate the rotation matrix
    double c = cos(angle);
    double s = sin(angle);
    double t = 1 - c;
    double x = crossProduct[0];
    double y = crossProduct[1];
    double z = crossProduct[2];

    std::cout << c << std::endl;
    std::cout << s << std::endl;
    std::cout << t << std::endl;
    std::cout << x << std::endl;
    std::cout << y << std::endl;
    std::cout << z << std::endl;

    // Apply the rotation matrix to the vector
    std::vector<double> rotatedVector;
    rotatedVector.push_back(t * x * x + c);
    rotatedVector.push_back(t * x * y - s * z);
    rotatedVector.push_back(t * x * z + s * y);

    rotatedVector.push_back(t * x * y + s * z);
    rotatedVector.push_back(t * y * y + c);
    rotatedVector.push_back(t * y * z - s * x);

    rotatedVector.push_back(t * x * z - s * y);
    rotatedVector.push_back(t * y * z + s * x);
    rotatedVector.push_back(t * z * z + c);

    std::cout << rotatedVector[0] << " " << rotatedVector[1] << " " << rotatedVector[2] << std::endl;
    std::cout << rotatedVector[3] << " " << rotatedVector[4] << " " << rotatedVector[5] << std::endl;
    std::cout << rotatedVector[6] << " " << rotatedVector[7] << " " << rotatedVector[8] << std::endl;

    // Apply the rotation to the vector
    double newX = rotatedVector[0] * v[0] + rotatedVector[1] * v[1] + rotatedVector[2] * v[2];
    double newY = rotatedVector[3] * v[0] + rotatedVector[4] * v[1] + rotatedVector[5] * v[2];
    double newZ = rotatedVector[6] * v[0] + rotatedVector[7] * v[1] + rotatedVector[8] * v[2];
    
    std::cout << newX << " " << newY << " " << newZ << std::endl;

    return {newX, newY, newZ};
}

int main() {
    std::vector<double> initialVector = {1.0, -5.0, 0.0};
    std::vector<double> targetVector = {1.0, 2.0, 0.0};

    std::vector<double> rotatedVector = rotateVectorToVector(initialVector, targetVector);

    std::cout << "Initial Vector: (" << initialVector[0] << ", " << initialVector[1] << ", " << initialVector[2] << ")\n";
    std::cout << "Target Vector: (" << targetVector[0] << ", " << targetVector[1] << ", " << targetVector[2] << ")\n";
    std::cout << "Rotated Vector: (" << rotatedVector[0] << ", " << rotatedVector[1] << ", " << rotatedVector[2] << ")\n";

    return 0;
}
