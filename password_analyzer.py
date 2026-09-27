import math


print("================================")
print("   PASSWORD SECURITY ANALYZER")
print("================================")

password = input("Enter a password: ")

# ========================================
# 1. Check password length
# ========================================

length = len(password)


# ========================================
# 2. Check character types
# ========================================

has_lowercase = any(char.islower() for char in password)
has_uppercase = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)


# ========================================
# 3. Estimate password entropy
# ========================================

character_set_size = 0

if has_lowercase:
    character_set_size += 26

if has_uppercase:
    character_set_size += 26

if has_number:
    character_set_size += 10

if has_special:
    character_set_size += 32

if character_set_size > 0:
    entropy = length * math.log2(character_set_size)
else:
    entropy = 0


# ========================================
# 4. Security Analysis
# ========================================

print("\n--- Security Analysis ---")

print("Length:", length)
print("Lowercase:", has_lowercase)
print("Uppercase:", has_uppercase)
print("Number:", has_number)
print("Special character:", has_special)
print("Estimated entropy:", round(entropy, 2), "bits")


# ========================================
# 5. Calculate password strength score
# ========================================

score = 0

if length >= 8:
    score += 1

if length >= 12:
    score += 1

if has_lowercase:
    score += 1

if has_uppercase:
    score += 1

if has_number:
    score += 1

if has_special:
    score += 1


print("\n--- Password Strength ---")
print("Score:", score, "/ 6")

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Moderate")
else:
    print("Strength: Strong")


# ========================================
# 6. Check for commonly used passwords
# ========================================

common_passwords = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "letmein",
    "welcome"
}

if password.lower() in common_passwords:
    print("Warning: This is a commonly used password.")
else:
    print("Common password check: Passed")


# ========================================
# 7. Security Recommendations
# ========================================

print("\n--- Security Recommendations ---")

if length < 8:
    print("- Use at least 8 characters.")

if length < 12:
    print("- Consider using 12 or more characters.")

if not has_lowercase:
    print("- Add lowercase letters.")

if not has_uppercase:
    print("- Add uppercase letters.")

if not has_number:
    print("- Add numbers.")

if not has_special:
    print("- Add special characters.")

if password.lower() in common_passwords:
    print("- Avoid commonly used passwords.")

if score >= 5 and password.lower() not in common_passwords:
    print("- Good password characteristics. Avoid reusing this password across accounts.")