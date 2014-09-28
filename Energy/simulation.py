
#    S1 ---- S2
#   / | \     |
#  H1 H2 H3  H4 
#
import topology, switch, host, port

topo = topology.Topology()

s1 = switch.Switch()
topo.addSwitch(s1)

s2 = switch.Switch()
topo.addSwitch(s2)

host1 = host.Host('h1')
host1.addPort(port.Port('AA:AA:AA:CC:CC:CC'))

host2 = host.Host('h2')
host2.addPort(port.Port('AA:AA:AA:CC:CC:CD'))

host3 = host.Host('h3')
host3.addPort(port.Port('AA:AA:AA:CC:CC:CE'))

host4 = host.Host('h4')
host4.addPort(port.Port('AA:AA:AA:CC:CC:CF'))

s1.addPath(1, host1, host1.ports[0], bandwidth=100000000) # Link de 100 Mbps

s1.addPath(2, host2, host2.ports[0], bandwidth=100000000) # Link de 100 Mbps

s1.addPath(3, host3, host3.ports[0], bandwidth=100000000) # Link de 100 Mbps

s2.addPath(2, host4, host4.ports[0], bandwidth=100000000) # Link de 100 Mbps

s2.addPath(1, s1, 4, bandwidth=1000000000) # Link de 1 Gbps

s2.addPath(3, s1, 5, bandwidth=1000000000) # Link de 1 Gbps

#print(topo.transferTime(host1, host2, 10 * 1024 * 1024), 'seconds')

print("O consumo de energia da simulacao foi de:", topo.consumption(), "W/H")