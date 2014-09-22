from energy import topology

    s1 = topology.addSwitch('s1', dpid='0000000000000201')
    h1 = topology.addHost('h1')
    h2 = topology.addHost('h2')
    topology.addLink(h1, s1)
    topology.addLink(h2, s1)

