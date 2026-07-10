## **What is Hardware Abstraction Layer (HAL)?**

- **Definition:** Software that handles all communication between hardware and the kernel
- **Kernel:** Core of the operating system with complete control over the entire computer
- **Kernel Responsibilities:**
  - Handles all input and output operations
  - Manages memory allocation and access
  - Controls all connected devices

## **User Mode vs Kernel Mode**

- **CPU Operating Modes:** The CPU operates in 2 different modes

  **1. User Mode:**
  - Where installed applications run
  - Restricted address space created for each application
  - Each app has its own dedicated process

  **2. Kernel Mode:**
  - Where the operating system runs
  - All kernel code shares the same address space
  - If kernel code fails, the entire OS crashes

---

## **Windows File Systems**

### **What is a File System?**

- **Definition:** How information is organized on storage media
- **Purpose:** Determines how data is stored, accessed, and managed
- **Selection Criteria:** Depends on the type of media being used

### **NTFS (New Technology File System)**

**Why NTFS is Most Widely Used:**

- Supports very large files and partitions
- Highly compatible with other operating systems
- Very reliable with recovery features
- Extensive security features
- File system encryption support

**Security Features:**

- **Data Access Control:** Achieved through security descriptors
- **Permissions:** File ownership and permissions down to file level
- **Timestamps (MACE):**
  - **M**odify - When file was last modified
  - **A**ccess - When file was last accessed
  - **C**reate - When file was created
  - **E**ntry Modified - When file metadata changed
- **Forensic Value:** Used in investigations to determine file/folder history

### **Partitioning and Formatting**

- **Partitions:** Hard drive divided into logical storage units
- **Process:** Device must be partitioned → formatted with file system
- **Automatic Setup:** Most OSs automatically partition and format during installation

### **NTFS Disk Structures**

1. **Partition Boot Sector**
   - First 16 sectors of the drive
   - Contains location of Master File Table (MFT)
   - Last 16 sectors contain backup copy

2. **Master File Table (MFT)**
   - Contains locations of all files and directories
   - Stores file attributes (security info, timestamps)

3. **System Files**
   - Hidden files
   - Store information about volumes and file attributes

4. **File Area**
   - Main partition area
   - Stores actual files and directories

### **Data Recovery Security Risk**

- ⚠️ **Important:** Previous data may be recoverable after formatting
- **Why:** Not all data is completely removed
- **Solution:** Perform **secure wipe** on reused drives
- **How:** Writes data multiple times to ensure no remaining data

### **Alternate Data Streams (ADS)**

**What are ADSs?**

- NTFS stores files as series of attributes (name, timestamp, etc.)
- Data stored in attribute `$DATA` = data stream
- **ADS:** Additional data streams attached to files

**Common Uses:**

- Applications store additional file information
- Metadata storage

**Security Concern:**

- ⚠️ Easy to hide data in ADS
- Attackers can store malicious code in ADS
- Code can be called from different files
- Important factor in malware analysis

**Identification:**

- Format: `Filename.txt:ADS`
- Example: `Testfile.txt:ADS` indicates ADS called "ADS" attached to Testfile.txt

---

## **Windows Boot Process**

### **Overview**

- Multiple actions occur from power button press to full Windows load
- Known as the **Windows Boot Process**

### **Computer Firmware Types**

**1. BIOS (Basic Input-Output System)**

- Created in early 1980s
- Works same way as original design
- Difficulty supporting new features as computers evolved

**2. UEFI (Unified Extensible Firmware Interface)**

- Designed to replace BIOS
- Supports modern features
- Greater visibility into boot process

### **BIOS Boot Process**

**Initialization Phase:**

- Hardware devices initialized
- Power-On Self-Test (POST) performed
- Verifies all devices communicating
- Ends when system disk discovered

**Loading OS:**

- POST looks for Master Boot Record (MBR)
- MBR contains small program to locate and load OS
- BIOS executes this code
- Operating system starts loading

### **UEFI Boot Process**

**Key Differences:**

- Loads EFI program files (`.efi` files)
- Stored in special disk partition: **EFI System Partition (ESP)**
- Direct entry to protected mode
- Enhanced security at boot time

### **Windows Boot Sequence (BIOS or UEFI)**

**1. Bootmgr.exe Execution**

