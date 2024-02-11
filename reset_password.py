from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.dialogs import Messagebox
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string
import hashlib

def send_email(email, token):
    msg = MIMEMultipart()
    msg['From'] = '2022.your.account@ves.ac.in' # Your email address use only ves account
    msg['To'] = email
    msg['Subject'] = 'Password Reset Request'
    body = 'Your token is {}'.format(token)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], 'YourPassword123') # Your password. But pls enable less secure app to use this feature
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

def reset_password_request():
    email = email_entry.get()
    conn = sqlite3.connect('Form.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ?', (email,))
    if c.fetchone() is not None:
        token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        c.execute('UPDATE users SET token = ? WHERE email = ?', (token, email))
        conn.commit()
        send_email(email, token)
        Messagebox.show_info('Info', 'Email sent!')
    else:
        Messagebox.show_error('Info', 'Email not found!')

def reset_password():
    email = email_entry.get()
    token = token_entry.get()
    new_password = password_entry.get()
    hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
    conn = sqlite3.connect('Form.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? AND token = ?', (email, token))
    if c.fetchone() is not None:
        c.execute('UPDATE users SET password = ? WHERE email = ?', (hashed_password, email))
        conn.commit()
        Messagebox.show_info('Info', 'Password reset successful!')
    else:
        Messagebox.show_error('Info', 'Invalid token!')

root = Tk()
style = Style(theme='superhero')
email_label = ttk.Label(root, text='Email')
email_label.pack()
email_entry = ttk.Entry(root)
email_entry.pack()

token_label = ttk.Label(root, text='Token')
token_label.pack()
token_entry = ttk.Entry(root)
token_entry.pack()

password_label = ttk.Label(root, text='New Password')
password_label.pack()
password_entry = ttk.Entry(root, show='*')
password_entry.pack()

reset_password_request_button = ttk.Button(root, text='Reset Password Request', command=reset_password_request)
reset_password_request_button.pack()

reset_password_button = ttk.Button(root, text='Reset Password', command=reset_password)
reset_password_button.pack()

style.map('TEntry', foreground=[
    ('disabled', 'gray'),
    ('focus !disabled', 'white'),
    ('hover !disabled', 'yellow')
])

root.mainloop()