from Onboard.ConfigUtils import _PACK_HOOK
class Topology(object):
    
    def __init__(self):
        self.switches = []
    
    def addSwitch(self, switch):
        self.switches.append(switch)
    
    def transferTime(self, h1, h2, size):
        bandwidth = 1000000000
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
        print("host1:"+str(host1)+", host2:"+str(host2))
        paths = []
        host1switches = self.switchesForHost(host1)
        host2switches = self.switchesForHost(host2)
        for sh1 in host1switches:
            ''' look for all connections in the same switch '''
            if sh1 in host2switches:
                b1 = sh1.getBandWidth(host1)
                b2 = sh1.getBandWidth(host2)
                paths.append((sh1,b1<b2 and b1 or b2,))
            else:
                hasitself = False
                for hidx in sh1.path:
                    if sh1.path[hidx] == host2:
                        hasitself = True
                        break
                if not hasitself and sh1 not in caller:
                    caller.append(host1)
                    _paths = self.findpaths(sh1, host2, threshold, caller)
                    paths = paths + _paths                
        #paths = paths + self.conectionsMultiHop(host1switches, host2switches)
        return paths
                
