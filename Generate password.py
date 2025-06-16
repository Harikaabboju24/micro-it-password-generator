import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True, exclude_similar=False):
    if not (use_upper or use_lower or use_digits or use_special):
        return "❌ Error: At least one character set must be selected."

    similar_chars = "O0Il1|"
    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if exclude_similar:
        character_pool = ''.join(c for c in character_pool if c not in similar_chars)

    if len(character_pool) == 0:
        return "❌ No valid characters available after applying exclusions."

    password = []

    # Ensure one character from each selected type
    if use_upper:
        password.append(random.choice([c for c in string.ascii_uppercase if c not in similar_chars] if exclude_similar else string.ascii_uppercase))
    if use_lower:
        password.append(random.choice([c for c in string.ascii_lowercase if c not in similar_chars] if exclude_similar else string.ascii_lowercase))
    if use_digits:
        password.append(random.choice([c for c in string.digits if c not in similar_chars] if exclude_similar else string.digits))
    if use_special:
        password.append(random.choice([c for c in string.punctuation if c not in similar_chars] if exclude_similar else string.punctuation))

    # Fill the rest of the password
    remaining_length = length - len(password)
    password += random.choices(character_pool, k=remaining_length)

    # Shuffle to remove pattern
    random.shuffle(password)
    return ''.join(password)


def rate_password_strength(password):
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    strength = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }
    return strength.get(score, "Unknown")


def main():
    print("🔐 Advanced Password Generator 🔐")

    try:
        length = int(input("Enter password length (recommended ≥ 12): "))
    except ValueError:
        print("❌ Invalid length. Using default (12).")
        length = 12

    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    exclude_similar = input("Exclude similar-looking characters (O, 0, l, 1)? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_special, exclude_similar)
    if "Error" in password:
        print(password)
    else:
        print(f"\n🔑 Generated Password: {password}")
        print(f"📊 Strength: {rate_password_strength(password)}")

        save = input("💾 Do you want to save this password to a file? (y/n): ").strip().lower()
        if save == 'y':
            with open("generated_passwords.txt", "a") as file:
                file.write(password + "\n")
            print("✅ Password saved to 'generated_passwords.txt'")


# Run the program
if __name__ == "__main__":
    main()
