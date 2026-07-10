## **Elements of a SOC**

### **Overview**

- **What it is:** i.e. ~={cyan}it is a formalized, structured, and disciplined approach=~ by ~={pink}organizations to defend against today's threats=~ using professional services in a ~={orange}Security Operations Center (SOC).=~
- **Services Provided:** i.e. ~={cyan}SOCs provide=~ a ~={pink}broad range of services=~ including ~={orange}monitoring and management, comprehensive threat solutions, and hosted security=~ that can be ~={cyan}customized to meet customer needs.=~
- **Structure:** i.e. ~={cyan}SOCs can be=~ either ~={pink}wholly in-house (owned and operated by a business)=~ or ~={orange}elements can be contracted out to security vendors.=~

---

### **The Three Elements of SOC**

The foundation of any SOC rests on three critical pillars: **People, Processes, and Technology**

---

## **People in the SOC**

~={cyan}Job roles in a SOC are rapidly evolving.=~ Traditionally, ~={pink}SOCs assign job roles by tiers=~ according to the ~={orange}expertise and responsibilities=~ required for each.

### **Tier 1: Alert Analyst**

- **Role:** i.e. ~={cyan}they monitor=~ ~={pink}incoming alerts,=~ verify that a ~={orange}true incident has occurred,=~ and forward tickets to Tier 2 if necessary.
- **Responsibility:** Entry-level position focused on alert verification and ticket management.

### **Tier 2: Incident Responder**

- **Role:** i.e. ~={cyan}they conduct=~ ~={pink}deep investigation of incidents=~ and ~={orange}advise remediation or action=~ to be taken.
- **Responsibility:** Mid-level position requiring expertise in incident analysis and response strategies.

### **Tier 3: Threat Hunter**

- **Role:** i.e. ~={cyan}they possess expert-level skill=~ in ~={pink}network, endpoint, threat intelligence, and malware reverse engineering.=~
- **Key Expertise:** i.e. ~={cyan}they are experts at=~ ~={pink}tracing malware processes=~ to determine its ~={orange}impact and removal methods.=~
- **Threat Detection:** i.e. ~={cyan}they are deeply involved in=~ ~={pink}hunting for potential threats=~ and ~={orange}implementing threat detection tools.=~
- **Proactive Hunting:** i.e. ~={cyan}threat hunters search for=~ ~={pink}cyber threats present in the network=~ that have ~={orange}not yet been detected.=~

### **SOC Manager**

- **Role:** i.e. ~={cyan}they manage=~ all the ~={pink}resources of the SOC=~ and serve as the ~={orange}point of contact=~ for the larger organization or customer.

---

## **Process in the SOC**

~={cyan}The day of a Cybersecurity Analyst typically begins with=~ monitoring ~={pink}security alert queues.=~

### **Alert Management Workflow**

- **Ticketing System:** i.e. ~={cyan}a ticketing system is frequently used=~ to ~={pink}assign alerts to a queue=~ for an analyst to investigate.
- **False Alarm Verification:** i.e. ~={cyan}one job of the Cybersecurity Analyst might be=~ to ~={pink}verify that an alert represents=~ a ~={orange}true security incident.=~
- **Escalation:** When ~={cyan}verification is established,=~ the incident can be ~={pink}forwarded to investigators=~ or other ~={orange}security personnel=~ to be acted upon. Otherwise, the alert may be dismissed as a false alarm.

### **Escalation Path**

- **Level 1 to Level 2:** If a ticket cannot be resolved by Tier 1, the ~={cyan}Cybersecurity Analyst will forward=~ the ticket to a ~={pink}Tier 2 Incident Responder=~ for ~={orange}deeper investigation and remediation.=~
- **Level 2 to Level 3:** If the ~={cyan}Incident Responder cannot resolve=~ the ticket, it will be forwarded to ~={pink}Tier 3 personnel=~ with ~={orange}in-depth knowledge and threat hunting skills.=~

---

## **Technology in the SOC: SIEM**

~={cyan}A SOC needs=~ a ~={pink}**security information and event management system (SIEM)**,=~ or its equivalent.

### **SIEM Purpose**

- **Core Function:** i.e. ~={cyan}SIEM makes sense of=~ all the data that ~={pink}firewalls, network appliances, intrusion detection systems, and other devices=~ generate.

### **SIEM Capabilities**

~={cyan}SIEM systems are used for=~:

- ~={pink}Collecting and filtering data=~
- ~={orange}**Detecting** and **classifying** threats=~
- **Analyzing** and **investigating** threats
- **Managing** resources
- **Addressing future threats**

### **SIEM Technologies Include**

- ~={red}Event collection, correlation, and analysis=~
- ~={red}Security monitoring and control=~
- ~={red}Log management=~
- ~={red}Vulnerability assessment=~
- ~={red}Vulnerability tracking=~

---

## **Technology in the SOC: SOAR**

~={cyan}SIEM and=~ ~={pink}security orchestration, automation and response (SOAR)=~ are ~={orange}often paired together=~ as they have **capabilities that complement each other.**

### **SOAR Overview**

- **Usage:** i.e. ~={cyan}Large security operations (SecOps) teams use=~ both technologies to **~={pink}optimize their SOC.=~**
- **Relationship:** i.e. ~={cyan}SOAR platforms are similar to SIEMs=~ in that they aggregate, correlate, and analyze alerts.
- **Key Difference:** i.e. SOAR technology goes a step further by integrating **~={pink}threat intelligence and automating incident investigation.=~**

### **SOAR Capabilities**

- **~={red}Data Gathering=~:** i.e. ~={orange}they gather alarm data from each component of the system.=~
- **~={red}Integration & Automation:=~** i.e. they emphasize integration  as a means of ~={orange}automating complex incident response workflows that enable more rapid response=~ and adaptive defense strategies.
- **~={red}Playbooks=~:** i.e. they include ~={orange}pre-defined playbooks that enable automatic response to specific threats.=~ Playbooks can be initiated automatically based on predefined rules or may be triggered by security personnel.

