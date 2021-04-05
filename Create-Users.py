
unCompile = """Anthony Loneliano,Rand0Num
Biggus Dickus,Rand0Num
Nick Mullen,Rand0Num
Stavvy Baby,Rand0Num
Jeff Mangum,Rand0Num
Alexandria Ocasio Cortez,Rand0Num
Hakeem Olajuwon,Rand0Num
Kareem Abdul-Jabbar,Rand0Num"""

Compile = dict(x.split(",") for x in unCompile.split("\n"))

def name(s):

    l = s.split()
    new = ""
    new = s[0] + l[-1]
    return new.lower() 
      
for i in Compile:
    upn = name(i)
    print(upn)
    """"
    print('$secure = "{}" | ConvertTo-SecureString -AsPlainText -Force'.format(Compile[i]))
    print('$name = "{}"'.format(i))
    print('$upn = "{}"'.format(upn))
    print('$user = "{}@crystalosc.com"'.format(upn))
    print('New-AdUser -name $name -Enabled $TRUE -SamAccountName $upn -AccountPassword $secure -UserPrincipalName {}'.format(upn) + '@crystalosc.com')
    print('Add-ADGroupMember -Identity sec.sys.txcosc.remote -Members {}'.format(upn))
    print('Add-ADGroupMember -Identity sec.sys.amkai -Members {}'.format(upn))
    print("For user {}, the username is {}@crystalosc.com and the password is {}.".format(i,upn,Compile[i]))
    """