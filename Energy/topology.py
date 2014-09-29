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
    
    def conectionsMultiHop(self,switchesHost1, switchesHost2):
        ''' aqui tem que fazer uma função recursiva para encontrar
        todas as possibilidades de saltos
        '''
        pass    
        
    def findpaths(self, host1, host2, threshold):
        paths = []
        h1s = self.switchesForHost(host1)
        h2s = self.switchesForHost(host2)
        for sh1 in h1s:
            ''' look for all connections in the same switch '''
            if sh1 in h2s:
                b1 = sh1.getBandWidth(host1)
                b2 = sh1.getBandWidth(host2)
                paths.append((sh1,b1<b2 and b1 or b2,))
        paths = paths = self.conectionsMultiHop(h1s, h2s)
        return paths
                
                
                
                
                