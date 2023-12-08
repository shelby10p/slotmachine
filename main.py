import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10
ROWS = 3
COLS = 3

symbol_count = {
    "a": 2,
    "b": 4,
    "c": 8,
    "d": 16,
}

symbol_values = {
    "a": 10,
    "b": 20,
    "c": 50,
    "d": 100,
}

def get_slot_machine_spin(rows, cols, symbol_count):
    all_symbols = []
    for symbol, count in symbol_count.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = [[] for _ in range(cols)]

    for column in columns:
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" ")
            else:
                print(column[row])
    print("\n")

def calculate_winnings(columns):
    winnings = 0
    for i in range(ROWS):
        symbols_in_row = set(columns[j][i] for j in range(COLS))
        for symbol, value in symbol_values.items():
            if len(symbols_in_row) == 1 and list(symbols_in_row)[0] == symbol:
                winnings += value
    return winnings

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                return amount  # Return the amount if it's valid
            else:
                print("Amount must be greater than or equal to 0.")
        else:
            print("Please enter a valid number.")

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines  # Return the number of lines if it's valid
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a valid number.")

def get_bet():
    while True:
        amount = input(f"How much would you like to bet per line? (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount  # Return the amount if it's valid
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a valid number.")

def main():
    balance = deposit()
    while True:
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines

        if balance < total_bet:
            print("Insufficient balance. Please deposit more money.")
            balance += deposit()  # Ask to deposit more money
        else:
            balance -= total_bet
            print("\nSpinning the slot machine...\n")
            slot_machine_result = get_slot_machine_spin(ROWS, COLS, symbol_count)
            print_slot_machine(slot_machine_result)

            winnings = calculate_winnings(slot_machine_result)
            if winnings > 0:
                balance += winnings
                print(f"Congratulations! You won ${winnings}.")
            else:
                print("Sorry, you didn't win this time. Try again later.")

            print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
            print(f"Remaining balance: ${balance}\n")

if __name__ == "__main__":
    main()

