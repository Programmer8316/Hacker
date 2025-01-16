from random import randint

def main():
    hacked = generate(8316)

    print(f"Password: {hacked[0]}\nAttempts: {hacked[1]}")

def generate(password):
    code = password
    number = 0
    generated = []
    attempts = 0

    while number != code:
        number = randint(0, 9999)

        if number not in generated:
            if number == code:
                break
            else:
                generated.append(number)
                attempts += 1
    
    return number, attempts

if __name__ == "__main__":
    main()