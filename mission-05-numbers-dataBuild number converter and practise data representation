# Mission 5 — Numbers and Data

## 1. Task / Objective
Convert between decimal, binary and hexadecimal by hand, verify results with Python, build a number converter program, and explain text encoding.

## 2. Work Completed
- Completed manual number conversions with working shown.
- Verified all conversions using Python's built-in functions.
- Built `number_converter.py` and tested it with three inputs.
- Wrote notes on ASCII, UTF-8 and text encoding.

## 3. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| `python3` (interactive mode) | Verified conversions using `bin()`, `int()`, `hex()`, `ord()`, `chr()` |
| `python3 number_converter.py` | Ran the converter program |
| `bin()` | Converts a decimal integer to its binary string representation |
| `hex()` | Converts a decimal integer to its hexadecimal string representation |
| `int('...', base)` | Converts a string in a given base back to a decimal integer |
| `input()` | Reads user input from the keyboard |

## 4. My Understanding

### Task 5.1 — Manual Conversions

| Question | Working and Answer |
|----------|--------------------|
| Decimal 13 → Binary | 13 ÷ 2 = 6 remainder **1** → 6 ÷ 2 = 3 remainder **0** → 3 ÷ 2 = 1 remainder **1** → 1 ÷ 2 = 0 remainder **1** → Read remainders bottom-to-top: **1101** |
| Decimal 25 → Binary | 25 ÷ 2 = 12 R **1** → 12 ÷ 2 = 6 R **0** → 6 ÷ 2 = 3 R **0** → 3 ÷ 2 = 1 R **1** → 1 ÷ 2 = 0 R **1** → Answer: **11001** |
| Binary 1010 → Decimal | (1×8) + (0×4) + (1×2) + (0×1) = 8 + 0 + 2 + 0 = **10** |
| Binary 1101 → Decimal | (1×8) + (1×4) + (0×2) + (1×1) = 8 + 4 + 0 + 1 = **13** |
| Hex A → Decimal | A = **10** |
| Hex 1F → Decimal | (1×16) + (15×1) = 16 + 15 = **31** |
| Binary 1111 → Hex | (1×8) + (1×4) + (1×2) + (1×1) = 15 in decimal = **F** in hex |

### Task 5.2 — Python Verification

| Expression | Result | Matches Manual? |
|-----------|--------|-----------------|
| `bin(13)` | `'0b1101'` | Yes |
| `bin(25)` | `'0b11001'` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `hex(10)` | `'0xa'` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(15)` | `'0xf'` | Yes |

### Task 5.3 — Number Converter Program

The program `number_converter.py` asks the user for a decimal number, then displays its binary and hexadecimal equivalents. `bin()` converts the integer to a binary string prefixed with `0b`, and `hex()` converts it to a hexadecimal string prefixed with `0x`.

**Test results:**

| Test Number | Binary Output | Hexadecimal Output |
|------------|---------------|-------------------|
| 10 | 0b1010 | 0xa |
| 255 | 0b11111111 | 0xff |
| 42 | 0b101010 | 0x2a |

### Task 5.4 — How Is Text Stored?

- **ASCII code for uppercase A:** 65
- **ASCII code for lowercase a:** 97
- **Why encoding standards are needed:** A computer stores everything as numbers (sequences of bits). An encoding standard like ASCII or UTF-8 provides an agreed mapping between numbers and characters so that every computer interprets the same number as the same character. Without a standard, text created on one machine could display as gibberish on another.
- **Character not in basic ASCII:** The emoji 😊 (or any character like ₹, é, or 漢) is not part of the basic 128-character ASCII set. UTF-8 can represent these because it supports over a million code points.

## 5. Difficulties Faced
No major difficulties. I initially forgot that `bin()` and `hex()` include prefixes (`0b` and `0x`), so my first comparison looked wrong until I realised the prefix is just a label.

## 6. How I Resolved Them
I checked the Python documentation and understood that `0b` means binary and `0x` means hexadecimal — the actual digits after the prefix matched my manual work.

## 7. Evidence / Files
- `number_converter.py` — the working Python converter program.
- `README.md` — this file with manual conversions, Python verification and encoding notes.

## 8. Commit Details
**Commit message:** "Build number converter and practise data representation"
Work has been pushed to GitHub and verified.
