### Introduction to SOC
- Security Operations Center **~={blue}SOC=~** comprises a **~={yellow}team of specialized professionals=~**, each responsible for **~={green}different aspects of cybersecurity operations.=~**
- **~={cyan}These roles work collaboratively=~** to **~={orange}ensure the organizations digital assets=~** are ~={purple}**protected, incidents are managed effectively and security measures are continuously improved.**=~

![[Pasted image 20260307213751.png]]

#### Roles In SOC
##### SOC Manager
~={yellow}1. **Leadership and Coordination**=~
- **Overview**: ~={orange}**Oversee=~ the ~={blue}entire SOC operation**=~ and ~={blue}ensure all teams work together effectively.=~
- **Example**:
```
Ensuring Tier 1, Tier 2, and Tier 3 analysts work together 
smoothly without silos
```
~={yellow}2. **Strategic Planning**=~
- **Overview**: **~={orange}Align SOC activities=~** with **~={blue}business objectives and organizational strategies.=~**
- **Example**:
```
If company is expanding to EU, plan for GDPR compliance 
monitoring in SOC
```

~={yellow}3. **Performance Management=~**
- **Overview**: **~={orange}Monitor=~** SOC performance using **~={blue}KPIs and metrics.=~**

~={yellow}4. **Resource Management=~**
- **Overview**: **~={orange}Allocate=~** resources ~={blue}effectively, including staffing, tools, and budgets.=~

#### **Security Analyst Tiers**

##### Tier 1
- Their role **~={orange}is Monitoring & Triage.=~ [ Triage means: ~={pink}Quickly sorting=~ and ~={purple}prioritizing items=~ ~={cyan}to determine the order of action.=~ ] **
	- Looking at a new alert
	- Quickly deciding if it is a real threat or a false alarm
	- Determining how serious it is
- Their task are as follows:
	- Monitor **~={blue}security alerts and dashboards.=~**
	- **~={blue}Perform initial check on alert=~** ( determine **severity** and if its **real** )
- If an **~={purple}alert is confirmed=~** then **Escalate** it to the Tier 2.

##### Tier 2
- Their role is~={orange} **Investigation and Threat Hunting**. =~
- Their task are as follows:
	- They perform **~={blue}deep-dive=~** **~={green}analysis of escalated incidents.=~**
	- They ~={purple}**proactively** hunts for threats=~ (uses MITRE ATTACK).
	- They helps to **~={blue}contain to incidents=~** and **~={blue}fix active incidents=~**.
	
##### Tier 3
- Their role is~={orange} **Advanced Response & Threat Hunting**. =~
- Their task are as follows:
	- They ~={blue}**Lead** **response for ~={green}major/complex incidents**=~=~.
	- They perform **~={purple}Deep Forensic investigation=~ (Forensic investigation usually means investigation that is done right the attack or incident has happened) ** to **~={orange}~={cyan}find root cause.=~=~**
	- They **~={purple}run post-incident review=~** so that they can **~={cyan}improve future processes.=~**

##### Threat Hunter
- They perform **Proactive Detection:** **~={green}Looks for threats=~** that **~={yellow}slipped past normal defenses.=~**
- They perform **Behavioral Analysis:** **~={purple}Studies patterns=~** to **~={blue}find complex attacks.=~**
- They also create **Rules** which ~={purple}**improves detection of threat**=~ with the help of security tools.

##### Incident Responder
- T**hey handles the incident** i.e. **~={yellow}Manages the incident=~** **~={cyan}from start to finish.=~**
- They also perform **Containment & Mitigation:** ~={purple}Stops the attack=~ and ~={purple}limits the damage.=~
- They also provide **Recovery Operations:** i.e. **~={pink}they fixes affected systems=~** and ~={pink}**gets things back to normal.**=~

##### Forensic Analyst
- They perform **Evidence Collection:** i.e. **~={green}they gather and preserve digital proof of the incident.=~**
- They perform **Detailed Analysis:** i.e. **~={green}Checks systems and logs=~** to see **~={cyan}how bad the breach is.=~**
- Once done they create a **Report:** i.e. **~={cyan}Writes findings and helps=~** with legal or compliance needs.

##### Threat Intelligence Analyst
- They perform **Gathering:** i.e. **~={cyan}they collects data=~** on **~={pink}new threats and hacker tactics.=~**
- Once gathering is done they **Report it:** i.e. **~={pink}reports are shared  with SOC teams=~** to **~={cyan}improve defenses.=~**
- They also perform **Collaboration:** i.e. **~={cyan}they exchange THREAT info=~** with **~={pink}partners and inside the organization.=~**

##### Security Engineer
- They perform **Tool Management:** i.e. **~={cyan}they set up and maintain=~** **~={pink}security tools like SIEM, firewalls, etc.=~**
- They also handle **Automation:** i.e. **~={cyan}they implement SOAR solutions=~** to **~={pink}automate SOC tasks.=~**
- They ensure **Integration:** i.e. **~={cyan}they make sure all security tools=~** **~={pink}work together smoothly.=~**