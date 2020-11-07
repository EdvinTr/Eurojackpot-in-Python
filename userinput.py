def user_row_generator():
    user_row = []
    used_numbers = []

    maxn = 50
    minn = 1
    while True:
        if len(user_row) > 6:
            break
        if len(user_row) == 5:
            used_numbers.clear()
            maxn = 10
        if len(user_row) < 5:
            number = input("Enter a number between 1-50: ")
        else:
            number = input("Enter a number between 1-10: ")
        try:
            i = int(number)
            if i not in used_numbers and maxn >= i >= minn:
                user_row.append(i)
                used_numbers.append(i)
                print(user_row)
            else:
                print(user_row)
        except ValueError:
            print("Enter a valid number")
    return user_row
