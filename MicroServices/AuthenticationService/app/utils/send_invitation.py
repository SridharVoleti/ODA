from flask_mail import Message

from app import mail


def send_invitation_email(email, token):
    try :
        invite_link = f"localhost:5000/register/{token}"
        message = Message("You're Invited to Join", recipients=[email])
        message.body = f"Click the link to create your account: {invite_link}"
        mail.send(message)  # Send the email with Flask-Mail
    except Exception as e:
        print(f"Exception in sending invitation email: {e}")