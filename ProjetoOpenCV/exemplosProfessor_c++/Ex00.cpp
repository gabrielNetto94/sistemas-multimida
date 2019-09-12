#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace cv;

using std::cin;
using std::cout;
using std::endl;

int main(void)
{
	Mat src;

	/// Le uma imagem de um arquivo
	src = imread("data/LinuxLogo.jpg");

	if (src.empty()) { cout << "Erro ao carregar a imagem" << endl; return -1; }

	Mat copia = src.clone();//faz uma copia da imagem inteira
	//src.copyTo(copia); //alternativo

	//mostra na tela
	imshow("Imagem", copia);
	waitKey(0);

	return 0;
}
