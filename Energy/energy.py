class topology (object):
    
    def searchpath (self):
        pass 

class switch (object):
    pass


class host (object):
    pass


class port (object):
    
    def port(self, src, dst):
        '''Get port number.

        @param src source switch name
        @param dst destination switch name
        @return tuple (src_port, dst_port):
            src_port: port on source switch leading to the destination switch
            dst_port: port on destination switch leading to the source switch
        '''
        if src in self.ports and dst in self.ports[src]:
            assert dst in self.ports and src in self.ports[dst]
            return self.ports[src][dst], self.ports[dst][src]