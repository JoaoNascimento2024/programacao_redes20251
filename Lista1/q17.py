import smtplib

try:
		msgFrom = str(input("Informe o e-mail de destino: "))
		smtpObj = smtplib.SMTP('smtp.outlook.com', 587)
		smtpObj.ehlo()
		smtpObj.starttls()
		msgTo = 'Email de envio'
		toPass = 'Senha'
		smtpObj.login(msgTo, toPass)
		msg = '''
		Mensagem do E-mail
		'''
		smtpObj.sendmail(msgTo,msgFrom,'Subject: Titulo do email\n{}'.format(msg))
		smtpObj.quit()
		print("Email enviado com sucesso!")
except:
		print("Erro ao enviar e-mail")