- Switches system from real mode → protected mode
- Enables use of all system memory

**2. Boot Configuration Database (BCD)**

- Bootmgr.exe reads BCD
- Contains additional startup code
- Indicates: hibernation resume OR cold start

**3. Hibernation Resume Path**

- If resuming from hibernation:
  - Winresume.exe runs
  - Reads Hiberfil.sys file
  - Restores computer state

**4. Cold Start Path**

- If fresh boot:
  - Winload.exe loads
  - Creates hardware configuration record in registry
  - Uses Kernel Mode Code Signing (KMCS)
  - Verifies all drivers digitally signed
  - Ensures safe driver loading

**5. Kernel Initialization**

- Winload.exe runs Ntoskrnl.exe
- Starts Windows kernel
- Sets up HAL (Hardware Abstraction Layer)

**6. User Environment Setup**

- Session Manager Subsystem (SMSS) reads registry
- Creates user environment
- Starts Winlogon service
- Prepares each user's desktop for login

---

## **Windows Startup**

### **Registry Keys for Auto-Start**

**1. HKEY_LOCAL_MACHINE**

- Stores Windows configuration aspects
- Contains services that start with each boot

**2. HKEY_CURRENT_USER**

- Stores logged-in user settings
- Contains services that start only when user logs on

### **Startup Entry Types**

- Run
- RunOnce
- RunServices
- RunServicesOnce
- Userinit

### **Configuration Methods**

- **Manual:** Directly edit registry (not recommended)
- **Safe Method:** Use **Msconfig.exe** tool
  - View all startup options
  - Change startup settings
  - Access via search box

---

## **Windows Shutdown**

### **Best Practice**

- Always perform proper shutdown
- Prevents file corruption and data loss

### **Why Proper Shutdown Matters**

- Closes open files safely
- Closes services in correct order
- Prevents application hanging
- Records configuration changes before power loss

### **Shutdown Process**

**Order of Operations:**

1. User mode applications close first
2. Kernel mode processes close second

**Unresponsive Process Handling:**

- **User Mode:** OS displays notification, allows wait or force end
- **Kernel Mode:** Shutdown appears to hang, may need power button

### **Shutdown Methods**

- Start menu power options
- Command line: `shutdown` command
- Ctrl+Alt+Delete → Power icon

### **Shutdown Options**

**1. Shutdown**

- Turns computer off (power off)

**2. Restart**

- Reboots computer (power off → power on)

**3. Hibernate**

- Records current computer state
- Stores in file
- User resumes with all files/programs still open
- Faster than cold start

---

## **Windows Configuration and Monitoring**

### **Run as Administrator**

**Security Best Practice:**

- ⚠️ Don't log on with Administrator account
- ⚠️ Don't use account with admin privileges
- **Why:** Any program inherits admin privileges
- **Risk:** Malware gains full file/folder access

**When Admin Privileges Needed:**

- Two methods to run/install software requiring admin privileges

### **Local Users and Domains**

**Local User Account**

- Created when starting new computer or installing Windows
- Contains customization settings
- Stores access permissions and file locations
- User-specific data storage

**Default Accounts:**

- Guest account (disabled by default)
- Administrator account (disabled by default)

**Security Best Practices:**

- ✓ Don't enable Administrator account
- ✓ Don't give standard users admin privileges
- ✓ System prompts for admin password when needed
- ✓ Only that task runs as administrator
- ✓ Prevents unauthorized software installation/execution

### **Windows Groups**

**Purpose:**

- Simplify user administration
- Assign permissions to groups instead of individuals

**Group Characteristics:**

- Has name and specific permission set
- User placed in group gets group permissions
- User can be in multiple groups

**Permission Overlap:**

- "Explicitly deny" overrides other permissions
- Useful for fine-grained access control

**Built-in Groups Example:**

- Performance Log Users group
  - Members can schedule performance counter logging
  - Can collect logs locally or remotely

**Management Tool:**

- lusrmgr.msc control panel applet

### **Domains**

**Definition:**

- Network service storing users, groups, computers, peripherals, security settings
- Controlled by database on domain controllers

**Domain Controllers (DCs):**

- Special computers storing domain database
- Can be single computer or group of computers

**Authentication:**

- Each user and computer must authenticate against DC
- Required to logon and access network resources

