#!/usr/bin/env python3
"""
Password Strength Checker
A comprehensive tool to evaluate password strength and provide improvement suggestions.
"""

import re
import string
import secrets
import getpass
from typing import Dict, List, Tuple


class PasswordStrengthChecker:
    def __init__(self):
        # Common weak passwords and patterns
        self.blacklist_words = {
            'password', 'admin', 'user', 'guest', 'test', 'demo',
            '1234', '12345', '123456', '1234567', '12345678',
            'qwerty', 'abc123', 'letmein', 'welcome', 'monkey',
            'football', 'baseball', 'basketball', 'soccer',
            'master', 'dragon', 'princess', 'hello', 'login'
        }
        
        # Common dictionary words (basic set for demonstration)
        self.common_words = {
            'love', 'hate', 'good', 'bad', 'best', 'worst',
            'home', 'work', 'family', 'friend', 'money',
            'happy', 'sad', 'angry', 'peace', 'war',
            'computer', 'internet', 'email', 'phone', 'mobile'
        }
    
    def check_length(self, password: str) -> Tuple[int, str, List[str]]:
        """Check password length and return score, category, and suggestions."""
        length = len(password)
        suggestions = []
        
        if length < 8:
            score = 1
            category = "weak"
            suggestions.append("Make password at least 8 characters long")
        elif length < 12:
            score = 3
            category = "medium"
            suggestions.append("Consider making password at least 12 characters for better security")
        else:
            score = 4
            category = "strong"
        
        return score, category, suggestions
    
    def check_character_variety(self, password: str) -> Tuple[int, List[str]]:
        """Check character variety and return score and suggestions."""
        score = 0
        suggestions = []
        
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_symbol = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))
        
        if has_upper:
            score += 1
        else:
            suggestions.append("Add uppercase letters (A-Z)")
        
        if has_lower:
            score += 1
        else:
            suggestions.append("Add lowercase letters (a-z)")
        
        if has_digit:
            score += 1
        else:
            suggestions.append("Add numbers (0-9)")
        
        if has_symbol:
            score += 1
        else:
            suggestions.append("Add special symbols (!@#$%^&* etc.)")
        
        return score, suggestions
    
    def check_blacklist(self, password: str) -> Tuple[int, List[str]]:
        """Check against common weak passwords."""
        password_lower = password.lower()
        suggestions = []
        
        # Check for exact matches
        if password_lower in self.blacklist_words:
            suggestions.append("Avoid common passwords like 'password', '123456', etc.")
            return -2, suggestions
        
        # Check for partial matches
        for word in self.blacklist_words:
            if word in password_lower and len(word) >= 4:
                suggestions.append(f"Avoid using common words like '{word}' in your password")
                return -1, suggestions
        
        return 0, suggestions
    
    def check_dictionary_words(self, password: str) -> Tuple[int, List[str]]:
        """Check for common dictionary words."""
        password_lower = password.lower()
        suggestions = []
        found_words = []
        
        for word in self.common_words:
            if word in password_lower and len(word) >= 4:
                found_words.append(word)
        
        if found_words:
            suggestions.append(f"Avoid dictionary words: {', '.join(found_words)}")
            return -len(found_words) * 0.5, suggestions
        
        return 0, suggestions
    
    def check_patterns_and_repetition(self, password: str) -> Tuple[int, List[str]]:
        """Check for patterns and repetitive characters."""
        suggestions = []
        penalty = 0
        
        # Check for repeated characters (3+ in a row)
        repeated_chars = re.findall(r'(.)\1{2,}', password)
        if repeated_chars:
            penalty -= 1
            suggestions.append("Avoid repeating characters (e.g., 'aaa', '111')")
        
        # Check for sequential patterns
        sequential_patterns = [
            '123', '234', '345', '456', '567', '678', '789',
            'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi',
            'qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio'
        ]
        
        password_lower = password.lower()
        for pattern in sequential_patterns:
            if pattern in password_lower:
                penalty -= 0.5
                suggestions.append("Avoid sequential patterns (e.g., '123', 'abc', 'qwe')")
                break
        
        # Check for repeated patterns
        for i in range(2, len(password) // 2 + 1):
            pattern = password[:i]
            if password.count(pattern) >= 2:
                penalty -= 1
                suggestions.append("Avoid repeating patterns within password")
                break
        
        return penalty, suggestions
    
    def generate_secure_password(self, length: int = 16) -> str:
        """Generate a secure random password."""
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
        
        # Ensure at least one character from each category
        password = [
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.digits),
            secrets.choice("!@#$%^&*")
        ]
        
        # Fill the rest randomly
        for _ in range(length - 4):
            password.append(secrets.choice(alphabet))
        
        # Shuffle the password
        secrets.SystemRandom().shuffle(password)
        return ''.join(password)
    
    def evaluate_password(self, password: str) -> Dict:
        """Evaluate password strength and return comprehensive results."""
        if not password:
            return {
                'score': 0,
                'max_score': 10,
                'strength': 'very weak',
                'suggestions': ['Enter a password'],
                'details': {}
            }
        
        total_score = 0
        all_suggestions = []
        details = {}
        
        # Length check (4 points max)
        length_score, length_category, length_suggestions = self.check_length(password)
        total_score += length_score
        all_suggestions.extend(length_suggestions)
        details['length'] = {'score': length_score, 'category': length_category}
        
        # Character variety check (4 points max)
        variety_score, variety_suggestions = self.check_character_variety(password)
        total_score += variety_score
        all_suggestions.extend(variety_suggestions)
        details['character_variety'] = {'score': variety_score, 'max': 4}
        
        # Blacklist check (penalty)
        blacklist_score, blacklist_suggestions = self.check_blacklist(password)
        total_score += blacklist_score
        all_suggestions.extend(blacklist_suggestions)
        details['blacklist'] = {'penalty': blacklist_score}
        
        # Dictionary check (penalty)
        dict_score, dict_suggestions = self.check_dictionary_words(password)
        total_score += dict_score
        all_suggestions.extend(dict_suggestions)
        details['dictionary'] = {'penalty': dict_score}
        
        # Pattern check (penalty)
        pattern_score, pattern_suggestions = self.check_patterns_and_repetition(password)
        total_score += pattern_score
        all_suggestions.extend(pattern_suggestions)
        details['patterns'] = {'penalty': pattern_score}
        
        # Bonus points for longer passwords
        if len(password) >= 16:
            total_score += 1
            details['length_bonus'] = 1
        elif len(password) >= 20:
            total_score += 2
            details['length_bonus'] = 2
        
        # Normalize score to 0-10 range
        total_score = max(0, min(10, total_score))
        
        # Determine strength category
        if total_score >= 8:
            strength = 'strong'
        elif total_score >= 5:
            strength = 'medium'
        elif total_score >= 3:
            strength = 'weak'
        else:
            strength = 'very weak'
        
        # Remove duplicate suggestions
        all_suggestions = list(dict.fromkeys(all_suggestions))
        
        return {
            'score': total_score,
            'max_score': 10,
            'strength': strength,
            'suggestions': all_suggestions,
            'details': details
        }
    
    def print_results(self, results: Dict, password: str):
        """Print formatted results to console."""
        print("\n" + "="*60)
        print("🔐 PASSWORD STRENGTH ANALYSIS")
        print("="*60)
        
        # Score display
        score = results['score']
        max_score = results['max_score']
        strength = results['strength'].upper()
        
        # Color coding (using ANSI color codes)
        if score >= 8:
            color = '\033[92m'  # Green
        elif score >= 5:
            color = '\033[93m'  # Yellow
        else:
            color = '\033[91m'  # Red
        
        reset = '\033[0m'
        
        print(f"📊 Score: {color}{score}/{max_score}{reset}")
        print(f"💪 Strength: {color}{strength}{reset}")
        
        # Password details
        print(f"\n📝 Password Details:")
        print(f"   Length: {len(password)} characters")
        
        if results['details'].get('character_variety'):
            variety = results['details']['character_variety']
            print(f"   Character Types: {variety['score']}/4")
        
        # Suggestions
        if results['suggestions']:
            print(f"\n💡 Suggestions for Improvement:")
            for i, suggestion in enumerate(results['suggestions'], 1):
                print(f"   {i}. {suggestion}")
        else:
            print(f"\n✅ Your password meets all security criteria!")
        
        # Generate secure password if weak
        if score < 5:
            print(f"\n🎯 Suggested Secure Password:")
            secure_password = self.generate_secure_password()
            print(f"   {secure_password}")
            print(f"   (This is a randomly generated secure password)")
        
        print("="*60)


def main():
    """Main function to run the password strength checker."""
    checker = PasswordStrengthChecker()
    
    print("🔐 Welcome to the Password Strength Checker!")
    print("This tool will evaluate your password and provide improvement suggestions.")
    print("Your password will be hidden as you type for security.\n")
    
    while True:
        try:
            # Get password input (hidden)
            password = getpass.getpass("Enter password to check (or 'quit' to exit): ")
            
            if password.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye! Stay secure!")
                break
            
            # Evaluate password
            results = checker.evaluate_password(password)
            
            # Display results
            checker.print_results(results, password)
            
            # Ask if user wants to check another password
            print("\nWould you like to check another password? (y/n): ", end="")
            choice = input().lower()
            if choice not in ['y', 'yes']:
                print("👋 Goodbye! Stay secure!")
                break
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Stay secure!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()