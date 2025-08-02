# Password Strength Checker

A comprehensive Python application built with Tkinter that analyzes password strength and provides detailed feedback to help users create secure passwords.

## Features

### 🔍 **Password Analysis**
- **Length Analysis**: Evaluates password length (6+ characters minimum, 8+ recommended, 12+ excellent)
- **Character Variety**: Checks for uppercase letters, lowercase letters, numbers, and special characters
- **Pattern Detection**: Identifies weak patterns like repeated characters and sequential patterns
- **Common Password Detection**: Flags common passwords and dictionary words
- **Smart Scoring**: Provides a score out of 10 based on multiple security criteria

### 🎨 **User Interface**
- **Clean, Intuitive Design**: Modern and responsive layout
- **Masked Input**: Password field with asterisk masking for security
- **Show/Hide Toggle**: Option to reveal password for verification
- **Color-Coded Results**: Visual strength indicators (Red=Weak, Orange=Medium, Green=Strong)
- **Progress Bar**: Visual representation of password strength score
- **Detailed Feedback**: Comprehensive suggestions for password improvement

### 🔐 **Password Generator**
- **Secure Generation**: Creates 12-character passwords using cryptographically random selection
- **Character Variety**: Includes uppercase, lowercase, numbers, and special characters
- **Automatic Analysis**: Generated passwords are automatically analyzed and scored
- **One-Click Integration**: Generated passwords are automatically filled into the input field

### ⌨️ **User Experience**
- **Keyboard Shortcuts**: Press Enter to check password strength
- **Centered Window**: Application opens in the center of the screen
- **Scrollable Feedback**: Large feedback area with scrolling for detailed suggestions
- **Real-time Updates**: Instant feedback when checking or generating passwords

## Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python)
- No external dependencies required

## Installation

### On Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

### On Other Systems:
Tkinter is typically included with Python installations. If not available, consult your system's package manager.

## Usage

### Running the Application
```bash
python3 password_strength_checker.py
```

### Using the Interface

1. **Enter a Password**: Type your password in the input field (it will be masked with asterisks)
2. **Check Strength**: Click "Check Strength" or press Enter to analyze the password
3. **Review Feedback**: Read the detailed feedback and suggestions in the scrollable text area
4. **Generate Password**: Click "Generate Strong Password" to create a secure password automatically
5. **Toggle Visibility**: Use the "Show Password" checkbox to reveal/hide the password text

### Understanding the Scoring System

The application uses a 10-point scoring system:

- **Length (0-3 points)**:
  - 12+ characters: 3 points
  - 8-11 characters: 2 points
  - 6-7 characters: 1 point
  - <6 characters: 0 points

- **Character Types (4 points total)**:
  - Lowercase letters: 1 point
  - Uppercase letters: 1 point
  - Numbers: 1 point
  - Special characters: 1 point

- **Pattern Analysis (2 points total)**:
  - No excessive repeated characters: 1 point
  - No sequential patterns: 1 point

- **Common Password Check (1 point)**:
  - Not a common/dictionary password: 1 point

- **Penalties**:
  - Common password elements: -2 points

### Strength Levels

- **Strong (8-10 points)**: Green - Excellent security
- **Medium (5-7 points)**: Orange - Good but could be stronger
- **Weak (0-4 points)**: Red - Needs improvement

## Code Structure

The application is organized into modular functions:

- `PasswordStrengthChecker`: Main application class
- `check_password_strength(password)`: Core password analysis logic
- `generate_password(length=12)`: Secure password generation
- `update_ui(score, feedback, strength_level)`: UI update functionality
- `create_widgets()`: UI layout and component creation
- `setup_window()`: Window configuration and styling

## Security Features

- **No Password Storage**: Passwords are never saved or logged
- **Masked Input**: Password field hides input by default
- **Secure Generation**: Uses Python's `random` module with proper character shuffling
- **Comprehensive Analysis**: Multiple security criteria evaluated
- **Educational Feedback**: Detailed explanations help users understand password security

## Testing

Run the included test script to verify functionality:

```bash
python3 test_password_checker.py
```

This will test various password scenarios and the password generation feature without opening the GUI.

## Examples

### Weak Password Analysis
- Input: `password123`
- Score: 4/10 (Weak)
- Issues: Common word, predictable pattern
- Suggestions: Add special characters, avoid dictionary words

### Strong Password Analysis
- Input: `Tr1cky#P@ssw0rd2024!`
- Score: 9/10 (Strong)
- Strengths: Good length, character variety, no common patterns

### Generated Password Example
- Generated: `K7#mP9$nQ2!x`
- Score: 9-10/10 (Strong)
- Features: 12 characters, all character types, randomized

## Contributing

This application is designed to be educational and beginner-friendly. The code is well-commented and structured for easy understanding and modification.

## License

This project is open source and available for educational and personal use.

## Security Note

While this tool provides good guidance for password creation, remember:
- Use a dedicated password manager for storing passwords
- Enable two-factor authentication when available
- Never reuse passwords across multiple accounts
- Consider using passphrases for memorable yet secure passwords