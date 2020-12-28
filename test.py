import Authentication

c=Authentication.IMAPCon()

host='HOST'
username='UN'
password='PASS'

conn=c.ImapLogin(host,username,password)
if conn is True:
    print('Login Success')
elif conn is False:
    print('Login Un-successful')
