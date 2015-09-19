#!/usr/bin/python
#-=- encoding: utf-8 -=-

# Abaixo defina os campos do banco de dados
def acesso():
	imap 		='mail.sinestec.com.br'
        imaplogin	='mailflow'
	imapsenha	='senha@123'
	smtp		='smtp.gmail.com'
	smtpporta	='465'
	smtplogin 	='mailflowsinestec'
	smtpmail	='mailflowsinestec@gmail.com'
	smtpsenha 	='SinesteC1@'

	return imap, imaplogin, imapsenha, smtp, smtpporta, smtplogin, smtpmail, smtpsenha


#print acesso('eva')
