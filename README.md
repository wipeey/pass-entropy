# 🔐 Password Entropy Calculator

## 📝 Overview

This Python script calculates the entropy of a password, providing insights into its strength and security. It helps users understand how robust their passwords are by analyzing complexity and uniqueness.

## ✨ Features

- Calculates password entropy in bits
- Checks against common password lists
- Provides strength assessment
- Offers security recommendations
- Uses getpass for secure password input

## 🛠️ Requirements

- Python 3.x
- `rockyou.txt` wordlist (optional)
- Libraries: 
  - `math`
  - `getpass`
  - `re`

## 🚀 Usage

```bash
python3 password_entropy.py
```

## 🔍 How It Works

1. Input password securely
2. Ability to check against common password list
3. Calculate entropy (log2(charset**length)) based on:
   - Password length
   - Character types
4. Display entropy and strength rating

## 🌟 Entropy Ratings

- 0-35 bits: Very Weak
- 36-59 bits: Weak
- 60-119 bits: Strong
- 120+ bits: Very Strong

## 💡 Security Tips

If entropy is low:
- Use longer passwords (12 characters minimum)
- Mix character types (lowercase, uppercase, numbers, special characters...)
- Avoid common words
- Use unique combinations

### 📨 Contact me on Discord → sctwck
