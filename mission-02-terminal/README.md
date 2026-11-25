# Mission 2 — Become Comfortable with the Terminal

## 1. Task / Objective
Use the command-line interface to inspect folders, create and manage practice files, understand flags and pipes, and explain package managers.

## 2. Work Completed
- Practised basic Terminal operations (pwd, ls, cd, mkdir, touch, cp, mv, cat).
- Created a `terminal-practice` folder and performed file-management exercises inside it.
- Explored flags (`-l`, `-la`, `-lah`) and the pipe operator.
- Wrote notes on package managers.

## 3. Commands / Tools Used

### Task 2.1 — Basic Terminal Operations

| Operation | Command | What It Does | What I Observed |
|-----------|---------|-------------|-----------------|
| Current-directory display | `pwd` | Prints the full (absolute) path of the directory I am currently in | It showed the complete path from the root to my project folder |
| Directory listing | `ls` | Lists the names of files and folders in the current directory | I could see all the mission folders and the root README |
| Detailed listing | `ls -l` | Lists files with extra details — permissions, owner, size and modification date | Each entry showed a permission string, file size in bytes and the date it was last changed |
| Change directory | `cd ..` | Moves to the parent directory (one level up) | The path shown by `pwd` shortened by one folder |
| Create directory | `mkdir terminal-practice` | Creates a new empty folder with the given name | A new folder appeared in the listing |
| Create empty file | `touch sample.txt` | Creates a new empty file, or updates the timestamp if the file exists | An empty file named sample.txt appeared |
| Copy file | `cp sample.txt sample-backup.txt` | Makes a duplicate of the file with a new name | Both files appeared in the listing with the same size |
| Move / rename file | `mv sample-backup.txt renamed-backup.txt` | Renames or moves a file to a new name or location | The old name disappeared and the new name appeared |
| Display file contents | `cat sample.txt` | Prints the contents of a file to the Terminal | The text I had added to the file was displayed |

### Task 2.2 — Practise File Changes Safely

I created `terminal-practice/` inside the repository and worked only inside that folder.

```
echo "First line of text" > practice-file.txt
echo "Second line of text" >> practice-file.txt
cat practice-file.txt
cp practice-file.txt practice-backup.txt
mv practice-backup.txt renamed-backup.txt
```

**Answers:**
- **Replacing vs appending:** The `>` operator replaces the entire contents of a file with new text. The `>>` operator adds text to the end of the file without removing what is already there.
- **Copying vs moving:** Copying (`cp`) creates a second independent copy of the file so both the original and the copy exist. Moving (`mv`) removes the file from its original location and places it in the new location (or renames it in place).
- **Current-directory display (`pwd`):** It tells me exactly where I am in the file system so I can confirm I am working in the correct folder before running commands.
- **Directory listing (`ls`):** It shows what files and folders exist in the current location, which helps me verify that files were created, copied or renamed correctly.

### Task 2.3 — Flags and Pipes

| Command | What It Shows |
|---------|--------------|
| `ls` | Simple list of file and folder names |
| `ls -l` | Detailed list with permissions, owner, size and date |
| `ls -la` | Same as `-l` but includes hidden files (names starting with `.`) |
| `ls -lah` | Same as `-la` but shows file sizes in human-readable units (K, M, G) |

**Pipe example:**
```
ls -la | head -5
```
The pipe symbol `|` takes the output of the command on its left side and sends it as input to the command on its right side. Here, `ls -la` produces a full detailed listing, and `head -5` keeps only the first five lines. This is useful when output is long and I only need a portion.

### Task 2.4 — Package Managers

A package manager is a tool that automates installing, updating and removing software. Instead of downloading programs manually from websites, a package manager handles dependencies, versions and updates from a central collection of packages. On macOS, **Homebrew** is a commonly used package manager. Package managers are useful because they save time, keep software up to date and reduce the risk of installing incompatible versions.

## 4. My Understanding
The Terminal gives direct control over the file system through typed commands. Flags modify a command's behaviour — for example, `-l` makes `ls` show details instead of just names. Pipes connect commands together so the output of one becomes the input of another, which lets me chain simple tools into more powerful operations.

## 5. Difficulties Faced
No major difficulties. I had to be careful with `>` versus `>>` to avoid accidentally overwriting the file.

## 6. How I Resolved Them
I tested `>` and `>>` on a practice file first before using them on important files.

## 7. Evidence / Files
- `README.md` — this file with all command tables and explanations.
- `terminal-practice/` folder containing practice files created during the exercises.

## 8. Commit Details
**Commit message:** "Complete Terminal and file management mission"
Work has been pushed to GitHub and verified.
