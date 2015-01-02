# Import smtplib for the actual sending function
import smtplib

#recipient == recipient's email address
#sender == my email address & password == password for sender account
recipient = 'sample_recipient@gmail.com'
sender = 'sample_sender@gmail.com'
password = 'sample_password'

try:
	# Specify host & port for gmail
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	#Identify yourself to an ESMTP server using EHLO
	smtpserver.ehlo()
	smtpserver.starttls()
	#Log in on an SMTP server that requires authentication
	smtpserver.login(sender, password)

	#smtplib doesn't automatically include a From: header, so you have to put one in yourself
	header = 'To:' + recipient + '\n' + 'From: ' + sender + '\n' + 'Subject: Send email with simple text message \n'
	#Body of email 
	msg = header + '\n Text line 1.' + '\n Text line 2.'
	smtpserver.sendmail(sender, recipient, msg)

	#Terminate the SMTP session and close the connection
	smtpserver.quit()
	print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"
