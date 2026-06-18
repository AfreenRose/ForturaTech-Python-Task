import random

otp = random.randint(1000, 9999)

print("OTP:", otp)

for i in range(3):
    user_otp = int(input("Enter OTP: "))

    if user_otp == otp:
        print("Verified")
        break
    else:
        print("Wrong OTP")