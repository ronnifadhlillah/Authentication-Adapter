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
    def IMAP(self,uri,un,ps,prt):
        DomainValidate(un,uri)
        username='%s@%s' % (un,'.'.join(dc[0:]))
        try:
            imp=imaplib.IMAP4(username,prt)
            imp.login(username,ps)
            adapter.Logger.LogVerbose(1,username,uri)
            return True
        except imaplib.IMAP4.error:
            adapter.Logger.LogVerbose(0,username,uri)
            return False
        imp.close()

    def SMBAD(self,uri,un,ps,prt):
        DomainValidate(un,uri)
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
        # attr=['memberOf'] --> For testing the AD
        l=ldap.initialize('ldap://%s' % addr)
        l.protocol_version=ldap.VERSION3    
        l.set_option(ldap.OPT_REFERRALS,prt)
        try:
            l.simple_bind_s(username,ps)
            # testing ldap connection --> For testing the AD
            # auth=l.search_s(base_dn,ldap.SCOPE_SUBTREE,'(objectClasas=*)',attr) --> For testing the AD
            # for dn,entry in auth: --> For testing the AD
            #     print('Processing',repr(entry)) --> For testing the AD
            adapter.Logger.LogVerbose(1,un,uri)
            return True
        except ldap.INVALID_CREDENTIALS:
            adapter.Logger.LogVerbose(0,un,uri)
            return False

        def DomainValidate(un,uri):
            # Validation URI parameter
            # Validation if input using IP as Domain Controller , it's not recommend
            if uri.replace('.','').isnumeric() == True:
                adapter.Logger.LogVerbose(3,un,uri)
                return False
            #Validation port on IMAP
            prt=list(995,993,465,143a)
            if cfg['IMAP']['Port'] not in prt:
                adapter.Logger.LogVerbose(0,un,uri)
                return False
