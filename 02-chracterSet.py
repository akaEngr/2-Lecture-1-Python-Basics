
# ! python character set

"""
A character set is the collection of valid characters that Python understands and can use to write code —
like letters, digits, symbols, and whitespace characters.

Python internally uses Unicode (UTF-8 encoding by default),
which means it supports characters from almost every language (English, Hindi, emojis, etc.).


| Category                     | Examples                                               | Description / Use                                                         |
| ---------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------- |
| **Letters**                  | `A–Z`, `a–z`                                           | Used in identifiers, variables, and strings.                              |
| **Digits**                   | `0–9`                                                  | Used in numeric literals and identifiers (not at start).                  |
| **Special Symbols**          | `+  -  *  /  =  %  @  #  &  ( ) [ ] { } : ; , . < >`   | Used in expressions, operators, and syntax.                               |
| **Whitespace Characters**    | `space`, `\t`, `\n`, `\r`, `\f`                        | Used for formatting and separating tokens.                                |
| ↳ **Space (` `)**            | Literal space                                          | Separates tokens.                                                         |
| ↳ **Tab (`\t`)**             | Horizontal tab                                         | Adds a tab space.                                                         |
| ↳ **Newline (`\n`)**         | Line Feed                                              | Moves to next line.                                                       |
| ↳ **Carriage Return (`\r`)** | Returns cursor to start of line (used in old systems). |                                                                           |
| ↳ **Form Feed (`\f`)**       | Advances to next “page” (rarely used today).           |                                                                           |
| **Escape Sequences**         | `\\`, `\'`, `\"`, `\n`, `\t`, `\r`, `\f`               | Used to represent special characters in strings.                          |
| **ASCII Characters**         | `A–Z`, `a–z`, `0–9`, basic symbols (`@ # $ % & * ...`) | Original 7-bit character encoding (0–127). Still compatible with Unicode. |
| **Unicode Characters**       | `\u0905` → अ, `\u2764` → ❤                            | Supports all world languages, emojis, and symbols.                        |
| **Comments**                 | `# This is a comment`                                  | Used to explain code, ignored by interpreter.                             |
"""

# ! used of form feed\f
# ! Original Purpose (History 🖨️)
# ! it breaks into parts because \f is treated as whitespace.
# ! In old printers and typewriters:
# * \f told the printer: “End this page and start a new one.”
# * It literally fed the paper forward → form feed.
print("--")
text = "Hello\fWorld"
print(text)
print(text.split())
# ['Hello', 'World']


print(ord("A")) # 65
print(chr(65)) # 65
print(ord("\n")) # 10
print(ord("\u2034")) # 8244
print(("\u2034")) # ‴

print("Hello\tWorld")     # tab
print("Line1\nLine2")     # newline
print("Hello\rWorld")     # carriage return
"""
Step-by-step:
Python first prints: Hello
Then \r sends the cursor back to the beginning of the same line.
Then World starts printing from the beginning, replacing the earlier characters.

✅ Output you’ll see: World

(Here, "World" overwrites "Hello", so only “World” is visible.)
"""

print("Page1\fPage2")     # form feed
print("Unicode:", "\u0905", "\u2764")  # अ ❤


"""
Hello   World
Line1
Line2
World
Page1Page2
Unicode: अ ❤
(Note: carriage return \r may overwrite text depending on the terminal.)
"""