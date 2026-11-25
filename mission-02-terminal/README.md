# Mission 2 — Be comfortable with the terminal

## 1. Objective
Use the command-line interface to inspect folders, create and manage practice files, understand flags and pipes, and explain the role of package managers.

## 2. Work Completed
- Practised basic Terminal operations (pwd, ls, cd, mkdir, touch, cp, mv, cat) and created a terminal-practice folder and performed file-management exercises inside it also explored flags (-l, -la, -lah) and the pipe operator.

## 3. Commands / Tools Used

### Task 2.1 — Basic Terminal Operations

| Operation | Command | What It Does | What I Observed |
|-----------|---------|-------------|-----------------|
| Current-directory display | pwd | Prints the full path of the directory I am currently in | showed the complete path from the root to my project folder |
| Directory listing | ls | Lists the names of files and folders in the current directory | I could see all the mission folders |
| Detailed listing | ls -l | Lists files with extra details — permissions, owner, size and modification date | Each entry showed a permission string, file size in bytes and the date it was last changed |
| Change directory | cd .. | Mmves to the parent directory (one level up) | the path shown by pwd shortened by one folder |
| Create directory | mkdir terminal-practice | Creates a new empty folder with the given name | a new folder appeared in the listing |
| Create empty file | touch sample.txt | creates a new empty file| An empty file named sample.txt appeared |
| Copy file | cp sample.txt sample-backup.txt | makes a duplicate of the file with a new name | both files appeared in the listing with the same size |
| Move / rename file | mv sample-backup.txt renamed-backup.txt | Renames or moves a file to a new location | the old name disappeared and the new name appeared |
| Display file contents | cat sample.txt | prints the contents of a file to the Terminal | the text I had added to the file was displayed |

### Task 2.2 — Practise File Changes Safely

'''
echo "First line of text" > practice-file.txt
echo "Second line of text" >> practice-file.txt
cat practice-file.txt
cp practice-file.txt practice-backup.txt
mv practice-backup.txt renamed-backup.txt
'''

### Task 2.3 — Flags and Pipes

| Command | What It Shows |
|---------|--------------|
| ls | Simple list of file and folder names |
| ls -l | Detailed list with permissions, owner, size and date |
| ls -la | Same as -l but includes hidden files (names starting with .) |
| ls -lah | Same as -la but shows file sizes in human-readable units (K, M, G) |

**Pipe example:**
ls -la | head -5

The pipe symbol '|' takes the output of the command on its left side and sends it as input to the command on its right side. Here, 'ls -la' produces a full detailed listing, and 'head -5' keeps only the first five lines. This is useful when output is long and I only need a portion.

### Task 2.4 — Package Managers

A package manager is a tool that automates installing and removing software. Homebrewis a commonly used package manager, package managers are useful because they save time, keep software up to date.

## 4. what i learned
The terminal gives direct control over the file system through typed commands. Flags modify a command's behaviour — for example, '-l' makes 'ls' show details instead of just names. 

## 5. How to Resolved Them
I tested '>' and '>>' on a practice file first before using them on important files.

