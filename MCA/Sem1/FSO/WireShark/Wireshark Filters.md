
## Filters
1. ip.addr == x.x.x.x
2. Tcp.port == portnumber
3. Udp.port == portnumber
4. http
5. tls or (SSL)
6. tcp.flags.syn == 1 && tcp.flags.ack == 0
7. tcp.flags.reset == 1
8. icmp
9. arp
10. dhcp
11. ip.src == x.x.x.x && ip.dst == y.y.y.y
12. frame contains "string"
13. dns.qry.name == "example.com"
14. tcp.analysis.retransmission
15. not arp && not icmp && not dns

#### HTTP
1. http contains "password"
2. http.request.uri contains "login"
3. http.response.code == 200
4. http.request.method == "GET"

#### Advanced Content Filter
1. frame contains "Microsoft"
2. frame contains "attachment" or frame contains "pdf"