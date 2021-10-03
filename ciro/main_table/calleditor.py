def newSIP(sip):
    with open('/etc/asterisk/sip.conf', 'a') as config:
        config.write('\n'+'['+sip+'](ohrana)')