# Mission 4 — How Programs Run

## 1. Task / Objective
Create and run a simple Python program, then compare how compilers and interpreters translate and execute programs.

## 2. Work Completed
- Created `hello.py` that prints "Hello from Python".
- Ran it successfully using `python3` from Terminal.
- Completed a compiler vs interpreter comparison table.
- Wrote an explanation in my own words.

## 3. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| VS Code | Created and edited the `hello.py` file |
| `python3 hello.py` | Ran the Python program from Terminal |
| `cat hello.py` | Displayed the contents of the program file to verify it |

## 4. My Understanding

### Task 4.1 — Creating and Running hello.py

I created `hello.py` with the following content:
```python
print("Hello from Python")
```
Running `python3 hello.py` in Terminal displayed:
```
Hello from Python
```
The program ran successfully on the first attempt.

### Task 4.2 — Compiler vs Interpreter Comparison

| Point | Compiler | Interpreter |
|-------|----------|-------------|
| When translation / execution happens | Translates the entire source code into machine code before the program runs | Reads and executes the source code line by line at runtime |
| Typical output | Produces a standalone executable file (e.g., a `.exe` or binary) | Does not produce a separate file; the result appears directly during execution |
| One example | `gcc` (compiles C programs) | `python3` (interprets Python programs) |
| One advantage | The compiled program usually runs faster because translation is already done | Easier to test and debug because you can run code immediately without a separate compile step |

**Explanation:**
A compiler takes the entire source code and translates it into machine code (or another lower-level form) in one go before the program is ever run. This means there is a build step, but the resulting executable runs quickly. An interpreter, on the other hand, reads the source code line by line and executes each instruction immediately at runtime without producing a separate executable file. This makes development faster because I can change a line and re-run instantly, but execution can be slower since translation happens every time. Python primarily uses an interpreter, which is why I can type `python3 hello.py` and see the output straight away without a compile step. In practice, many languages mix both approaches — Python actually compiles to bytecode internally before the interpreter runs it.

## 5. Difficulties Faced
No major difficulties. The program was simple and ran on the first try.

## 6. How I Resolved Them
Not applicable.

## 7. Evidence / Files
- `hello.py` — the working Python program.
- `README.md` — this file with the comparison and explanation.

## 8. Commit Details
**Commit message:** "Compare compilers and interpreters"
Work has been pushed to GitHub and verified.
