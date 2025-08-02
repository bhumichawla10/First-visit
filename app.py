from flask import Flask, render_template, request
import re
import string

app = Flask(__name__)

def check_password_strength(password):
    """
    Check password strength and return score, level, and feedback
    """
    score = 0
    feedback = []
    
    # Common weak passwords/patterns
    common_weak = [
        '123456', 'password', '123456789', 'qwerty', 'abc123',
        '111111', 'password1', 'admin', 'welcome', 'monkey',
        'letmein', '1234567890', 'Password', '12345678', '123123'
    ]
    
    # Length check
    length = len(password)
    if length >= 12:
        score += 3
    elif length >= 8:
        score += 2
    elif length >= 6:
        score += 1
    else:
        feedback.append("Password should be at least 6 characters long")
    
    # Character type checks
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_numbers = bool(re.search(r'\d', password))
    has_symbols = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\?]', password))
    
    if has_uppercase:
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z)")
        
    if has_lowercase:
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z)")
        
    if has_numbers:
        score += 1
    else:
        feedback.append("Add numbers (0-9)")
        
    if has_symbols:
        score += 2
    else:
        feedback.append("Add special characters (!@#$%^&*)")
    
    # Check for common weak passwords
    if password.lower() in [weak.lower() for weak in common_weak]:
        score = max(0, score - 3)
        feedback.append("Avoid common passwords")
    
    # Check for repeated characters
    if len(set(password)) < len(password) * 0.7:
        score = max(0, score - 1)
        feedback.append("Avoid too many repeated characters")
    
    # Determine strength level
    if score >= 8:
        level = "Strong"
        level_class = "strong"
    elif score >= 5:
        level = "Medium"
        level_class = "medium"
    else:
        level = "Weak"
        level_class = "weak"
    
    # Add positive feedback for strong passwords
    if score >= 8 and not feedback:
        feedback.append("Excellent! Your password is very strong.")
    elif score >= 5 and len(feedback) <= 1:
        feedback.append("Good password! Consider the suggestions above to make it stronger.")
    
    return {
        'score': min(score, 10),
        'level': level,
        'level_class': level_class,
        'feedback': feedback
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    password = ""
    
    if request.method == 'POST':
        password = request.form.get('password', '')
        if password:
            result = check_password_strength(password)
    
    return render_template('index.html', result=result, password=password)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)