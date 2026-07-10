### What is Computer Networks

- **A computer network is simply~={yellow} two or more computers connected together so they can exchange resources, files and possess some kind of communications within themselves.**=~

#### Types of Computer Network

##### Classification Based on SIZE : 

1. Personal Area Network (PAN) : A personal area network (PAN) is a **computer network** **~={green}organized around an individual for personal use only.=~**
	- e.g. Your phone connected to your earbuds via Bluetooth.
	
2. Local Area Network (LAN) :  A local area network (LAN) is a **~={green}computer network that interconnects computers within a limited area.=~**
	- e.g.: Your home Wi-Fi connecting all your family's devices.
	
3. Metropolitan Area Network (MAN) : A MAN is a ~={green}**computer network that interconnects computers within a metropolitan area.**=~

4. Wide Area Network (WAN) : A wide area network (WAN) is a **~={green}computer network that covers a large geographical area.=~**
	- e.g. A company with offices in different cities connecting them together
##### Classification Based On Ownership
- Open Network - If the network’s internal operation is in the public domain.
- Closed Network - Private network that can only be used by authenticated, authorized devices.

##### Classification Based On Topologies
- Topology defines the structure of the network of how all the components are interconnected to each other. 
- Types are 
	- Bus 
	- Ring 
	- Star 
	- Mesh 
	- Hybrid

#### Types of Transmission MEDIA : 

- **Guided/ Wired Medium:** ~={orange}**Uses cables or wires to transmit data.** =~

	- **Twisted Pair Cable** 
		- **Two insulated copper wires** ~={green}**twisted together to reduce interference.**=~
		- Types of Twisted Pair Cable :
			- **UTP** (Unshielded Twisted Pair) — no shielding, cheaper
			- **STP** (Shielded Twisted Pair) — has shielding, more protection
		- Speed up to 10 Gbps (depending on category)
		- Ranges up to 100 meters.
		
	- **Coaxial Cable** 
		- **Single copper core** ~={green}**surrounded by insulation, shielding, and outer cover.**=~
		- Speed up to 10 Mbps (depending on category)
		- Ranges up to 500 meters.
		- Has higher bandwidth.

	- **Fiber Optic Cable**
		- **Uses light pulses** (not electricity) **~={green}to transmit data through thin glass or plastic fibers=~**
		- Types of Fiber Optic Cable :
			- **Single-mode** — long distances, uses laser
			- **Multi-mode** — shorter distances, uses LED
		- Speed up to 100 Gbps or more
		- Range up to 40+ kilometers (single-mode)

-  **UNGUIDED MEDIA (WIRELESS)** : **~={orange}Signals travel through air, vacuum, or water without a physical conductor.=~**

	- **Radio Waves**
		- Electromagnetic waves with frequencies from 30 Hz to 300 GHz
		- Used for " Wi-Fi, Bluetooth, radio broadcasting, cellular networks "
		- Radio Waves are **omni-directional.**
		- Transmitter are used to generate radio waves artificially which are received by radio receivers.

	- **Microwaves**
		- Microwave is a **~={green}type of radio wave with high frequencies.=~** 
		- It has a frequency range between 300MHz to 300GHz. 
		- Microwaves are **unidirectional.**

	- **Infrared** Wave
		- This type of Wave is **~={green}used for very short range communication=~** and it has **~={orange}frequencies that are higher than Microwaves.=~**
		- These waves **cannot penetrate walls.**
		- IT has high data transfer rate.

#### Network Architecture :
- It is **the design of a computer network.**
- There are 2 types of network architecture 
	- **Peer to Peer model** : 
		- This **~={green}network involve two or more computers=~** pooling individual resources.
		- The **shared resources** are **~={green}available to every computer in the network.=~**
		- Each computer acts as **~={green}both the client and the server=~**, **communicating directly with the other computers.** 
		- For example, **a printer on one computer can be used by any other computer on the network.**

		- **Advantages of Peer-to-Peer Network :**
			- **Does not require a dedicated server** which means its less costly.
			- **If one computer stops working**, **~={green}the other computers connected to the network will continue working=~**
			
		- **Disadvantages of Peer-to-Peer Network :** 
			- ~={green}**Security and data backup=~s** are to be done to each individual computer.
			- As the ~={green}**numbers of computers increases on a P2P network**=~, the performance, security, and access **becomes more complex.**

	- **Client/server model :**
		- In this architecture **many clients** (remote processors) **~={green}request and receive service from a centralized server=~** (host computer).
		- In this architecture the **centralized host,** (dedicated server) is **~={green}really a powerful computer that acts as a hub=~** in which other computers connect to or request to. 
		- This **server** is the **heart of the system**, which **manages** and **provides resources to any client that requests them.**

		- **Advantages of Client-Server Network :**
			- **Resources and data security** are ~={green}**controlled through the serve=~r**.
			- **Server** can be **accessed anywhere** and **across multiple platforms.** 
		- **Disadvantages of Client-Server Network :**
			- Can become very **costly** due to the maintain the server.
			- **If and when the server goes down**, the entire network will be affected.

####  Layered Architecture
##### OSI Model
![[Pasted image 20260321165447.png]]

- **Organization of Layers** (Divided in to 2 subgroups)

- **Network Support Layers** 
	- **Physical**, **data link** and **network** layers. • Deals with physical aspects of moving data from one device to another. 
- **User Support Layers**
	- **Session**, **Presentation** and **application** layer. • Provides interoperability among different software systems. 
- **Transport layer** links these two subgroups. 


1.  **Physical Layer**
	- The **lowest layer** of the OSI reference model. 
	- It is responsible for the~={green} **actual physical connection between the devices.**=~ 
	- The physical layer **~={green}contains information=~** in the ~={green}**form of bits**=~.

	- **Protocols**: USB, Ethernet (cabling), Bluetooth.

2.  **Data Link Layer**
	- This layer is responsible for the **~={green}node-to-node delivery of the message.=~** 
	- The **main function of this layer** is to **make sure data transferred without anyone** **~={green}error from one node to another.=~**

	- **Protocols**: Ethernet, Frame Relay, MAC addressing.

3.  **Network Layer**
	- This layer is responsible **~={green}routing data packets across different networks to reach the correct destination.=~**
	- It also takes care of **packet routing** i.e. **selection of the shortest path** to **transmit the packet**, **from the number of routes available.**

	- **Protocols**: IP (IPv4/IPv6), ICMP.

4.  **Transport Layer**
	- This Layer is responsible for **~={green}ensuring reliable and efficient delivery of data between devices.=~**
	- The data in the transport layer is referred to as **Segments**. 
	- It is responsible for the **~={green}end-to-end delivery of the complete message.=~**

	- **Protocols**: TCP (connection-oriented), UDP (connectionless).

5.  **Session Layer**
	- This Layer is responsible for the ~={green}**establishment of connections, management of connections, terminations of sessions**=~ **between two devices**. 
	- It also provides **authentication and security.** 

	- **Protocols** used in the Session Layer are NetBIOS, PPTP.

6.  **Presentation Layer**
	- This layer is responsible for **~={green}translating, encrypting, and compressing data=~** into a format that **both sender and receiver understand.**

	- **Protocols**: TLS/SSL, ASCII,  JPEG.

7.  **Application Layer**
	- This Layer is responsible for the ~={green}**Direct interaction with end-user applications**=~ (e.g., **web browsers**, **email clients**).

	- **Protocols**: HTTP, HTTPS, DNS.