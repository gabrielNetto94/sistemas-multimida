#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace cv;

using std::cin;
using std::cout;
using std::endl;

int main(void)
{
	//cria uma matriz de imagem 2x2 na memória
	//CV_8UC3 significa que é uma imagem de 3 canais (BGR) cujos valores são de até 8 bits (0 a 255)
	Mat M(2, 2, CV_8UC3, Scalar(0, 0, 255));

	cout << "M = " << endl << " " << M << endl << endl;

	//cria uma matriz de imagem 40x40 na memória
	Mat M2;
	M2.create(40, 40, CV_8UC(3));
	//coloca valores aleatórios nela de 0 a 255
	randu(M2, Scalar::all(0), Scalar::all(255));
	//cout << "M2 = " << endl << " " << M2 << endl << endl;

	//mostra na tela
	imshow("Imagem", M2);
	waitKey(0);

	//grava em um arquivo
	cv::imwrite("resultado.jpg", M);

	return 0;
}
