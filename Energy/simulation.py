
#    S1 ---- S2
#   / | \     |
#  H1 H2 H3  H4 
#
import topology, switch, host, port
topo = topology.Topology()
sw = switch.Switch()

s1 = switch.Switch()
topo.addSwitch(s1)

s2 = switch.Switch()
topo.addSwitch(s2)

h1 = host.Host('h1')
h1.addPort(port.Port('AA:AA:AA:CC:CC:CC'))

h2 = host.Host('h2')
h2.addPort(port.Port('AA:AA:AA:CC:CC:CD'))

h3 = host.Host('h3')
h3.addPort(port.Port('AA:AA:AA:CC:CC:CE'))

h4 = host.Host('h4')
h4.addPort(port.Port('AA:AA:AA:CC:CC:CF'))

s1.addPath(1, h1, h1.ports[0], bandwidth=100000000) # Link de 100 Mbps

s1.addPath(2, h2, h2.ports[0], bandwidth=100000000) # Link de 100 Mbps

s1.addPath(3, h3, h3.ports[0], bandwidth=100000000) # Link de 100 Mbps

s2.addPath(2, h4, h4.ports[0], bandwidth=100000000) # Link de 100 Mbps

s2.addPath(1, s1, 4, bandwidth=1000000000) # Link de 1 Gbps

s2.addPath(3, s1, 5, bandwidth=1000000000) # Link de 1 Gbps

#print(topo.transferTime(h1, h2, 10 * 1024 * 1024), 'seconds')

print("O consumo de energia da simulacao foi de:", topo.consumption(), "W/H")

print ( '*** Iniciando %s switches\n' % len( topo.switches ) )
print ( '*** Iniciando %s Portas\n' % len( sw.path.keys()))
#for switch in self.switches:
 #   print( switch.name + ' ')