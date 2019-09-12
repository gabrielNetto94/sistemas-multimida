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
	src = imread("data/vermelho.png");

	if (src.empty()) { cout << "Erro ao carregar a imagem" << endl; return -1; }

	//trocando as cores dos pixeis

	//le a imagem pixel a pixel
	for (int i = 0; i < src.rows; i++)
	{
		for (int j = 0; j < src.cols; j++)
		{
			//cada pixel da imagem tem um valor BGR, ou seja, 3 valores
			cv::Vec3b bgrPixel = src.at<cv::Vec3b>(i, j);

			try
			{

				bgrPixel.val[0] = 255;	//B
				bgrPixel.val[1] = 0;	//G
				bgrPixel.val[2] = 0;	//R

				src.at<cv::Vec3b>(i, j) = bgrPixel;
			}
			catch (int e)
			{
				continue;
			}
		}
	}
	
	//mostra na tela
	imshow("Imagem com cores trocadas", src);
	waitKey(0);

	//grava em um arquivo
	cv::imwrite("azul.jpg", src);
	return 0;
}
