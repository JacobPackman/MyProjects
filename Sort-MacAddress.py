import re


test = """
B4-47-5E-23-80-00    1 Self
F8-73-A2-A2-FC-01    1 Dynamic Unit:2 Port:48
00-17-7D-12-3D-5C   48 Dynamic Unit:1 Port:30
00-40-84-20-72-DB   48 Dynamic Unit:1 Port:22
00-BB-C1-79-D8-2A   48 Dynamic Unit:1 Port:31
00-E0-07-8E-92-8E   48 Dynamic Unit:1 Port:45
B0-AD-AA-2B-98-48   48 Self
00-20-85-EE-63-86   64 Dynamic Unit:2 Port:33
00-23-24-37-66-08   64 Dynamic Unit:2 Port:27
00-23-24-9E-61-D3   64 Dynamic Unit:1 Port:27
"""
class SortList:
    def __init__(self, macadd, ports, list, test=test):
        self.macadd = macadd
        self.ports = ports
        self.test = test
        self.list = list

    def getMacAddresses(test):
        macadd = re.findall(r"(?:\S{2}\-){4}\S{2}", test)
#        print(macadd)
        return macadd
    

    def getPorts(test):
        ports = re.findall("(?:Self)|(?:Dynamic Unit:.*)", test)
#        print(ports)
        return ports

    def createList(test):
        list = {}
        ports1 = getPorts(test)
        #test1 = SortList.getMacAddresses(test)
        #for x,y in zip(ports,macadd):
        #    list[x] = y
        print(pots1)


SortList.createList(test)

#list = dict(zip(macadd,ports))
#for i in sorted(dict):
#    print(i,list[i])