**Security Settings:**

- DC sets security settings for each user/computer per session
- DC settings override local settings

---

## **CLI and PowerShell**

### **Windows Command Line Interface (CLI)**

**Capabilities:**

- Run programs
- Navigate file system
- Manage files and folders
- Create batch files for multiple commands

**Access:**

- Search for cmd.exe
- Right-click for "Run as administrator" option

### **CLI Basics**

**File Naming:**

- Not case-sensitive by default

**Storage Devices:**

- Assigned letters (C:, D:, E:, etc.)
- Format: `Drive:\path\to\file`
- Example: `C:\Users\Jim\Desktop\file.txt`

**Command Switches:**

- Use forward slash (/) to separate command from options
- Example: `command /option`

**Navigation Shortcuts:**

- Tab key auto-completes directories/files
- Up/Down arrows access command history

**Device Switching:**

- Type drive letter + colon + Enter
- Example: `D:` switches to D drive

### **Windows PowerShell**

**Purpose:**

- Create scripts to automate tasks
- CLI for command execution
- Integrated within Windows

**Access:**

- Search for "powershell"
- Right-click for "Run as administrator"

**Command Types:**

**1. Cmdlets**

- Perform action and return output/object
- Output feeds to next command

**2. PowerShell Scripts**

- Files with `.ps1` extension
- Contain PowerShell commands

**3. PowerShell Functions**

- Pieces of code referenced in scripts

### **PowerShell Help System**

**Four Help Levels:**

1. **Basic Help**
   - Command: `get-help PS command`
   - Shows basic command information

2. **Help with Examples**
   - Command: `get-help PS command [-examples]`
   - Includes usage examples

3. **Detailed Help**
   - Command: `get-help PS command [-detailed]`
   - Detailed info with examples

4. **Full Help**
   - Command: `get-help PS command [-full]`
   - All information in greater depth

**Getting Started:**

- Type `help` in PowerShell for overview

---

## **Windows Management Instrumentation (WMI)**

### **Purpose**

- Manage remote computers
- Retrieve computer component information
- Monitor hardware and software statistics
- Monitor remote computer health

### **Access**

- Control Panel → Administrative Tools → Computer Management
- Expand Services and Applications tree
- Right-click WMI Control → Properties

### **WMI Control Properties - Four Tabs**

**1. General**

- Summary information about local computer
- WMI status and info

**2. Backup/Restore**

- Manual backup of WMI-gathered statistics

**3. Security**

- Configure WMI access permissions
- Control who accesses different statistics

**4. Advanced**

- Configure default namespace for WMI

### **Security Concerns**

**Attack Vector:**

- Attackers use WMI to connect to remote systems
- Modify registry remotely
- Run commands remotely

**Why Effective:**

- Common traffic (trusted by security devices)
- Remote WMI commands don't leave evidence on host
- Difficult to detect

**Mitigation:**

- ⚠️ Strictly limit WMI access
- Implement access controls

---

## **The net Command**

### **Purpose**

- Administration and maintenance of OS
- Multiple subcommands available
- Can combine with switches for specific output

### **Usage**

- Type `net help` at command prompt
- Lists all available net commands
- Type `net help [command]` for verbose help
- Example: `C:\> net help`

---

## **Task Manager and Resource Monitor**

### **Purpose**

- Understand running applications, services, processes
- Monitor computer performance (CPU, memory, network)
- Investigate malware-related problems
- Determine component performance issues

### **Task Manager Features**

- Information about running processes
- System performance metrics
- Resource usage details
- Manage applications
- Monitor system health
- Terminate unresponsive tasks

---

## **Networking**

### **Importance**

- Critical OS feature
- Enables network resource access
- Enables internet connectivity

### **Network Configuration Tool: Network and Sharing Center**

**Access:**

- Search for "Network and Sharing Center"

**Functions:**

- Verify or create network connections
- Configure network sharing
- Change network adapter settings

### **Initial View Information**

- Internet access status
- Network type (private, public, guest)
- Connection type (wired, wireless)
- HomeGroup membership

**Note:** HomeGroup removed from Windows 10 version 1803+

### **Change Adapter Settings**

- Access all available network connections
- Select adapter to configure
- Example: Configure Ethernet adapter for automatic IPv4

