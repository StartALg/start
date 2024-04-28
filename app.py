from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email address
app.config['MAIL_PASSWORD'] = 'your_password'  # Replace with your email password

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    meeting_title = request.form['meetingTitle']
    meeting_datetime = request.form['meetingDateTime']
    person_name = request.form['personName']
    person_email = request.form['personEmail']
    comments = request.form['comments']

    # Compose email message
    msg = Message('Meeting Reservation Details', sender='your_email@example.com', recipients=[person_email])
    msg.body = f'''Hello {person_name},

Thank you for reserving a meeting. Below are the details:

Meeting Title: {meeting_title}
Meeting Date and Time: {meeting_datetime}
Your Name: {person_name}
Your Email: {person_email}
Additional Comments: {comments}

You will be discussing with the tutor at the meeting.
'''

    # Send email
    try:
        mail.send(msg)
        return 'Email sent successfully.'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
