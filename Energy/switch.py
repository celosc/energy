class Switch(object):
    
    def __init__(self):
        self.path = {}
    
    def addPath(self, portNumber, host, port, bandwidth=100):
        if self.path.has_key(portNumber):
            raise Exception("Port already used.")
        self.path[portNumber] = {'bandwidth': bandwidth, 'host': host, 'port': port}
        
    def getBandWidth(self, host):
        for p in self.path.keys():
            if self.path[p]['host'].hostname == host.hostname:
                return self.path[p]['bandwidth']
        return 0