### **DNS Testing: nslookup**

- Essential for host address resolution
- Translates names (URLs) to addresses
- Command: `nslookup cisco.com`
- Confirms DNS functionality

### **Port and Connection Status: netstat**

- Check open ports
- View connection destinations
- Monitor connection status
- Command: `netstat`

---

## **Accessing Network Resources**

### **SMB Protocol**

- Server Message Block
- Originally developed by IBM
- Microsoft aided development
- Primarily for remote file access

### **UNC Format**

- Universal Naming Convention
- Format: `\\servername\sharename\file`
- **servername:** DNS name, NetBIOS name, or IP address
- **sharename:** Root folder on remote host
- **file:** Resource to access (may be nested deeper)

### **Network Sharing**

**Access Control:**

- Identify area of file system to share
- Apply access control to folders/files
- Restrict users/groups to specific functions (read, write, deny)

### **Administrative Shares**

**Definition:**

- Automatically created by Windows
- Identified by dollar sign ($) after share name

**Examples:**

- `C$`, `D$`, `E$` - Disk volumes
- `admin$` - Windows installation folder
- `print$` - Printers folder

**Access:**

- Only users with admin privileges can access

### **Connecting to Shares**

**Method 1: File Explorer**

- Type UNC in File Explorer address bar
- Windows prompts for credentials
- ⚠️ Use remote computer credentials, not local

**Method 2: Remote Desktop Protocol (RDP)**

- Log in to remote host
- Manipulate computer as if local
- Configuration changes, software installation, troubleshooting

**Access:**

- Search for "remote desktop"

### **RDP Security Concerns**

**Risks:**

- ⚠️ Natural target for threat actors
- Vulnerable on unpatched legacy Windows versions
- Found in industrial control systems

**Best Practices:**

- Limit RDP exposure to internet
- Use Zero Trust security approach
- Implement access control policies
- Restrict access to internal hosts only

---

## **Windows Server**

### **Overview**

- Edition of Windows for data centers
- Family of Microsoft products
- Began with Windows Server 2003

**Note:** Windows Server 2000 is client version (NT 5.0)

### **Services Provided**

**1. Network Services**

- DNS
- DHCP
- Terminal services
- Network Controller
- Hyper-V Network virtualization

**2. File Services**

- SMB
- NFS
- DFS

**3. Web Services**

- FTP
- HTTP
- HTTPS

**4. Management**

- Group policy
- Active Directory domain services control

---

## **What is Linux?**

### **Overview**

- Operating system created in 1991
- Open source, fast, reliable, small
- Minimal hardware requirements
- Highly customizable
- Community-maintained (not corporate)

### **Key Characteristics**

- ✓ Found on devices from wristwatches to supercomputers
- ✓ Designed for network connectivity
- ✓ Simplifies network application development
- ✓ Open source code available for inspection/modification
- ✓ Can be redistributed with or without charges

### **Linux Distributions (Distros)**

**Definition:**

- Packages created by different organizations
- Include Linux kernel + customized tools/software

**Examples:**

- Debian
- Red Hat
- Ubuntu
- CentOS
- SUSE

**Licensing:**

- Some charge for support (business-focused)
- Most offer free distribution without support

---

## **The Value of Linux**

### **Why Linux in Security Operations Center (SOC)**

**1. Open Source**

- Free acquisition
- Modify to fit specific needs
- Tailor-build for security analysis

**2. Powerful CLI**

- More powerful than GUI-based systems
- Less resource-intensive
- Remote task execution capability
- Direct terminal operations

**3. User Control**

- Root user (superuser) has absolute power
- Modify any OS aspect with few keystrokes
- Precise control over network stack
- Fine-grained network packet handling

**4. Network Communication Control**

- Inherent control in OS design
- Adjustable in practically every aspect
- Excellent platform for network applications
- Many network tools available for Linux only

### **Linux in SOC - Practical Application**

**Flexibility Benefits:**

- Tailor entire OS for security analysis
- Add only necessary packages (lean, efficient)
- Install/configure specific tools together
- Build customized computer for SOC workflow

**Example Tools:**

- **Sguil:** Cybersecurity analyst console
- **Security Onion:** Special Linux version
  - Open source suite of tools
  - Network security analysis focus
  - Tools work together seamlessly

---

## **Linux Tools**

