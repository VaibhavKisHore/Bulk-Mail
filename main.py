import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your email credentials
sender_email = "vbhvkishore@gmail.com"
password = "nsyf mfoz dsqf aigq"

# Email list
emails = [
"lk6758322@gmail.com",
]

subject = "Application for Software / Data Analyst Internship"

body = """
Dear Hiring Manager,

My name is Vaibhav Kishore, and I am currently a 6th-semester B.Tech computer science student. I am writing to express my interest in an internship opportunity at your company.

I have knowledge of Python, machine learning concepts, and data analysis. I have also worked on academic projects such as an intelligent e-commerce system that includes classification, clustering, and regression models.

I am eager to gain industry experience and contribute to real-world projects while improving my technical skills.

I have attached my resume for your review. I would be grateful for the opportunity to discuss how I can contribute to your team.

Thank you for your time and consideration.

Sincerely,
Vaibhav Kishore
Phone: +91 8076183568
Email: vbhvkishore@gmail.com
GitHub: https://github.com/VaibhavKisHore

LinkedIn: https://www.linkedin.com/in/vaibhav-kishore-23a024327?utm_source=share_via&utm_content=profile&utm_medium=member_androi

Resume link: d:\padhai\Vaibhav_Kishore_Resume_Clickable_Links.pdf
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)

for email in emails:
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    server.sendmail(sender_email, email, msg.as_string())

server.quit()

print("Emails sent successfully")