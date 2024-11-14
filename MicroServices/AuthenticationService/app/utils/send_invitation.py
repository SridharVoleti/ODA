from flask_mail import Message

from app import mail


def send_invitation_email(email, token):
    try :
        invite_link = f"http://51.20.42.220/register/{token}"
        message = Message("You're Invited to Join ODA", recipients=[email])
        message.body = f"""
Dear User,

We are pleased to extend an exclusive invitation for you to join ODA. We are excited about the possibility of you becoming part of our community.

Please click the link below to accept your invitation and complete the registration process:
{invite_link}

If you have any questions or need assistance, feel free to reach out to our support team at yogeshkumarnandi@gmail.com.

We look forward to welcoming you aboard.

Warm regards,  
The ODA Team
"""
        mail.send(message)
    except Exception as e:
        print(f"Exception in sending invitation email: {e}")