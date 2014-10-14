from host import Host
import topology

class Switch(object):
    
    def __init__(self,name):
        self.path = {}
        self.chassi = 60
        self.name = name
    
    def __repr__(self):
        #return "%s(%r)" % (self.name, self.__dict__)
        return "%s" % (self.name)
    
    def __str__(self):
        return self.name
   
    def addConnection(self, portNumber, host, port, bandwidth=topology._1G):
        if portNumber in self.path:
            raise Exception("Port already used.")
        self.path[portNumber] = {'host': host, 'port': port, 'bandwidth': bandwidth}
        #s1.addConnection(1, h1, h1.ports[0], bandwidth=100000000)
        
    def getBandWidth(self, host):
        for p in self.path.keys():
            if self.path[p]['host'] == host:
                return self.path[p]['bandwidth']
        return 0

    def getConsumption(self, portNumber):
        if portNumber in self.path:
            if self.path[portNumber]['bandwidth'] <= topology._10M:
                ''' 10Mb = 1Watts/h '''
                return 1
            elif self.path[portNumber]['bandwidth'] == topology._100M:
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
    
    def hasHost(self,host):
        for p in self.path:
            if self.path[p]['host'] == host:
                return self.path[p]['bandwidth']
        return 0
