
#    S1 ---- S2
#   / | \     |
#  H1 H2 H3  H4 
#
import topology, switch, host, port

topo = topology.Topology()

central=switch.Switch("central")
topo.addSwitch(central)
for z in range(10):
    s1 = switch.Switch("s1")
    topo.addSwitch(s1)
    central.addConnection(z,s1,101,topology._100M)
    
    s2 = switch.Switch("s2")
    topo.addSwitch(s2)
    central.addConnection(100 + z,s2,101,topology._100M)
    
    for i in range(100):
        h=host.Host("h"+str(i))
        h.addPort(port.Port('AA:AA:AA:CC:CC:CF'))
        s1.addConnection(i,h,h.ports[0],topology._100M)
        
    for i in range(100):
        h=host.Host("h"+str(i))
        h.addPort(port.Port('AA:AA:AA:CC:CC:CF'))
        s2.addConnection(i,h,h.ports[0],topology._100M)
    


#print(topo.transferTime(h1, h2, 10 * 1024 * 1024), 'seconds')

#p = topo.findpaths(h1,h2,topology._1G)

#print(str(p))

print("O consumo de energia da simulacao foi de:", topo.consumption(), "W/H\n")

#print ( '*** Iniciando %s switches\n' % len( topo.switches ) )

#for switch in topo.switches:
#    print  (switch)


#for key in s1.path.items():
#    print (key)
