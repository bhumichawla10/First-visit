#!/usr/bin/env python3
"""
Password Strength Checker GUI
A clean tkinter interface for the password strength checker.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import re
import string
import secrets
from password_strength_checker import PasswordStrengthChecker


class PasswordStrengthGUI:
    def __init__(self, root):
        self.root = root
        self.checker = PasswordStrengthChecker()
        self.setup_window()
        self.create_widgets()
        self.setup_layout()
        
    def setup_window(self):
        """Configure the main window."""
        self.root.title("🔐 Password Strength Checker")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        
        # Center the window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        # Configure style
        self.root.configure(bg='#f0f0f0')
        
        # Configure grid weights for responsive design
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        
    def create_widgets(self):
        """Create all GUI widgets."""
        # Main container frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        self.title_label = tk.Label(
            self.main_frame,
            text="🔐 Password Strength Checker",
            font=("Arial", 20, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        
        # Password entry frame
        self.entry_frame = ttk.Frame(self.main_frame)
        
        self.password_label = tk.Label(
            self.entry_frame,
            text="Enter Password:",
            font=("Arial", 12),
            bg='#f0f0f0',
            fg='#34495e'
        )
        
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            self.entry_frame,
            textvariable=self.password_var,
            font=("Arial", 12),
            show="*",
            width=40,
            relief="solid",
            bd=1
        )
        
        # Show/Hide password checkbox
        self.show_password_var = tk.BooleanVar()
        self.show_password_check = tk.Checkbutton(
            self.entry_frame,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
            font=("Arial", 10),
            bg='#f0f0f0'
        )
        
        # Buttons frame
        self.buttons_frame = ttk.Frame(self.main_frame)
        
        self.check_button = tk.Button(
            self.buttons_frame,
            text="🔍 Check Strength",
            command=self.check_password_strength,
            font=("Arial", 12, "bold"),
            bg='#3498db',
            fg='white',
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        
        self.generate_button = tk.Button(
            self.buttons_frame,
            text="🎯 Generate Strong Password",
            command=self.generate_password,
            font=("Arial", 12, "bold"),
            bg='#27ae60',
            fg='white',
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        
        self.clear_button = tk.Button(
            self.buttons_frame,
            text="🗑️ Clear",
            command=self.clear_all,
            font=("Arial", 12, "bold"),
            bg='#e74c3c',
            fg='white',
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        
        # Results frame
        self.results_frame = ttk.Frame(self.main_frame)
        
        # Strength score label
        self.strength_label = tk.Label(
            self.results_frame,
            text="Strength: Not Checked",
            font=("Arial", 14, "bold"),
            bg='#f0f0f0',
            fg='#7f8c8d',
            relief="solid",
            bd=1,
            padx=20,
            pady=10
        )
        
        # Score label
        self.score_label = tk.Label(
            self.results_frame,
            text="Score: --/10",
            font=("Arial", 12),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        
        # Feedback text area
        self.feedback_label = tk.Label(
            self.results_frame,
            text="💡 Feedback & Suggestions:",
            font=("Arial", 12, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        
        self.feedback_text = scrolledtext.ScrolledText(
            self.results_frame,
            height=12,
            width=70,
            font=("Arial", 11),
            wrap=tk.WORD,
            relief="solid",
            bd=1,
            bg='#ffffff',
            fg='#2c3e50'
        )
        
        # Bind Enter key to check password
        self.password_entry.bind('<Return>', lambda event: self.check_password_strength())
        
        # Bind real-time checking (optional - can be enabled/disabled)
        # self.password_var.trace('w', self.on_password_change)
        
    def setup_layout(self):
        """Arrange widgets in the window."""
        # Title
        self.title_label.grid(row=0, column=0, pady=(0, 20))
        
        # Password entry section
        self.entry_frame.grid(row=1, column=0, pady=(0, 20), sticky="ew")
        self.entry_frame.grid_columnconfigure(0, weight=1)
        
        self.password_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.password_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        self.show_password_check.grid(row=2, column=0, sticky="w")
        
        # Buttons section
        self.buttons_frame.grid(row=2, column=0, pady=(0, 20))
        
        self.check_button.grid(row=0, column=0, padx=(0, 10))
        self.generate_button.grid(row=0, column=1, padx=(5, 5))
        self.clear_button.grid(row=0, column=2, padx=(10, 0))
        
        # Results section
        self.results_frame.grid(row=3, column=0, sticky="nsew")
        self.results_frame.grid_columnconfigure(0, weight=1)
        self.results_frame.grid_rowconfigure(3, weight=1)
        
        self.strength_label.grid(row=0, column=0, pady=(0, 10), sticky="ew")
        self.score_label.grid(row=1, column=0, pady=(0, 10))
        self.feedback_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.feedback_text.grid(row=3, column=0, sticky="nsew")
        
    def toggle_password_visibility(self):
        """Toggle password visibility in the entry field."""
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
    
    def check_password_strength(self):
        """Check the password strength and update the display."""
        password = self.password_var.get()
        
        if not password:
            messagebox.showwarning("Warning", "Please enter a password to check.")
            return
        
        # Use the existing checker logic
        results = self.checker.evaluate_password(password)
        
        # Update strength label with color coding
        score = results['score']
        strength = results['strength'].title()
        
        if score >= 8:
            color = '#27ae60'  # Green
        elif score >= 5:
            color = '#f39c12'  # Orange
        else:
            color = '#e74c3c'  # Red
        
        self.strength_label.config(
            text=f"Strength: {strength}",
            fg=color,
            bg='#ecf0f1'
        )
        
        # Update score label
        self.score_label.config(
            text=f"Score: {score}/10",
            fg=color
        )
        
        # Update feedback text
        self.update_feedback_text(results, password)
        
    def update_feedback_text(self, results, password):
        """Update the feedback text area with detailed results."""
        self.feedback_text.delete(1.0, tk.END)
        
        # Password details
        feedback = f"📝 Password Analysis:\n"
        feedback += f"   • Length: {len(password)} characters\n"
        
        if results['details'].get('character_variety'):
            variety = results['details']['character_variety']
            feedback += f"   • Character Types: {variety['score']}/4\n"
        
        feedback += f"\n📊 Detailed Scoring:\n"
        
        # Length scoring
        if 'length' in results['details']:
            length_info = results['details']['length']
            feedback += f"   • Length Score: {length_info['score']}/4 ({length_info['category']})\n"
        
        # Character variety
        if 'character_variety' in results['details']:
            variety_info = results['details']['character_variety']
            feedback += f"   • Character Variety: {variety_info['score']}/4\n"
        
        # Penalties
        penalties = []
        if results['details'].get('blacklist', {}).get('penalty', 0) < 0:
            penalties.append(f"Blacklist: {results['details']['blacklist']['penalty']}")
        if results['details'].get('dictionary', {}).get('penalty', 0) < 0:
            penalties.append(f"Dictionary: {results['details']['dictionary']['penalty']}")
        if results['details'].get('patterns', {}).get('penalty', 0) < 0:
            penalties.append(f"Patterns: {results['details']['patterns']['penalty']}")
        
        if penalties:
            feedback += f"   • Penalties: {', '.join(penalties)}\n"
        
        # Bonus points
        if results['details'].get('length_bonus'):
            feedback += f"   • Length Bonus: +{results['details']['length_bonus']}\n"
        
        # Suggestions
        if results['suggestions']:
            feedback += f"\n💡 Suggestions for Improvement:\n"
            for i, suggestion in enumerate(results['suggestions'], 1):
                feedback += f"   {i}. {suggestion}\n"
        else:
            feedback += f"\n✅ Excellent! Your password meets all security criteria!\n"
        
        # Generate secure password suggestion if weak
        if results['score'] < 5:
            secure_password = self.checker.generate_secure_password()
            feedback += f"\n🎯 Suggested Secure Password:\n"
            feedback += f"   {secure_password}\n"
            feedback += f"   (Copy this randomly generated secure password)\n"
        
        self.feedback_text.insert(tk.END, feedback)
        
    def generate_password(self):
        """Generate a strong password and display it."""
        try:
            # Generate password with different lengths randomly
            length = secrets.choice([12, 16, 20])
            password = self.checker.generate_secure_password(length)
            
            # Set the generated password in the entry field
            self.password_var.set(password)
            
            # Automatically check the generated password
            self.check_password_strength()
            
            # Show success message
            messagebox.showinfo(
                "Password Generated", 
                f"A secure {length}-character password has been generated!\n\n"
                f"Password: {password}\n\n"
                f"(The password has been set in the input field and analyzed)"
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate password: {str(e)}")
    
    def clear_all(self):
        """Clear all fields and reset the interface."""
        self.password_var.set("")
        self.strength_label.config(
            text="Strength: Not Checked",
            fg='#7f8c8d',
            bg='#f0f0f0'
        )
        self.score_label.config(
            text="Score: --/10",
            fg='#7f8c8d'
        )
        self.feedback_text.delete(1.0, tk.END)
        self.feedback_text.insert(tk.END, "Enter a password and click 'Check Strength' to see analysis...")
        self.password_entry.focus()
    
    def on_password_change(self, *args):
        """Optional: Real-time password checking as user types."""
        # Uncomment to enable real-time checking
        # password = self.password_var.get()
        # if password:
        #     self.check_password_strength()
        pass


def main():
    """Main function to run the GUI application."""
    try:
        root = tk.Tk()
        app = PasswordStrengthGUI(root)
        
        # Add some initial text to feedback area
        app.feedback_text.insert(tk.END, 
            "Welcome to the Password Strength Checker! 🔐\n\n"
            "Enter a password and click 'Check Strength' to see detailed analysis...\n\n"
            "Features:\n"
            "• Real-time strength scoring (0-10)\n"
            "• Character variety analysis\n"
            "• Common password detection\n"
            "• Pattern and repetition checking\n"
            "• Personalized improvement suggestions\n"
            "• Secure password generator\n\n"
            "Your password is never stored or transmitted anywhere!"
        )
        
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror("Application Error", f"Failed to start application: {str(e)}")


if __name__ == "__main__":
    main()