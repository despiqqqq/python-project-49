import random
import prompt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 100)

        print("Question:", number)
        answer = input("Your answer: ")

        if (answer == "yes" and is_prime(number)) or (answer == "no" and not is_prime(number)):
            print("Correct!")
            correct_answers+=1
        else:
            correct_answer = "yes" if is_prime(number) else "no"
            print("'" + answer + "' is wrong answer ;(. Correct answer was '" + correct_answer + "'.")
            print("Let's try again, " + name + "!")
            break

    print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()