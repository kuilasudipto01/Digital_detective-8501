# Mission 3 — Understand the Operating System

## 1. Task / Objective
Explore the operating system, running processes, storage, paths and file permissions, and describe the OS responsibilities.

## 2. Work Completed
- Gathered system information (OS version, storage, system activity).
- Observed running processes and identified PIDs.
- Explained absolute vs relative paths with examples.
- Examined file permissions.
- Completed the OS responsibilities table.

## 3. Commands / Tools Used

| Command | Purpose |
|---------|---------|
| sw_vers | Displays the macOS version and build number |
| whoami | Shows the currently logged-in user account |
| df -h | Displays available and used disk storage in human-readable format |
| top -l 1 | head -15` | Shows a snapshot of system activity including CPU and memory usage |
| `ps aux | head -10` | Lists currently running processes with details |
| pwd | Prints the absolute path of the current directory |
| ls -l| Shows file details including permission strings |

## 4. My Understanding

### Task 3.1 — System Exploration

| Information Explored | What It Tells You | Observation (privacy-safe) |
| Operating system details | The name, version and build of the OS running on the machine | macOS 27.2.1, Build 26B131 |
| Current account identity | Which user account is logged in and running commands | [redacted] |
| Available and used storage | How much disk space is used and how much remains free | 460 GB total, 13 GB used, 307 GB available |
| System activity snapshot | Real-time CPU and memory usage, number of running processes | Several hundred processes running; CPU mostly idle during normal use |

### Task 3.2 — Processes

- **What is a process?** A process is a program that is currently running in memory. When I open an application, the OS creates a process for it and allocates resources like CPU time and memory.
- **What does the PID column represent?** PID stands for Process Identifier. It is a unique number the OS assigns to each running process so it can track, manage and stop processes individually.
- **Two examples of processes:**
  1. A web browser (e.g., Google Chrome) — an application process I started.
  2. WindowServer — a background system process that manages the graphical display on macOS.

### Task 3.3 — Paths and Permissions

**Absolute path:** Starts from the root of the file system and gives the full location.
Example: /Users/[redacted]/Digital_detective-8501/mission-03-operating-system

**Relative path:** Starts from the current working directory.
Example: ../mission-02-terminal(from inside mission-03-operating-system, go up one level and into mission-02-terminal)

**File permissions (from ls -l):**


- r (read) — the owner can open and read the file.
- w (write) — the owner can modify the file.
- The owner does not have x (execute) permission on this file, which makes sense because a Markdown file is not meant to be run as a program.

### Task 3.4 — Operating System Responsibilities

| OS Responsibility | Explanation | Example |

Process management - The OS starts, schedules, pauses and stops processes so multiple programs can share the CPU fairly | When I switch between Chrome and VS Code, the OS gives each application CPU time |
Memory management - The OS allocates RAM to running programs and reclaims it when they close, making sure one program does not overwrite another's data | Opening a large file causes the OS to allocate more memory to the editor | Device management - The OS communicates with hardware devices through drivers so applications can use printers, keyboards, displays and storage without knowing low-level details | Plugging in a USB drive and the OS making it accessible in Finder |
File management - The OS organises files into directories, tracks their location on disk and controls read/write access | Creating folders and files in Terminal and seeing them appear in Finder |


## 5. Commit Details
**Commit message:** "Document operating system and file management"
Work has been pushed to GitHub and verified.
