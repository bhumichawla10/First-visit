#!/usr/bin/env python3
"""
Demo Examples for Password Strength Checker
Shows various password examples and their strength analysis.
"""

from password_strength_checker import PasswordStrengthChecker


def demo_password_examples():
    """Demonstrate password strength checking with various examples."""
    checker = PasswordStrengthChecker()
    
    # Test passwords with different strength levels
    test_passwords = [
        ("123", "Very weak - only numbers, too short"),
        ("password", "Weak - common word, no variety"),
        ("Password123", "Medium - has variety but contains dictionary word"),
        ("MyStr0ng!P@ssw0rd", "Strong - good length and variety"),
        ("P@$$w0rd!2023", "Medium - good but has common patterns"),
        ("Tr0ub4dor&3", "Strong - inspired by famous XKCD comic"),
        ("correct horse battery staple", "Medium - long but only lowercase"),
        ("C0rr3ct-H0rs3-B@tt3ry-St@pl3!", "Very Strong - long with great variety"),
        ("admin123", "Very weak - common admin password"),
        ("qwerty", "Very weak - keyboard pattern"),
        ("aaaaaa", "Very weak - repetitive"),
        ("abcdefg", "Weak - sequential pattern"),
    ]
    
    print("🔐 Password Strength Checker Demo")
    print("=" * 80)
    print()
    
    for password, description in test_passwords:
        print(f"Password: '{password}'")
        print(f"Expected: {description}")
        
        results = checker.evaluate_password(password)
        score = results['score']
        strength = results['strength']
        
        # Color coding for terminal
        if score >= 8:
            color = '\033[92m'  # Green
        elif score >= 5:
            color = '\033[93m'  # Yellow
        else:
            color = '\033[91m'  # Red
        reset = '\033[0m'
        
        print(f"Result: {color}Score {score}/10 - {strength.upper()}{reset}")
        
        if results['suggestions']:
            print("Suggestions:")
            for i, suggestion in enumerate(results['suggestions'][:3], 1):  # Show top 3
                print(f"  {i}. {suggestion}")
        
        print("-" * 80)


def demo_password_generation():
    """Demonstrate secure password generation."""
    checker = PasswordStrengthChecker()
    
    print("\n🎯 Secure Password Generation Demo")
    print("=" * 80)
    
    for length in [12, 16, 20]:
        password = checker.generate_secure_password(length)
        results = checker.evaluate_password(password)
        
        print(f"Generated {length}-char password: {password}")
        print(f"Strength: {results['score']}/10 - {results['strength'].upper()}")
        print()


if __name__ == "__main__":
    demo_password_examples()
    demo_password_generation()