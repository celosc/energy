class Topology(object):
    
    def __init__(self):
        self.switches = []
    
    def addSwitch(self, switch):
        self.switches.append(switch)
    
    def transferTime(self, host1, host2, size):
        bandwidth = 1000000000000
        for s in self.switches:
            lb = s.getBandWidth(host1)
            if lb and s.getBandWidth(host2):
                bandwidth = lb > s.getBandWidth(host2) and s.getBandWidth(host2) or lb
                break
        return size * 8 / bandwidth
                