### **Penetration Testing Tools**

**Definition:**

- PenTesting = process of finding vulnerabilities by attacking
- Look for weaknesses in networks/computers

**Tool Examples:**

- Packet generators
- Port scanners
- Proof-of-concept exploits

### **Kali Linux**

**Purpose:**

- Linux distribution grouping penetration tools
- Single distribution with many tools
- Great selection for security testing

---

## **Working in the Linux Shell**

### **The Linux Shell**

**Communication Methods:**

- CLI (Command Line Interface)
- GUI (Graphical User Interface)

**Default:** Linux often starts in GUI

**Accessing CLI from GUI:**

- Use terminal emulator application
- Common terminal emulators:
  - Terminator
  - eterm
  - xterm
  - konsole
  - gnome-terminal

**Browser-based Option:**

- JSLinux (created by Fabrice Bellard)
- Emulated Linux running in browser
- Access via internet search

### **Basic Commands**

**Command Definition:**

- Programs created to perform specific tasks

**Getting Help:**

- `man [command]` - Manual/documentation
- Example: `man ls` - Documentation for ls command

**Command Execution:**

- Shell searches specific directories (path)
- If not in path, must specify location
- Users can add directories to path

**Common Commands:**

- `mv` - Move or rename files
- `clear` - Clear terminal display
- `cat` - Display file contents

### **File and Directory Commands**

- `ls` - List directories (most frequently used)
- `pwd` - Print working directory
- `cd` - Navigate through directories
- `mkdir` - Create directories

---

## **Working with Text Files**

### **Text Editors in Linux**

**Types:**

- Graphical interfaces (convenient, easy)
- Command-line only (important for remote access)

**Features Vary:**

- Programmer-focused: syntax highlighting, bracket checking
- General purpose: basic editing
- Specialized: specific task support

**Importance of CLI Editors:**

- Allow remote file editing
- Essential for system administration
- No GUI overhead on remote systems

### **The Importance of Text Files in Linux**

**"Everything is a File" Philosophy:**

- Memory treated as file
- Disks treated as file
- Monitor treated as file
- Directories treated as file

**Configuration Files:**

- Text files storing settings/adjustments
- Control application/service behavior
- Often multiple config files per service
- Services read config files on startup
- Changes require service restart

**User Modification:**

- Users with proper permissions edit config files
- Changes saved and used by services
- Precise control over application behavior

**Example:**

- Command: `sudo nano /etc/hosts`
- `sudo` = superuser do (invoke superuser privilege)
- `nano` = text editor
- `/etc/hosts` = host file

## **Linux Servers and Clients**

### **Client-Server Communications**

**Server Definition:**

- Computer with software providing services to clients
- Connected across network

**Service Types:**

- External resources: files, email, web pages
- Maintenance tasks: log management, memory management, disk scanning

**One Server, Multiple Services:**

- Each service requires separate server software
- Example: File server software for file retrieval/submission

### **Servers, Services, and Their Ports**

**Port Definition:**

- Reserved network resource used by service
- Server "listens" on port for client requests

**Port Assignment:**

- Administrator can choose port
- Many clients configured for specific default port
- Common practice: use default port

**Well-Known Ports:**

- Standard ports for common services
- Examples provided in course materials

### **Clients**

**Client Definition:**

- Programs/applications communicating with specific server type
- Also called client applications

**Communication:**

- Use well-defined protocol
- Example: Web browsers (HTTP on port 80)

**Client Examples:**

- Web browsers → Web servers (HTTP, port 80)
- FTP clients → FTP servers (File Transfer Protocol)

---

## **Basic Server Administration**

### **Service Configuration Files**

**Purpose:**

- Manage Linux services
- Store service settings

**Common Configuration Options:**

- Port number
- Location of hosted resources
- Client authorization details

**Service Startup:**

- Service reads configuration files
- Loads settings into memory
- Adjusts behavior according to settings

**Configuration Changes:**

- Often require service restart
- Changes take effect after restart

**Privilege Requirements:**

- Services often require superuser privileges
- Configuration files often require superuser privileges to edit

**Example:**

- Nginx (lightweight web server) configuration file shown in course

---

## **Hardening Devices**

### **Device Hardening Definition**

- Implementing proven security methods
- Protecting device and administrative access

