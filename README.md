# Password Strength Checker

A Flask web application that evaluates password strength and provides feedback to users.

## Features

- **Password Strength Analysis**: Evaluates passwords based on multiple criteria
- **Real-time Scoring**: Provides a score out of 10 for password strength
- **Strength Levels**: Categorizes passwords as Weak, Medium, or Strong
- **Detailed Feedback**: Offers specific suggestions for improving password security
- **Responsive Design**: Clean, modern UI that works on all devices
- **No JavaScript Required**: Pure HTML/CSS frontend with Flask backend

## Password Evaluation Criteria

The application checks for:
- **Length**: Minimum 6 characters, optimal 12+ characters
- **Character Types**: 
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)
- **Common Passwords**: Detects and warns against common weak passwords
- **Character Repetition**: Identifies passwords with too many repeated characters

## Project Structure

```
password-strength-checker/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   └── css/
│       └── style.css     # Stylesheet
└── README.md             # This file
```

## Installation and Setup

1. **Clone or download the project files**

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Activate the virtual environment** (if not already activated):
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the Flask application**:
   ```bash
   python app.py
   ```

3. **Access the application**:
   Open your web browser and navigate to: `http://localhost:5000`

## Usage

1. Enter a password in the input field
2. Click "Check Strength" to analyze the password
3. View the results:
   - **Score**: Numerical score out of 10
   - **Strength Level**: Visual indicator (Weak/Medium/Strong)
   - **Progress Bar**: Visual representation of strength
   - **Recommendations**: Specific feedback for improvement

## Example Password Tests

- **Weak**: `123456` → Score: 0-4, many suggestions
- **Medium**: `Password123` → Score: 5-7, some suggestions  
- **Strong**: `MySecureP@ssw0rd2024!` → Score: 8-10, minimal suggestions

## Security Notes

- Passwords are not stored or logged
- All processing happens server-side
- No password data is transmitted to external services
- This tool is for educational purposes and basic password evaluation

## Customization

You can modify the password evaluation criteria by editing the `check_password_strength()` function in `app.py`:
- Adjust scoring weights
- Add new character type checks
- Modify the common passwords list
- Change strength level thresholds