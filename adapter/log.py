import os
import datetime
import configparser

cfg=configparser.ConfigParser()
cfg.read(os.getcwd()+'\conn.conf')

class Logger:
    def Tstamp():
        return datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def LogResponse(un,h):
        res={
            0:Logger.Tstamp() +' --> ' +un+' Has been FAILED to login to this application via '+cfg['Environment']['Adapter']+' Host / AD: '+h,
            1:Logger.Tstamp() +' --> ' +un+' Has been SUCCESS to login to this application via '+cfg['Environment']['Adapter']+' Host / AD: '+h,
            2:Logger.Tstamp() +' --> The domain cannot be found or contacted. Check the AD DC server.',
            3:Logger.Tstamp() +' --> You\'re login using server IP address and that is not recommended.'
        }
        return res

    def LogVerbose(res,un,h):
        # GetResponse
        if res == 1:
            r=Logger.LogResponse(un,h)[1]
        elif res == 2:
            r=Logger.LogResponse(un,h)[2]
        else:
            r=Logger.LogResponse(un,h)[0]
        dp=os.getcwd()+'\Log'
        if os.path.exists(dp):
            Logger.WrittingLog(dp,r)
        else:
            Logger.FilePrepare(dp,r)

    def FilePrepare(dp,r):
        chmod=int(cfg['Log']['File_mode'])
        os.mkdir(dp,chmod)
        return Logger.WrittingLog(dp,r)

    def WrittingLog(dp,r):
        fp=dp+'\/'+cfg['Log']['File_name']
        f=open(fp,'a+')
        f.write(r+'\n')
        f.close()