### **Hardening Methods**

**1. Password Management**

- Maintain strong passwords
- Force periodic password changes
- Prevent password reuse

**2. Enhanced Remote Login**

- Configure secure login features
- Implement SSH (Secure Shell)
- Disable root account SSH login

**3. Administrative Role Definition**

- Define access levels
- Not all IT personnel need same access
- Principle of least privilege

**4. Service Management**

- Disable unused services
- Many services enabled by default
- Some enabled for historical reasons
- Prevent auto-start at boot

**5. OS Updates**

- Critical for security
- New vulnerabilities discovered daily
- Developers issue fixes/patches regularly
- Up-to-date systems less likely compromised

### **Best Practices Checklist**

- ✓ Ensure physical security
- ✓ Minimize installed packages
- ✓ Disable unused services
- ✓ Use SSH and disable root SSH login
- ✓ Keep system updated
- ✓ Disable USB auto-detection
- ✓ Enforce strong passwords
- ✓ Force periodic password changes
- ✓ Prevent password reuse
- ✓ Other service/application-dependent steps

---

## **Monitoring Service Logs**

### **Log Files Definition**

- Records computer stores for important events
- Track system activity and health

**Log Types:**

- Kernel events
- Service events
- Application events

### **Importance of Log Review**

- Administrator periodically reviews logs
- Maintains computer health
- Identifies performance issues
- Detects security problems
- Guards against upcoming issues

### **Log Categories**

**1. Application Logs**

- Application-specific events

**2. Event Logs**

- System events

**3. Service Logs**

- Service-specific events

**4. System Logs**

- Core system events

### **Daemons**

**Definition:**

- Background processes running without user interaction

**Example:**

- System Security Services Daemon (SSSD)
  - Manages remote access
  - Handles authentication
  - Enables single sign-on

---

## **The Linux File System**

### **File System Types**

**Variety:**

- Many different file systems
- Vary in: speed, flexibility, security, size, structure, logic

**Administrator Choice:**

- Select file system best suited for OS and files

**Common Linux File Systems:**

- ext2, ext3, ext4
- NFS (Network File System)
- CDFS (CD File System)

### **Mounting**

**Definition:**

- Process of assigning directory to partition
- After mount, file system on partition accessible through directory
- Directory = mounting point

**Windows Equivalent:**

- Drive letters (C:, D:, E:)

**Root File System:**

- Represented by "/" symbol
- Contains all files by default

**Mount Command:**

- Display currently mounted file systems
- Show file system details

---

## **Linux Roles and File Permissions**

### **File Permissions Concept**

**Philosophy:**

- Most system entities treated as files
- File permissions organize system and enforce boundaries

**Permission Mechanism:**

- Built into file system structure
- Define actions owner, group, others can perform

**Permission Rights:**

- **R** (Read) - View file contents
- **W** (Write) - Modify file contents
- **X** (Execute) - Run file as program

### **Permission Display: ls -l Command**

**Output Format:**

- Provides extensive file information
- Displays permissions in User, Group, Other order

**Example: `-rwxrw-r--`**

**Permission Breakdown:**

- **First character:** `-` = file, `d` = directory
- **Characters 2-4 (User):** `rwx` = owner can read, write, execute
- **Characters 5-7 (Group):** `rw-` = group can read, write (not execute)
- **Characters 8-10 (Other):** `r--` = others can only read

### **File Information Fields**

**1. Permissions** - User, Group, Other rights

**2. Hard Links Count** - Number of hard links to file

**3. Owner** - User who owns file

**4. Group** - Group that owns file

**5. File Size** - In bytes

**6. Modification Date/Time** - Last change timestamp

**7. File Name** - Name of file

### **Permission Enforcement**

**Fundamental Rule:**

- File permissions cannot be broken
- User has only rights permissions allow

**Root User Exception:**

- Only root user can override file permissions
- Root can write to any file
- Root has full OS control

**Root Access Security:**

- Requires strong passwords
- Not shared with non-administrators
- Carefully controlled

### **Hard Links and Symbolic Links**

**Hard Link:**

- Another file pointing to same location
- Created with `ln` command
- Changes to hard-linked file affect original
- Limitations:
  - Difficult to locate
  - Limited to same file system
  - Cannot link to directories

