import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('harsvardhanguleria@gmail.com', 'Tiger_Leap_1')
server.sendmail('harshvardhanguleria@gmail.com',
                'harshvardhanguleria@yahoo.com',
                'Automated email using Python')