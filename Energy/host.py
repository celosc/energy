class Host(object):
    
    def __init__(self, hostname, ports=[]):
        self.hostname = hostname
        self.ports = []
        for p in ports:
            self.ports.append(p)
    
    def addPort(self, port):
        if port:
            self.ports.append(port)
            