**Symbolic Link (Symlink/Soft Link):**

- Similar to hard link (changes reflected)
- Created with `ln -s` command
- Shows original file location in `ls -l`
- Advantages over hard links:
  - Easy to locate (shows target)
  - Works across file systems
  - Can link to directories
- Disadvantage:
  - Single point of failure (if original deleted, symlink broken)

---

## **Working with the Linux GUI**

### **X Window System (X/X11)**

**Purpose:**

- Basic software framework for GUI
- Provides windowing system foundation

**Functions:**

- Drawing and moving windows
- Display device interaction
- Mouse and keyboard handling

**Server Architecture:**

- Works as server
- Remote users connect via network
- Application runs on server
- Graphical display sent over network
- Displayed on remote terminal

**Flexibility:**

- Doesn't specify user interface
- Other programs define graphical components
- Window managers create interface
- Allows great customization

**Customizable Components:**

- Buttons, fonts, icons
- Window borders, color schemes

**Window Manager Examples:**

- Gnome
- KDE

### **The Linux GUI**

**GUI Replacement:**

- Entire GUI can be replaced by user
- Not required for OS function
- Considered more user-friendly than CLI

**Ubuntu Linux Default:**

- Uses Gnome 3
- Goal: Enhanced user-friendliness

**GUI Variation:**

- Looks and feels vary by distribution
- Main components remain consistent

---

## **Working on a Linux Host**

### **Installing and Running Applications**

**Package Definition:**

- Program and all supporting files

**Package Manager Purpose:**

- Aids complex application installation
- Places all necessary files in correct locations

**Distribution-Specific Managers:**

- Arch Linux: pacman
- Debian/Ubuntu: dpkg (base) and apt (interface)

**Package Manager Commands:**

- `apt-get update` - Get package list, update local database
- `apt-get upgrade` - Update all installed packages to latest versions

### **Keeping System Up to Date**

**OS Updates (Patches):**

- Released periodically by OS companies
- Address known vulnerabilities
- Scheduled releases and emergency releases

**Update Notification:**

- Modern OS alerts when updates available
- Users can check anytime

**Ubuntu Linux:**

- Specific commands for updates (see LMS video lecture)

---

## **Processes and Forks**

### **Process Definition**

- Running instance of computer program
- Multitasking OS executes many simultaneously

### **Forking**

**Definition:**

- Kernel method allowing process to copy itself
- Only way to create new processes in Linux

**Importance:**

- Process scalability
- Multiple concurrent operations

**Example: Apache Web Server**

- Forks itself
- Serves large number of requests
- Uses fewer resources than single-process server

### **Parent-Child Relationship**

**Terminology:**

- Caller process = parent process
- Newly created process = child process

**After Fork:**

- Processes somewhat independent
- Different process IDs
- Run same program code

---

## **Malware on a Linux Host**

### **Malware Types**

- Viruses
- Trojan horses
- Worms
- Other malware types

### **Linux Protection**

**Better Protected Than Others:**

- File system structure
- File permissions
- User account restrictions

**Not Immune:**

- Many vulnerabilities discovered and exploited
- Range from server software to kernel vulnerabilities

**Fast Response:**

- Open source = quick fixes/patches
- Often available within hours of discovery

### **Attack Vectors**

**Primary Target:**

- Services and processes
- Server software vulnerabilities
- Kernel vulnerabilities

**Attack Method:**

- Exploit unpatched vulnerabilities
- Example: Outdated Apache web server
- Attackers probe open ports
- Research known vulnerabilities
- Launch targeted attacks

**Mitigation:**

- Keep system updated
- Close unused services/ports
- Reduce attack opportunities

---

## **Rootkit Check**

### **Rootkit Definition**

- Malware increasing unauthorized user privileges
- Grants access to restricted software portions
- Often secures backdoor to compromised computer

### **Rootkit Installation**

**Methods:**

- Automated (part of infection)
- Manual (after compromise)

**Privilege Requirements:**

- Vast majority require root/administrator access
- Few vulnerabilities allow regular user installation

### **Rootkit Danger**

**Deep Compromise:**

- Changes kernel code and modules
- Modifies fundamental OS operations
- Hides intrusion
- Removes installation tracks
- Tampers with diagnostic tools
- Hides rootkit presence

### **Rootkit Detection**

