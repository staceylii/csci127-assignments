#include <iostream>
#include <math.h>

int disc(int a, int b, int c) {
int ans;

 ans = (b*b)-(4*a*c);
 return ans;

  }

int quadsolve (int a, int b, int c) {
  int disc = (b*b)-(4*a*c);
  int x ;
  if (disc >= 0){
    int pos;
    x  = (disc - b) / (2*a);
  }
  else {
    x  = 0;
  }
  std::cout << "Root is " <<  x << "\n" ;
  return x;
  
}
int main()
{
  std::cout << disc(5, 5, 8) << "\n";
  std::cout << disc(1, 6, 2) << "\n";
  std::cout << disc(7, 5, 0) << "\n";
  std::cout << quadsolve(7, 5, 0) << "\n";
  std::cout << quadsolve(5, 5, 8) << "\n";
  std::cout << quadsolve(1, 6, 2) << "\n";
  return 0;
}

/*
int quadsolve (int a, int b, int c) {
	int root;
	int disc = (b*b) - (4*a*c);
	if (disc >= 0) {
		root = (disc - b) / (2*a);
	}
	else {
		root = 0;
	}
	std::cout << "The root is " << root << std::endl;
	return root;

*/
