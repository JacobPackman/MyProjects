import re


test = """
00-15-5D-0B-0A Dynamic Unit:1 Port:12
00-17-7D-12-3D Dynamic Unit:1 Port:30
00-20-85-EE-63 Dynamic Unit:2 Port:33
"""
class SortList:
    def __init__(self, macadd, ports, list, test=test)
    self.macadd = macadd
    self.ports = ports
    self.test = test
    self.list = list

    def getMacAddresses(test):
        macadd = re.findall(r"(?:\S{2}\-){4}\S{2}", arg)
        return macadd
    

    def getPorts(test):
        ports = re.findall("(?:Self)|(?:Dynamic Unit:.*)", arg)

    def createList()        

getPorts(test)
getMacAddresses(test)

#list = dict(zip(macadd,ports))
#for i in sorted(dict):
#    print(i,list[i])