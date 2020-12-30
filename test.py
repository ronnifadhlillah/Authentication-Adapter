import Authenticator
import configparser
import os

grp=os.path.dirname(os.path.abspath(__file__))+'\Test.conf' #You can change Test.conf with your default config folder.
cfg=configparser.ConfigParser()
cfg.read(grp)
ca=Authenticator.IMAPCon()

imap_param={
    'host':cfg['Environment']['Host'],
    'email':'ronnif@ccsi.co.',
    'password':'Tamarin2019'
}

conn=ca.ImapLogin(imap_param['host'],imap_param['email'],imap_param['password'],143)
if conn is True:
    print('Login Success')
elif conn is False:
    print('Login Un-successful')
