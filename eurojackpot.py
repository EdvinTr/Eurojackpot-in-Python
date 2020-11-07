from generate import generate_row
from userinput import user_row_generator
from time import time

done = False
while not done:
    users_row = user_row_generator()

    results_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0
    }

    while True:
        loops = input("How many loops would you like to run? ")
        try:
            loops = int(loops)
            print("Executing...")
            break
        except ValueError:
            print("Enter a valid number")
    start = time()
    for x in range(loops):

        game_row = generate_row()
        index = 0
        count = 0
        for num in users_row:
            if num == game_row[index]:
                count += 1
                index += 1
            else:
                index += 1

        current_val = results_dict[count]
        results_dict[count] = current_val + 1

    end = time()
    print(f"Time Elapsed {round(end - start, 2)}s")
    print(f"You ran {loops} iterations")
    print(f"This is equal to playing the Eurojackpot each week for {int(loops / 52)} years")

    for key, val in results_dict.items():
        round_amount = 6 if key > 3 else 2
        round_val = round((val / loops * 100), round_amount)
        print(f"Number of [{key}] | {val} | {round_val}%")

    playAgain = input("Would you like to play again? Y/N ")
    if playAgain.lower() in "yesyupya":
        pass
    else:
        print("Exiting Eurojackpot simulator, Goodbye")
        done = True
