import imaplib
import os
import datetime

# Must create configuration file to define the imap connection

class IMAPCon:
    def ImapLogin(self,h,un,ps,prt):
        try:
            imp=imaplib.IMAP4(h,143)
            imp.login(un,ps)
            IMAPCon.LogInit(IMAPCon.Stamp() +' --> ' +un+' Has been SUCCESS to login to this application via imap Host : '+h)
            return True
        except imaplib.IMAP4.error:
            IMAPCon.LogInit(IMAPCon.Stamp() +' --> ' +un+' Has been FAILED to login to this application via imap Host : '+h)
            return False

    # def ImapSslLogin(h,un,ps,prt):
    #     pass

    def Stamp():
        return datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def LogInit(desc):
        dp=os.path.dirname(os.path.abspath(__file__))+'\Log'
        if os.path.exists(dp):
            IMAPCon.LogTrace(dp,desc)
        else:
            IMAPCon.LogFileBuilder(dp,desc)

    def LogFileBuilder(dp,desc):
        # fp=os.path.dirname(os.path.abspath(__file__),'Log')
        chmod=0o777
        os.mkdir(dp,chmod)
        return IMAPCon.LogTrace(dp,desc)

    def LogTrace(dp,desc):
        fp=dp+'\Auth.Log'
        f=open(fp,'a+')
        f.write(desc+'\n')
        f.close()
