## What is the Internet?

> **The Internet is a global system of interconnected computer networks** that uses standardized protocols (TCP/IP) to communicate and share information.

---

## Key Components Explained
### 1. Hosts / End Systems

- **What they are:** All devices connected to the Internet
- **Examples:**
    
    - Computers (desktops, laptops)
    - Smartphones and tablets
    - Servers (web servers, email servers)
    - IoT devices (smart TVs, cameras, thermostats)
    - Gaming consoles

> **Think of them as:** The "people" of the Internet — they send and receive data.

---
### 2. Communication Links

- **What they are:** The physical or wireless connections that carry data
- **Types:**
    
    - **Wired:** Fiber optic, Ethernet cables, coaxial cables
    - **Wireless:** Wi-Fi, cellular (4G/5G), satellite

- **Transmission Rate:** Measured in **bits per second (bps)**
    
    - Common rates: Mbps (megabits), Gbps (gigabits)

> **Think of them as:** The "roads" and "highways" that data travels on.

---
### 3. Packets

- **What they are:** Data is broken into small chunks called **packets** for transmission
- **Why packets?**
    
    - Efficient use of network resources
    - Allows multiple users to share the same link
    - If a packet is lost, only that packet needs retransmission (not the whole file)

```text
+-------------------+-------------------+-------------------+
|    Header         |    Payload        |    Trailer        |
| (Source/Dest IP,  |  (Actual Data)    | (Error Checking)  |
|  Sequence #, etc.)|                   |                   |
+-------------------+-------------------+-------------------+
```
### 4. Packet Switches

- **What they are:** Devices that forward packets toward their destination
    
- **Two Main Types:**
    
|Type|Function|Example|
|---|---|---|
|**Routers**|Forward packets between different networks|Home router, enterprise routers|
|**Link-Layer Switches**|Forward packets within the same network (LAN)|Network switches in offices|
### 5. Internet Service Providers (ISPs)

- **What they are:** Companies that provide Internet access to end systems
    
- **Tiers of ISPs:**
    
    - **Tier 1:** Global backbone (e.g., AT&T, Verizon, Level 3)
    - **Tier 2:** Regional providers (connect Tier 1 to local ISPs)
    - **Tier 3:** Local ISPs (provide direct access to homes/businesses)

### 6. Protocols

- **What they are:** ~={red}**Rules**=~ and ~={red}**standards**=~ that govern how data is sent and received
    
- **Why they matter:** Without protocols, ~={yellow}devices couldn't understand each other=~

**Key Protocols:**

|Protocol|Full Form|Purpose|
|---|---|---|
|**TCP**|Transmission Control Protocol|Reliable, connection-oriented delivery|
|**IP**|Internet Protocol|Addressing and routing packets|
|**HTTP**|Hypertext Transfer Protocol|Web browsing|
|**FTP**|File Transfer Protocol|File transfers|
|**SMTP**|Simple Mail Transfer Protocol|Sending emails|
|**DNS**|Domain Name System|Converts domain names to IP addresses|
