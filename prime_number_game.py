import random

def check_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if check_prime(num):
    print(num, "is Prime")
else:
    print(num, "is Not Prime")


print("\nPrime Number Game")

score = 0
results = []

for round in range(1, 6):

    num = random.randint(2, 70)

    print("\nRound", round)
    print("Number:", num)

    answer = input("Prime or Not Prime? (P/N): ").upper()

    if check_prime(num):
        correct = "P"
    else:
        correct = "N"

    if answer == correct:
        print("Correct!")
        score += 1
        result = "Correct"
    else:
        print("Wrong!")
        result = "Wrong"

    results.append([round, num, answer, correct, result])


print("\nGame Over!")
print("Your score:", score, "out of 5")

print("\nRound Summary")

for result in results:
    print(
        "Round:", result[0],
        "| Number:", result[1],
        "| Your Answer:", result[2],
        "| Correct Answer:", result[3],
        "|", result[4]
    )
