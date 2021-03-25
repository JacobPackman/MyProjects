
unCompile = """Angela Mattioda,VRnp8Hm
Aleta Paul,uvfPm52
Michelle McCord,bAS6gaS
Maggie Raesz,9i6afPX
Krissy Eggemeyer,D5KJWii
Alicia Cortez,Pe4dSU6
Lea Young,qvTPR2Z
Crissy Bates,uM3qwTC
Jeremy Parlington,8LdAGch
Liza Avina,3oqs6DU
Lori Bahr,nzv93eD
Mark Binder,iA6Rpeb
Katryna Yaworski,hEA4nm4
Samantha Adams,4hpDDwn
Sarah Rodriguez,77Euub3
Janine Nelms,9eLPhcn
Amy Miller,8xNJNe3
Jordan Hawkins,W4Srzs8
Jocelyn Preston,g78PRhs
James Webster,8ihbcZL"""

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