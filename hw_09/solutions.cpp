#include <iostream>

into main ()
{
  //establish the computers number
  srand(time(NULL));
  int answer = rand()%100;
  std::cout<<answer<< "\n";
  answer = rand()%100;
  std::cout <<answer << "\n";
  // repeat until the answer is guessed
  // get a guess from the user
  // see if the guess is too low/high/just right
  std::count << "Please enter a guess: ";
  std::cin >> guess;
  while (guess != answer) {
    if (guess>answer)
      std::cout << "you guessed too high\n";
    else if (guess < annswer)
      std::cout << "You guessed too low\n";
    std::cout << "Please enter a guess: ";
    std::cin >>guess;
    guesses++;
    
  }
  std::cout << "congratulations, you guessed the number!!!\n";
  return 0;
}
