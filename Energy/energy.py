class topology (object):
    
    def searchpath (self):
        pass 

class Switch( Node ):
    portBase = 1
    dpidLen = 16

    def __init__( self, name, dpid=None, opts='', listenPort=None, **params):
        Node.__init__( self, name, **params )
        self.dpid = self.defaultDpid( dpid )
        self.opts = opts
        self.listenPort = listenPort
        if not self.inNamespace:
            self.controlIntf = Intf( 'lo', self, port=0 )

    def defaultDpid( self, dpid=None ):
        if dpid:
            # Remove any colons and make sure it's a good hex number
            dpid = dpid.translate( None, ':' )
            assert len( dpid ) <= self.dpidLen and int( dpid, 16 ) >= 0
        else:
            # Use hex of the first number in the switch name
            nums = re.findall( r'\d+', self.name )
            if nums:
                dpid = hex( int( nums[ 0 ] ) )[ 2: ]
            else:
                raise Exception( 'Unable to derive default datapath ID - '
                                 'please either specify a dpid or use a '
                                 'canonical switch name such as s23.' )
        return '0' * ( self.dpidLen - len( dpid ) ) + dpid

    def defaultIntf( self ):
        if self.controlIntf:
            return self.controlIntf
        else:
            return Node.defaultIntf( self )


class host (object):
    pass


class port (object):
    
    def __init__():
        self.bw = [10, 100, 1000]
        self.status = [on, off]
        self.phosts = [0]
        self.pswitchs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        
class Node( object ):
    
    portBase = 0
    
    def __init__(self, name):
        
     self.name = name
     self.intfs = {}
     self.ports = {}
    
    
    def newPort( self ):
        if len( self.ports ) > 0:
            return max( self.ports.values() ) + 1
        return self.portBase
    
    def connectionsTo( self, node):
        for intf in self.intfList():
            link = intf.link
            if link:
                node1, node2 = link.intf1.node, link.intf2.node
                if node1 == self and node2 == node:
                    connections += [ ( intf, link.intf2 ) ]
                elif node1 == node and node2 == self:
                    connections += [ ( intf, link.intf1 ) ]
        return connections
    
    def linkTo( self, node, link=Link ):
        return link( self, node )

    # Other methods

    def intfList( self ):
        return [ self.intfs[ p ] for p in sorted( self.intfs.iterkeys() ) ]

    def intfNames( self ):
        return [ str( i ) for i in self.intfList() ]