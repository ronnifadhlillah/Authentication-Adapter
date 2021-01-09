import adapter

# you can use .conf file. View ConfigParser baic usage

c=adapter.Strategy()
conn=c.SMBAD('domain.tld','santoso','your password',port)

if conn is True:
    print('Login Success')
elif conn is False:
    print('Login Un-successful')
