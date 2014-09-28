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
                bandwidth = lb > s.getBandWidth(h2) and s.getBandWidth(h2) or lb
                break
        return size * 8 / bandwidth
    
    def consumption(self):
        consumption = 0
        for s in self.switches:
            consumption = consumption + s.chassi
            consumption = consumption + s.getPortsConsumption()
        return consumption
    
    