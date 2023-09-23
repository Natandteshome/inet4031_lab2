file = open("input.txt", "r")
lines = file.readlines()
file.close()

users_data = [line.strip().split(':') for line in lines if not line.startswith('#')]

print("Printing out User Data:\n")

for user in users_data:
    print(f"The user {user[0]} has a password of {user[1]} and has userid {user[2]} and groupid {user[3]}")

for line in lines:
    if line.startswith("#User4"):
        print("User4 is skipped because it starts with a hashtag (is commented out)")

print("\nEnd of User Data")
