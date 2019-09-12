/**
 * @file AddingImages.cpp
 * @brief Simple linear blender ( dst = alpha*src1 + beta*src2 )
 * @author OpenCV team
 */
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace cv;

// we're NOT "using namespace std;" here, to avoid collisions between the beta variable and std::beta in c++17
using std::cin;
using std::cout;
using std::endl;

/**
 * @function main
 * @brief Main function
 */
int main(void)
{
	double alpha = 0.5; double beta;

	Mat src1, src2, dst;

	/// Le imagens (ambas precisam ser do mesmo tamanho e tipo)
	src1 = imread("data/LinuxLogo.jpg");
	src2 = imread("data/WindowsLogo.jpg");

	if (src1.empty()) { cout << "Erro ao carregar a imagem 1" << endl; return -1; }
	if (src2.empty()) { cout << "Erro ao carregar a imagem 2" << endl; return -1; }

	//mistura as imagens
	beta = (1.0 - alpha);
	addWeighted(src1, alpha, src2, beta, 0.0, dst);

	//mostra na tela
	imshow("Linear Blend", dst);
	waitKey(0);

	return 0;
}
