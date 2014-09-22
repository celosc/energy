class topology (object):
    #  s1 = self.addSwitch('s1', dpid='0000000000000201')
    #  h1 = self.addHost('h1')
    #  h2 = self.addHost('h2')
    #  self.addLink(h1, s1)
    #  self.addLink(h2, s1)
    
    def addHost( self, name, cls=None, **params ):
        """Add host.
           name: name of host to add
           cls: custom host class/constructor (optional)
           params: parameters for host
           returns: added host"""
        # Default IP and MAC addresses
        defaults = { 'ip': ipAdd( self.nextIP,
                                  ipBaseNum=self.ipBaseNum,
                                  prefixLen=self.prefixLen ) +
                                  '/%s' % self.prefixLen }
        if self.autoSetMacs:
            defaults[ 'mac'] = macColonHex( self.nextIP )
        if self.autoPinCpus:
            defaults[ 'cores' ] = self.nextCore
            self.nextCore = ( self.nextCore + 1 ) % self.numCores
        self.nextIP += 1
        defaults.update( params )
        if not cls:
            cls = self.host
        h = cls( name, **defaults )
        self.hosts.append( h )
        self.nameToNode[ name ] = h
        return h

    def addSwitch( self, name, cls=None, **params ):
        """Add switch.
           name: name of switch to add
           cls: custom switch class/constructor (optional)
           returns: added switch
           side effect: increments listenPort ivar ."""
        defaults = { 'listenPort': self.listenPort,
                     'inNamespace': self.inNamespace }
        defaults.update( params )
        if not cls:
            cls = self.switch
        sw = cls( name, **defaults )
        if not self.inNamespace and self.listenPort:
            self.listenPort += 1
        self.switches.append( sw )
        self.nameToNode[ name ] = sw
        return sw
    
    def addLink( self, node1, node2, port1=None, port2=None,
                 cls=None, **params ):
        """"Add a link from node1 to node2
            node1: source node
            node2: dest node
            port1: source port
            port2: dest port
            returns: link object"""
        defaults = { 'port1': port1,
                     'port2': port2,
                     'intf': self.intf }
        defaults.update( params )
        if not cls:
            cls = self.link
        return cls( node1, node2, **defaults )
    
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
    
    
    
    class Link( object ):

    def __init__( self, node1, node2, port1=None, port2=None,
                  intfName1=None, intfName2=None,
                  intf=Intf, cls1=None, cls2=None, params1=None,
                  params2=None ):
        """Create veth link to another node, making two new interfaces.
           node1: first node
           node2: second node
           port1: node1 port number (optional)
           port2: node2 port number (optional)
           intf: default interface class/constructor
           cls1, cls2: optional interface-specific constructors
           intfName1: node1 interface name (optional)
           intfName2: node2  interface name (optional)
           params1: parameters for interface 1
           params2: parameters for interface 2"""
        # This is a bit awkward; it seems that having everything in
        # params would be more orthogonal, but being able to specify
        # in-line arguments is more convenient!
        if port1 is None:
            port1 = node1.newPort()
        if port2 is None:
            port2 = node2.newPort()
        if not intfName1:
            intfName1 = self.intfName( node1, port1 )
        if not intfName2:
            intfName2 = self.intfName( node2, port2 )

        self.makeIntfPair( intfName1, intfName2 )

        if not cls1:
            cls1 = intf
        if not cls2:
            cls2 = intf
        if not params1:
            params1 = {}
        if not params2:
            params2 = {}

        intf1 = cls1( name=intfName1, node=node1, port=port1,
                      link=self, **params1  )
        intf2 = cls2( name=intfName2, node=node2, port=port2,
                      link=self, **params2 )

        # All we are is dust in the wind, and our two interfaces
        self.intf1, self.intf2 = intf1, intf2

    @classmethod
    def intfName( cls, node, n ):
        "Construct a canonical interface name node-ethN for interface n."
        return node.name + '-eth' + repr( n )

    @classmethod
    def makeIntfPair( cls, intf1, intf2 ):
        """Create pair of interfaces
           intf1: name of interface 1
           intf2: name of interface 2
           (override this class method [and possibly delete()]
           to change link type)"""
        makeIntfPair( intf1, intf2  )
        
        
        
        