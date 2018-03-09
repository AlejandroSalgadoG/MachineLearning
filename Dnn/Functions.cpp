#include <math.h>
#include "Functions.h"

void Sigmoid::evaluate(double* x, double* ans, int size){
    for(int i=0;i<size;i++)
        x[i] = 1/(1+exp(x[i] * -1));
} 

double Sigmoid::derivative(double* x, int element){
    return x[element] * (1 - x[element]);
}

LessSquare::LessSquare(double * y){
	this->y = y;
}

void LessSquare::evaluate(double * y_hat, double* loss, int size){
    *loss = 0;
    for(int i=0;i<size;i++)
        *loss += pow(y[i] - y_hat[i], 2);
	*loss /= 2;
}

double LessSquare::derivative(double * y_hat, int element){
	return y_hat[element] - y[element];;
}