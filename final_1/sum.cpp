#include <iostream>

int sumofsquares(int a, int b) {
  int last = (b + 1) -a;
  int i = 0;
  int sum = 0;
  while (i < last) {
    sum += (a + i) * (a + i);
    std::cout << "squared is " << (a+i)*(a+i) << "\n";
    i += 1;
  }
  std::cout <<"Total is " <<  sum << "\n";

}

int main () {
    sumofsquares(5, 10);
    sumofsquares(7, 10);
    sumofsquares(11, 95);
    sumofsquares(80, 101);
    sumofsquares(68, 70);
}

