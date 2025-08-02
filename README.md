# 🔐 Password Strength Checker

A comprehensive password strength analysis tool with both command-line and GUI interfaces. This tool evaluates password security and provides personalized suggestions for improvement.

## ✨ Features

- **Comprehensive Scoring System**: 0-10 point scale based on multiple criteria
- **Length Analysis**: Evaluates password length (weak < 8, medium 8-12, strong 12+)
- **Character Variety Check**: Requires uppercase, lowercase, numbers, and symbols
- **Blacklist Detection**: Identifies common weak passwords and patterns
- **Dictionary Word Detection**: Warns against common dictionary words
- **Pattern Recognition**: Detects repetition and sequential patterns
- **Secure Password Generator**: Creates cryptographically secure passwords
- **Real-time Feedback**: Provides specific improvement suggestions
- **Multiple Interfaces**: Command-line and graphical user interface

## 📁 Files

- `password_strength_checker.py` - Core password analysis engine
- `password_gui.py` - Tkinter GUI application
- `demo_examples.py` - Demo script with test cases
- `README.md` - This documentation

## 🚀 Quick Start

### Command Line Interface

Run the interactive command-line version:

```bash
python3 password_strength_checker.py
```

Features:
- Hidden password input for security
- Detailed analysis and scoring
- Color-coded strength indicators
- Automatic secure password suggestions for weak passwords

### Graphical User Interface

Launch the modern GUI application:

```bash
python3 password_gui.py
```

GUI Features:
- Clean, intuitive interface
- Password visibility toggle
- Real-time color-coded feedback
- Detailed analysis in scrollable text area
- One-click secure password generation
- Responsive design

### Demo Examples

See the tool in action with various password examples:

```bash
python3 demo_examples.py
```

## 📊 Scoring System

### Length Scoring (4 points max)
- **< 8 characters**: 1 point (Weak)
- **8-12 characters**: 3 points (Medium)  
- **12+ characters**: 4 points (Strong)
- **Bonus**: +1 for 16+ chars, +2 for 20+ chars

### Character Variety (4 points max)
- **Uppercase letters (A-Z)**: +1 point
- **Lowercase letters (a-z)**: +1 point
- **Numbers (0-9)**: +1 point
- **Special symbols (!@#$...)**: +1 point

### Security Penalties
- **Common passwords**: -2 points (password, 123456, etc.)
- **Dictionary words**: -0.5 points per word
- **Repetitive patterns**: -1 point (aaa, 123123)
- **Sequential patterns**: -0.5 points (abc, 123, qwe)

### Final Strength Categories
- **8-10 points**: Strong 🟢
- **5-7 points**: Medium 🟡  
- **3-4 points**: Weak 🟠
- **0-2 points**: Very Weak 🔴

## 🛡️ Security Features

### Blacklist Protection
Detects common weak passwords including:
- Common passwords (password, admin, 123456)
- Keyboard patterns (qwerty, asdf)
- Common words (welcome, login, master)
- Sport teams (football, basketball)

### Pattern Detection
- Repeated characters (aaa, 111)
- Sequential numbers (123, 456)
- Sequential letters (abc, def)
- Keyboard sequences (qwe, asd)
- Internal pattern repetition

### Secure Password Generation
- Uses `secrets` module for cryptographic randomness
- Guarantees character variety
- Configurable length (12-20+ characters)
- No ambiguous characters by default

## 🎨 GUI Interface Details

### Components
- **Title**: Clear application branding
- **Password Entry**: Masked input with show/hide toggle
- **Check Strength Button**: Analyzes entered password
- **Generate Password Button**: Creates secure passwords
- **Clear Button**: Resets all fields
- **Strength Display**: Color-coded strength indicator
- **Score Display**: Numerical score out of 10
- **Feedback Area**: Detailed analysis and suggestions

### Styling
- Modern flat design with professional colors
- Responsive layout that adapts to window resizing
- Color-coded feedback (green/yellow/red)
- Clean typography and spacing
- Intuitive keyboard shortcuts (Enter to check)

## 💡 Usage Examples

### Example 1: Weak Password
```
Input: "password123"
Score: 2/10 - WEAK
Issues: Common word, insufficient variety
Suggestions: Add symbols, avoid dictionary words
```

### Example 2: Medium Password  
```
Input: "MyPassword1!"
Score: 6/10 - MEDIUM
Issues: Contains dictionary word
Suggestions: Replace common words with random characters
```

### Example 3: Strong Password
```
Input: "Tr0ub4dor&3"
Score: 9/10 - STRONG
Analysis: Excellent variety and length
```

## 🔧 Customization

### Adding Custom Blacklist Words
Edit the `blacklist_words` set in the `PasswordStrengthChecker` class:

```python
self.blacklist_words = {
    'password', 'admin', 'your_custom_word'
}
```

### Adjusting Scoring Weights
Modify scoring functions in `password_strength_checker.py`:
- `check_length()` - Length scoring
- `check_character_variety()` - Character type scoring  
- `check_blacklist()` - Common password penalties
- `check_patterns_and_repetition()` - Pattern penalties

### GUI Appearance
Customize colors and fonts in `password_gui.py`:
- Window background: `self.root.configure(bg='#f0f0f0')`
- Button colors: `bg='#3498db'`, `fg='white'`
- Fonts: `font=("Arial", 12, "bold")`

## 🐍 Requirements

- Python 3.6+
- tkinter (usually included with Python)
- Standard library modules: `re`, `string`, `secrets`, `getpass`

No external dependencies required!

## 🚀 Advanced Usage

### Integration into Other Projects
```python
from password_strength_checker import PasswordStrengthChecker

checker = PasswordStrengthChecker()
results = checker.evaluate_password("your_password")
print(f"Score: {results['score']}/10")
print(f"Strength: {results['strength']}")
print(f"Suggestions: {results['suggestions']}")
```

### Batch Password Testing
```python
passwords = ["weak1", "Better123!", "VeryStr0ng!P@ssw0rd"]
for password in passwords:
    results = checker.evaluate_password(password)
    print(f"{password}: {results['score']}/10")
```

## 🔒 Security Notes

- Passwords are never stored or logged
- Uses cryptographically secure random generation
- GUI masks password input by default
- All analysis is performed locally
- No network communication

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional language support
- More sophisticated pattern detection
- Integration with password managers
- Mobile app version
- Additional security criteria

---

**Stay Secure! 🔐**