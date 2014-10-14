
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

s5 = switch.Switch("s5")
topo.addSwitch(s5)

s6 = switch.Switch("s6")
topo.addSwitch(s6)


h1 = host.Host('h1')
h1.addPort(port.Port('AA:AA:AA:CC:CC:CC'))
h1.addPort(port.Port('AA:AA:AA:AC:CC:CC'))

h2 = host.Host('h2')
h2.addPort(port.Port('AA:AA:AA:CC:CC:CD'))

h3 = host.Host('h3')
h3.addPort(port.Port('AA:AA:AA:CC:CC:CE'))

h4 = host.Host('h4')
h4.addPort(port.Port('AA:AA:AA:CC:CC:CF'))

#CONEXOES ENTRE OS SWITCHES

s1.addConnection(0, s2, 0, bandwidth=topology._1G) # Link de 100 Mbps

s2.addConnection(0, s1, 0, bandwidth=topology._1G) # Link de 100 Mbps

s1.addConnection(1, s3, 0, bandwidth=topology._1G) # Link de 100 Mbps

s3.addConnection(0, s1, 1, bandwidth=topology._1G) # Link de 100 Mbps

s2.addConnection(1, s3, 1, bandwidth=topology._1G) # Link de 100 Mbps

s3.addConnection(1, s2, 1, bandwidth=topology._1G) # Link de 100 Mbps

s2.addConnection(3, s4, 0, bandwidth=topology._1G) # Link de 100 Mbps

s4.addConnection(0, s2, 3, bandwidth=topology._1G) # Link de 100 Mbps

s2.addConnection(2, s5, 0, bandwidth=topology._1G) # Link de 100 Mbps

s5.addConnection(0, s2, 2, bandwidth=topology._1G) # Link de 100 Mbps

s3.addConnection(2, s5, 2, bandwidth=topology._1G) # Link de 100 Mbps

s5.addConnection(2, s3, 2, bandwidth=topology._1G) # Link de 100 Mbps

s3.addConnection(3, s6, 0, bandwidth=topology._1G) # Link de 100 Mbps

s6.addConnection(0, s3, 3, bandwidth=topology._1G) # Link de 100 Mbps

#CONEXOES ENTRE OS SWITCHES / HOSTS

s4.addConnection(2, h1, h1.ports[0], bandwidth=topology._100M) # Link de 100 Mbps

s4.addConnection(3, h2, h2.ports[0], bandwidth=topology._100M) # Link de 100 Mbps

s6.addConnection(2, h3, h3.ports[0], bandwidth=topology._100M) # Link de 100 Mbps

s6.addConnection(3, h4, h4.ports[0], bandwidth=topology._100M) # Link de 100 Mbps

#print(topo.transferTime(h1, h2, 10 * 1024 * 1024), 'seconds')

p = topo.findpaths(h1,h4,topology._1G)

print(str(p))

print("O consumo de energia da simulacao foi de:", topo.consumption(), "W/H\n")

#print ( '*** Iniciando %s switches\n' % len( topo.switches ) )

#for switch in topo.switches:
#    print  (switch)


#for key in s1.path.items():
#    print (key)
