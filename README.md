## AUTHENTICATION ADAPTER.

This library is using to integrate between hosting or AD with your internal application. like internal webservice / operational business management or etc. <strong>This lib is not suitable for public application use.</strong>

First of all you need to create configuration (.conf) file to define the connection.

Adapter and strategy :
- CPanel & Plesk : The client authentication config for POP3 / IMAP and it's SMTP included when you join a CPanel WHM / Plesk subscription for the first time.
<strong>for sample : internetMailProtocol(IMAP/POP3).domain.co.id:993/ssl/novalidate.</strong>. The client connection config URL
  - CPanel Hosting : https://docs.cpanel.net/cpanel/email/set-up-mail-client/
  - Plesk Hosting : https://www.plesk.com/blog/various/server-wide-mail-settings-configuring-them-in-plesk/.

- Samba AD : Samba AD is written using Python LDAP URL : https://www.python-ldap.org/en/python-ldap-3.3.0/

#### BASIC USAGE
- IMAP
    ```sh
    >> import Adapter
    >> c=adapter.Strategy()
    >> conn=c.IMAP('domain.tld','santoso@domain.tld','your password',port)

    >> # Application Response
    ```
- SMBAD
    ```sh
    >> import Adapter
    >> c=adapter.Strategy()
    >> conn=c.SMBAD('domain.tld','santoso','your password',port)

    >> # Application Response
    ```

#### This repo is still developing
