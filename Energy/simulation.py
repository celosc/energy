
#    S1 ---- S2
#   / | \     |
#  H1 H2 H3  H4 
#
import topology, switch, host, port

topo = topology.Topology()

s1 = switch.Switch("s1")
topo.addSwitch(s1)

s2 = switch.Switch("s2")
topo.addSwitch(s2)

s3 = switch.Switch("s3")
topo.addSwitch(s3)
#s3.chassi=100

s4 = switch.Switch("s4")
topo.addSwitch(s4)

h1 = host.Host('h1')
h1.addPort(port.Port('AA:AA:AA:CC:CC:CC'))
h1.addPort(port.Port('AA:AA:AA:AC:CC:CC'))

h2 = host.Host('h2')
h2.addPort(port.Port('AA:AA:AA:CC:CC:CD'))

h3 = host.Host('h3')
h3.addPort(port.Port('AA:AA:AA:CC:CC:CE'))

h4 = host.Host('h4')
h4.addPort(port.Port('AA:AA:AA:CC:CC:CF'))

s1.addConnection(4, s3, 1, bandwidth=topology._10M) # Link de 1 Gbps

s3.addConnection(1, s1, 4, bandwidth=topology._10M) # Link de 1 Gbps

s1.addConnection(5, s2, 4, bandwidth=topology._100M) # Link de 1 Gbps

s2.addConnection(4, s1, 5, bandwidth=topology._100M) # Link de 1 Gbps

s1.addConnection(6, s4, 0, bandwidth=topology._1G) # Link de 1 Gbps

s4.addConnection(0, s1, 6, bandwidth=topology._1G) # Link de 1 Gbps

s4.addConnection(1, s2, 3, bandwidth=topology._1G) # Link de 1 Gbps

s2.addConnection(3, s4, 1, bandwidth=topology._10M) # Link de 1 Gbps #ERRO

s3.addConnection(2, s2, 2, bandwidth=topology._10M) # Link de 1 Gbps

s2.addConnection(2, s3, 2, bandwidth=topology._10M) # Link de 1 Gbps

s1.addConnection(1, h1, h1.ports[0], bandwidth=topology._100M) # Link de 100 Mbps

s1.addConnection(2, h2, h2.ports[0], bandwidth=topology._100M) # Link de 100 Mbps

s1.addConnection(3, h3, h3.ports[0], bandwidth=topology._1G) # Link de 100 Mbps

s2.addConnection(1, h4, h4.ports[0], bandwidth=topology._1G) # Link de 100 Mbps

#s2.addConnection(3, h1, h1.ports[1], bandwidth=topology._10M)

#print(topo.transferTime(h1, h2, 10 * 1024 * 1024), 'seconds')

p = topo.findpaths(h1,h4,topology._1G)

print(str(p))

print("\n")

print("O consumo de energia da simulacao foi de:", topo.consumption(), "W/H\n")

#print ( '*** Iniciando %s switches\n' % len( topo.switches ) )

#for switch in topo.switches:
#    print  (switch)


#for key in s1.path.items():
#    print (key)
