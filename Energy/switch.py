class Switch(object):
    
    def __init__(self):
        self.path = {}
        self.chassi = 40
    
    def addPath(self, portNumber, host, port, bandwidth=10000000):
        if portNumber in self.path:
            raise Exception("Port already used.")
        self.path[portNumber] = {'bandwidth': bandwidth, 'host': host, 'port': port}
        
    def getBandWidth(self, host):
        for p in self.path.keys():
            if self.path[p]['host'].hostname == host.hostname:
                return self.path[p]['bandwidth']
        return 0

    def getConsumption(self, portNumber):
        if portNumber in self.path:
            if self.path[portNumber]['bandwidth'] == 10000000:
                ''' 10Mb = 1Watts/h '''
                return 1
            elif self.path[portNumber]['bandwidth'] == 100000000:
                ''' 100Mb = 2.5Watts/h '''
                return 2.5
            else:
                ''' > 100Mb = 5Watts/h '''
                return 5
    
    def getPortsConsumption(self):
        _r = 0
        for p in self.path:
            _r = _r + self.getConsumption(p)
        return _r