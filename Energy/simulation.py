import topology, switch, host, port

topo = topology.Topology()

s1 = switch.Switch()
topo.addSwitch(s1)

host1 = host.Host('h1')
host1.addPort(port.Port('AA:AA:AA:CC:CC:CC'))

host2 = host.Host('h2')
host2.addPort(port.Port('AA:AA:AA:CC:CC:CD'))

s1.addPath(1, host1, host1.ports[0], bandwidth=56400.0)

s1.addPath(2, host2, host2.ports[0], bandwidth=56400.0)

print topo.transferTime(host1, host2, 10 * 1024 * 1024), 'seconds'
