import random

ranks = ["نمونه‌ای", "بسیار خوبی", "خوب", "قبول", "با شانس بردی!"]

play = True
while play:
    secret = random.randint(1, 100)
    won = False
    attempt = 1

    while attempt <= 5:
        print("تلاش", attempt, "از 5")
        print("جان باقی‌مانده:", 6 - attempt)
        text = input("حدس خود را وارد کن: ")

        if not text.isdigit():
            print("ورودی نامعتبر است")
            continue

        guess = int(text)
        if guess < 1 or guess > 100:
            print("عدد باید بین 1 تا 100 باشد")
            continue

        if guess == secret:
            print("برنده شدی!")
            print("رتبه:", ranks[attempt - 1])
            won = True
            break

        if guess < secret:
            print("بزرگ‌تر وارد کن")
        else:
            print("کوچک‌تر وارد کن")

        diff = abs(guess - secret)
        if diff <= 5:
            print("خیلی نزدیکی!")
        elif diff <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")

        attempt += 1

    if not won:
        print("باختی!")
        print("عدد مخفی", secret, "بود")

    answer = input("دوباره بازی می‌کنی؟ (بله/خیر): ")
    while answer != "بله" and answer != "خیر":
        answer = input("فقط بله یا خیر وارد کن: ")
    if answer == "خیر":
        play = False