**Difficulty:**

- Very difficult due to deep compromise
- Typical methods:
  - Boot from trusted media (diagnostics live CD)
  - Mount compromised drive
  - Use trusted diagnostic tools
  - Inspect compromised file system

**Detection Methods:**

- Behavioral-based analysis
- Signature scanning
- Difference scanning
- Memory dump analysis

### **Rootkit Removal**

**Challenge:**

- Complicated and often impossible
- Especially if in kernel

**Solution:**

- Operating system re-installation (usually only real solution)
- Firmware rootkits require hardware replacement

### **chkrootkit Tool**

**Purpose:**

- Popular Linux program for rootkit detection
- Shell script using common Linux tools

**How It Works:**

- Uses `strings` and `grep` commands
- Compares core program signatures
- Looks for discrepancies in /proc file system
- Compares signatures with `ps` output

**Limitations:**

- ⚠️ Not 100% reliable
- Helpful but not foolproof

---

## **Piping Commands**

### **Piping Concept**

**Definition:**

- Technique chaining commands together
- Output of one command = input of next
- Named after pipe character: `|`

**Purpose:**

- Combine simple tools for complex tasks
- Create powerful command sequences

### **Example: Filtering Output**

**Individual Commands:**

- `ls` - List files and directories
- `grep` - Search for specified string in text

**Piped Together:**

- `ls | grep [search_term]`
- Filters `ls` output to show only matching items

**Result:**

- More focused, useful output
- Combines command capabilities

---

## **Linux Basics Summary**

### **Linux Overview**

- Fast, reliable, small open-source OS
- Minimal hardware requirements
- Highly customizable
- Network-designed
- Community-maintained

### **Linux Distributions**

- **Security Onion:** Network security monitoring tools
- **Kali Linux:** Penetration testing tools

### **Working in Linux Shell**

- **Communication:** CLI or GUI
- **Access:** Terminal emulator (xterm, gnome-terminal, etc.)
- **Commands:** Programs performing specific tasks
- **Help:** `man [command]` for documentation
- **Philosophy:** Everything treated as file

### **Linux Servers and Clients**

- **Servers:** Provide services to clients across network
- **Services:** External resources (files, email, web) or maintenance tasks
- **Ports:** Reserved network resources for services
- **Well-Known Ports:** Standard ports for common services
- **Clients:** Applications communicating with specific server types
- **Protocols:** Well-defined communication standards

### **Basic Server Administration**

- **Configuration Files:** Manage services and settings
- **Hardening:** Secure device and administrative access
- **Best Practices:**
  - Physical security
  - Minimal packages
  - Disable unused services
  - SSH with root login disabled
  - Regular updates
  - Strong passwords
  - Periodic password changes
  - Prevent password reuse
- **Log Monitoring:** Track system health and security

### **Linux File System**

- **Types:** ext2, ext3, ext4, NFS, CDFS (vary by speed, flexibility, security, size)
- **Mounting:** Assign directory to partition for access
- **Root File System:** "/" contains all files by default
- **File Permissions:** Read (r), Write (w), Execute (x)
- **Permission Levels:** User, Group, Other
- **Hard Links:** Another file pointing to same location
- **Symbolic Links:** Similar to hard links with advantages (cross-filesystem, directory linking)

### **Linux GUI**

- **X Window System:** Basic GUI framework
- **Window Managers:** Define graphical interface (Gnome, KDE)
- **Customization:** Buttons, fonts, icons, colors, borders
- **Flexibility:** Can be replaced by user

### **Working on Linux Host**

- **Package Managers:** Install complex applications (apt, dpkg, pacman)
- **Updates:** Regular OS patches for vulnerability fixes
- **Processes:** Running program instances
- **Forking:** Kernel method for process creation
- **Scalability:** Apache example of fork efficiency

### **Security Concerns**

- **Malware:** Viruses, Trojans, worms (less vulnerable but not immune)
- **Attack Vectors:** Services, outdated software, kernel vulnerabilities
- **Rootkits:** Deep malware modifying kernel (difficult to detect/remove)
- **Detection Tools:** chkrootkit (helpful but not 100% reliable)

### **Command Techniques**

- **Piping:** Chain commands with `|` for complex operations
- **Example:** `ls | grep [term]` filters directory listing
