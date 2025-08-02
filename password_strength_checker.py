import tkinter as tk
from tkinter import ttk
import string
import random
import re

class PasswordStrengthChecker:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """Configure the main window"""
        self.root.title("Password Strength Checker")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Center the window on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.root.winfo_width() // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.root.winfo_height() // 2)
        self.root.geometry(f"+{x}+{y}")
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
    def create_widgets(self):
        """Create and layout all UI widgets"""
        # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Password Strength Checker",
            font=("Arial", 18, "bold"),
            fg="#2c3e50"
        )
        title_label.pack(pady=(0, 20))
        
        # Password input section
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        password_label = tk.Label(
            input_frame,
            text="Enter Password:",
            font=("Arial", 12),
            fg="#34495e"
        )
        password_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            input_frame,
            textvariable=self.password_var,
            font=("Arial", 12),
            show='*',
            width=40
        )
        self.password_entry.pack(fill=tk.X, pady=(0, 10))
        
        # Bind Enter key to check password
        self.password_entry.bind('<Return>', lambda e: self.check_password())
        
        # Show/Hide password checkbox
        self.show_password_var = tk.BooleanVar()
        show_checkbox = tk.Checkbutton(
            input_frame,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
            font=("Arial", 10)
        )
        show_checkbox.pack(anchor=tk.W)
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=(10, 20))
        
        self.check_button = tk.Button(
            buttons_frame,
            text="Check Strength",
            command=self.check_password,
            font=("Arial", 11, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=8,
            cursor="hand2"
        )
        self.check_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.generate_button = tk.Button(
            buttons_frame,
            text="Generate Strong Password",
            command=self.generate_and_fill_password,
            font=("Arial", 11, "bold"),
            bg="#27ae60",
            fg="white",
            padx=20,
            pady=8,
            cursor="hand2"
        )
        self.generate_button.pack(side=tk.LEFT)
        
        # Results section
        results_frame = ttk.Frame(main_frame)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Strength display
        strength_frame = ttk.Frame(results_frame)
        strength_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.strength_label = tk.Label(
            strength_frame,
            text="Strength: Not Checked",
            font=("Arial", 14, "bold"),
            fg="#7f8c8d"
        )
        self.strength_label.pack()
        
        self.score_label = tk.Label(
            strength_frame,
            text="Score: -/10",
            font=("Arial", 12),
            fg="#7f8c8d"
        )
        self.score_label.pack(pady=(5, 0))
        
        # Progress bar for visual score representation
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            strength_frame,
            variable=self.progress_var,
            maximum=10,
            length=300,
            mode='determinate'
        )
        self.progress_bar.pack(pady=(10, 0))
        
        # Feedback section
        feedback_label = tk.Label(
            results_frame,
            text="Feedback & Suggestions:",
            font=("Arial", 12, "bold"),
            fg="#34495e"
        )
        feedback_label.pack(anchor=tk.W, pady=(10, 5))
        
        # Scrollable text widget for feedback
        feedback_frame = ttk.Frame(results_frame)
        feedback_frame.pack(fill=tk.BOTH, expand=True)
        
        self.feedback_text = tk.Text(
            feedback_frame,
            height=12,
            width=50,
            font=("Arial", 10),
            wrap=tk.WORD,
            bg="#f8f9fa",
            fg="#2c3e50",
            padx=10,
            pady=10
        )
        
        scrollbar = ttk.Scrollbar(feedback_frame, orient=tk.VERTICAL, command=self.feedback_text.yview)
        self.feedback_text.configure(yscrollcommand=scrollbar.set)
        
        self.feedback_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Make text widget read-only
        self.feedback_text.configure(state=tk.DISABLED)
        
    def toggle_password_visibility(self):
        """Toggle password visibility in the entry field"""
        if self.show_password_var.get():
            self.password_entry.configure(show='')
        else:
            self.password_entry.configure(show='*')
    
    def check_password_strength(self, password):
        """
        Analyze password strength and return score, feedback, and strength level
        Returns: tuple (score, feedback_list, strength_level)
        """
        if not password:
            return 0, ["Please enter a password to check."], "Not Checked"
        
        score = 0
        feedback = []
        
        # Length check (0-3 points)
        length = len(password)
        if length >= 12:
            score += 3
            feedback.append("✓ Excellent length (12+ characters)")
        elif length >= 8:
            score += 2
            feedback.append("✓ Good length (8+ characters)")
        elif length >= 6:
            score += 1
            feedback.append("⚠ Fair length (6+ characters)")
            feedback.append("• Consider using 8+ characters for better security")
        else:
            feedback.append("✗ Too short (less than 6 characters)")
            feedback.append("• Use at least 8 characters")
        
        # Character variety checks (1 point each)
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        
        if has_lower:
            score += 1
            feedback.append("✓ Contains lowercase letters")
        else:
            feedback.append("✗ Missing lowercase letters")
            feedback.append("• Add lowercase letters (a-z)")
            
        if has_upper:
            score += 1
            feedback.append("✓ Contains uppercase letters")
        else:
            feedback.append("✗ Missing uppercase letters")
            feedback.append("• Add uppercase letters (A-Z)")
            
        if has_digit:
            score += 1
            feedback.append("✓ Contains numbers")
        else:
            feedback.append("✗ Missing numbers")
            feedback.append("• Add numbers (0-9)")
            
        if has_special:
            score += 1
            feedback.append("✓ Contains special characters")
        else:
            feedback.append("✗ Missing special characters")
            feedback.append("• Add special characters (!@#$%^&*)")
        
        # Pattern checks (1 point each)
        # No repeated characters
        if not re.search(r'(.)\1{2,}', password):
            score += 1
            feedback.append("✓ No excessive repeated characters")
        else:
            feedback.append("⚠ Contains repeated characters")
            feedback.append("• Avoid repeating the same character 3+ times")
        
        # No sequential characters
        sequential_patterns = ['123', '234', '345', '456', '567', '678', '789', 
                             'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi']
        has_sequential = any(pattern in password.lower() for pattern in sequential_patterns)
        
        if not has_sequential:
            score += 1
            feedback.append("✓ No common sequential patterns")
        else:
            feedback.append("⚠ Contains sequential characters")
            feedback.append("• Avoid sequences like '123' or 'abc'")
        
        # Common password check
        common_passwords = [
            'password', '123456', '123456789', 'qwerty', 'abc123',
            'admin', 'letmein', 'welcome', 'monkey', 'dragon',
            'password123', 'admin123', '12345678', '1234567890'
        ]
        
        is_common = password.lower() in common_passwords
        contains_common = any(common in password.lower() for common in ['password', 'admin', '123456'])
        
        if not is_common and not contains_common:
            feedback.append("✓ Not a common password")
        else:
            feedback.append("✗ Contains common password elements")
            feedback.append("• Avoid common words like 'password', 'admin', '123456'")
            score = max(0, score - 2)  # Penalty for common passwords
        
        # Determine strength level
        if score >= 8:
            strength_level = "Strong"
        elif score >= 5:
            strength_level = "Medium"
        else:
            strength_level = "Weak"
        
        # Add overall recommendations
        feedback.append("")
        feedback.append("=== RECOMMENDATIONS ===")
        
        if strength_level == "Strong":
            feedback.append("🎉 Excellent! Your password is strong.")
            feedback.append("• Consider using a password manager")
            feedback.append("• Enable two-factor authentication when available")
        elif strength_level == "Medium":
            feedback.append("👍 Good password, but could be stronger.")
            feedback.append("• Try adding more character types")
            feedback.append("• Consider increasing the length")
        else:
            feedback.append("⚠ Your password needs improvement.")
            feedback.append("• Use at least 8 characters")
            feedback.append("• Include uppercase, lowercase, numbers, and symbols")
            feedback.append("• Avoid common words and patterns")
        
        return min(score, 10), feedback, strength_level
    
    def generate_password(self, length=12):
        """Generate a strong random password"""
        # Define character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special = "!@#$%^&*(),.?\":{}|<>"
        
        # Ensure at least one character from each category
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special)
        ]
        
        # Fill the rest with random characters from all categories
        all_chars = lowercase + uppercase + digits + special
        for _ in range(length - 4):
            password.append(random.choice(all_chars))
        
        # Shuffle the password to avoid predictable patterns
        random.shuffle(password)
        
        return ''.join(password)
    
    def update_ui(self, score, feedback, strength_level):
        """Update the UI with password analysis results"""
        # Update strength label and color
        colors = {
            "Weak": "#e74c3c",      # Red
            "Medium": "#f39c12",    # Orange
            "Strong": "#27ae60",    # Green
            "Not Checked": "#7f8c8d" # Gray
        }
        
        self.strength_label.configure(
            text=f"Strength: {strength_level}",
            fg=colors[strength_level]
        )
        
        self.score_label.configure(
            text=f"Score: {score}/10",
            fg=colors[strength_level]
        )
        
        # Update progress bar
        self.progress_var.set(score)
        
        # Configure progress bar style based on strength
        style = ttk.Style()
        if strength_level == "Strong":
            style.configure("TProgressbar", background="#27ae60")
        elif strength_level == "Medium":
            style.configure("TProgressbar", background="#f39c12")
        else:
            style.configure("TProgressbar", background="#e74c3c")
        
        # Update feedback text
        self.feedback_text.configure(state=tk.NORMAL)
        self.feedback_text.delete(1.0, tk.END)
        
        feedback_text = "\n".join(feedback)
        self.feedback_text.insert(1.0, feedback_text)
        self.feedback_text.configure(state=tk.DISABLED)
    
    def check_password(self):
        """Check the password strength and update UI"""
        password = self.password_var.get()
        score, feedback, strength_level = self.check_password_strength(password)
        self.update_ui(score, feedback, strength_level)
    
    def generate_and_fill_password(self):
        """Generate a strong password and fill it in the input field"""
        new_password = self.generate_password()
        self.password_var.set(new_password)
        
        # Automatically check the generated password
        self.check_password()
        
        # Show a message about the generated password
        self.feedback_text.configure(state=tk.NORMAL)
        self.feedback_text.insert(1.0, "🔑 Generated a strong 12-character password!\n\n")
        self.feedback_text.configure(state=tk.DISABLED)

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()

if __name__ == "__main__":
    main()