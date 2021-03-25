import re

buffer = []
while True:
    print("> ", end="")
    line = input()
    if line == "":
        break
    buffer.append(line)
test = "\n".join(buffer)

class SortList:
    def __init__(self, macadd, ports, list, test=test):
        self.macadd = macadd
        self.ports = ports
        self.test = test
        self.list = list

    def getMacAddresses(test):
        macadd = re.findall(r"(?:\S{2}\-){4}\S{2}", test)
        return macadd
    

    def getPorts(test):
        ports = re.findall("(?:Self)|(?:Dynamic Unit:.*)", test)
        return ports

    def createList(test):
        list = {}
        ports = SortList.getPorts(test)
        macadd = SortList.getMacAddresses(test)
        for x,y in zip(macadd,ports):
            list[x] = y
        return list

    def finalList(test):
        list = SortList.createList(test)
        for i in sorted(list):
            print("\t\t\t\t{} {}".format(i, list[i]))
        


SortList.finalList(test)

#list = dict(zip(macadd,ports))
#for i in sorted(dict):
#    print(i,list[i])