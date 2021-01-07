import adapter
import ldap
import imaplib
import os
import socket
import tldextract
import configparser

cfg=configparser.ConfigParser()
cfg.read(os.getcwd()+'\conn.conf')

class Strategy:
    def IMAP(self,h,un,ps,prt):
        try:
            imp=imaplib.IMAP4(h,prt)
            imp.login(un,ps)
            adapter.Logger.LogVerbose(1,un,h)
            return True
        except imaplib.IMAP4.error:
            adapter.Logger.LogVerbose(0,un,h)
            return False
        imp.close()

    def SMBAD(self,uri,un,ps,prt):
        # Validation URI parameter
        # Validation while using IP as Domain Controller , it's not recommend
        if uri.replace('.','').isnumeric() == True:
            adapter.Logger.LogVerbose(3,un,uri)
            return False

        # Validation if using subdomain
        # Depending of Server NetBIOS Name
        dc=uri.split('.')
        if tldextract.extract(uri).subdomain is not '':
            username='%s@%s' % (un,'.'.join(dc[1:]))
            dn=[]
            for i in dc[1:]:
                dn.append(str(i))
        else:
            username='%s@%s' % (un,'.'.join(dc[0:]))
            dn=[]
            for i in dc[0:]:
                dn.append(str(i))

        # Mastering DN
        bj=',DC='.join(dn)
        base_dn=str('DC='+bj)

        addr=socket.gethostbyname(dc[0].upper())
        # attr=['memberOf']
        l=ldap.initialize('ldap://%s' % addr)
        if cfg['SMBAD']['Version'] == '3':
            l.protocol_version=ldap.VERSION3
        l.set_option(ldap.OPT_REFERRALS,prt)
        try:
            l.simple_bind_s(username,ps)

            # testing ldap connection
            # auth=l.search_s(base_dn,ldap.SCOPE_SUBTREE,'(objectClasas=*)',attr)
            # for dn,entry in auth:
            #     print('Processing',repr(entry))
            adapter.Logger.LogVerbose(1,un,uri)
            return True
        except ldap.INVALID_CREDENTIALS:
            adapter.Logger.LogVerbose(0,un,uri)
            return False
