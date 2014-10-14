_10M = 10000000
_100M = 100000000
_1G = 1000000000

class Topology(object):
    
    def __init__(self):
        self.switches = []
    
    def addSwitch(self, switch):
        self.switches.append(switch)
    
    def transferTime(self, h1, h2, size):
        bandwidth = _1G
        for s in self.switches:
            lb = s.getBandWidth(h1)
            if lb and s.getBandWidth(h2):
                bandwidth = lb > s.getBandWidth(hh2) and s.getBandWidth(h2) or lb
                break
        return size * 8 / bandwidth
    
    def consumption(self):
        consumption = 0
        for s in self.switches:
            consumption = consumption + s.chassi
            consumption = consumption + s.getPortsConsumption()
        return consumption
    
    def switchesForHost(self,host):
        _s = []
        for s in self.switches:
            if s.hasHost(host):
                _s.append(s)
        return _s
        
    def findpaths(self, host1, host2, threshold, caller=[]):
        paths = []
        host1switches = self.switchesForHost(host1)
        host2switches = self.switchesForHost(host2)
        for sh1 in host1switches:
            ''' look for all connections in the same switch '''
            if sh1 in host2switches:
                if host1 not in caller: caller.append(host1)
                b1 = sh1.getBandWidth(host1)
                b2 = sh1.getBandWidth(host2)
                seq = list(caller)
                seq.append(sh1)
                seq.append(host2)
                paths.append((seq,b1<b2 and totext(b1) or tostrtext(b2),))
            else:
                hasitself = False
                for hidx in sh1.path:
                    if sh1.path[hidx] == host2:
                        hasitself = True
                        break
                if not hasitself and sh1 not in caller:
                    if host1 not in caller: caller.append(host1)
                    _paths = self.findpaths(sh1, host2, threshold, list(caller))
                    paths = paths + _paths                
        return paths
    
def totext(size):
    if size / 1000 < 1:            
        return str(size)
    elif size / 1000 / 1000 < 1:
        size = size / 1000
        r = ''
        if (size) % 1 > 0:
            r = '.'+str(size%1000)            
        return str(int(size))+r+'K'
    elif size / 1000 / 1000 / 1000 < 1:
        size = size / 1000 / 1000
        r = ''
        if (size) % 1 > 0:
            r = '.'+str(size%1000)            
        return str(int(size))+r+'M'
    else:
        size = size / 1000 / 1000 / 1000
        r = ''
        if (size) % 1 > 0:
            r = '.'+str(size%1000)            
        return str(int(size))+r+'G'