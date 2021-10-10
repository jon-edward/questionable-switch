# q_switch
A questionable implementation of switch cases in Python.

## Why should I use this?
You most definitely should not.

## What does it offer?
Because Python doesn't offer multiline lambda expressions, it most notably offers a way to thwart this limitation by expressing code blocks in the form of a mutiline string to force lazy execution of code blocks.

## How do I use this?
Simplest case.

```py
switch = Switch(4)
with switch as case:
  case[0] = "Zeroth"
  case[1] = "First"
  case[2] = "Second"
  case[3] = "Third"
  case[4] = "Fourth"
  
print(switch.value)
```

Switch with default case.
```py
switch = Switch(4)
with switch as case:
  case[0] = "Zeroth"
  case[1] = "First"
  case["default"] = "I lost count after 1."
 
 print(switch.value)
```

Switch with multiple cases per expression.
```py
switch = Switch(4)
with switch as case:
  case[0, 2, 4] = "Even"
  case[1, 3, 5] = "Odd"
  
print(switch.value)
```

Switch with code block (where it gets hacky).
```py
switch = Switch(4)
with switch as case:
  case[0] = "Zeroth"
  case[1] = "First"
  case[2] = "Second"
  case[3] = "Third"
  case[4] = CodeString("""
    one = 1
    two = one + 1
    three = two + 1
    four = three + 1
    value = four
  """)

print(switch.value)
```

Switch with code tuple (this is certainly worse).
```py
switch = Switch(4)
with switch as case:
  case[0] = "Zeroth"
  case[1] = "First"
  case[2] = "Second"
  case[3] = "Third"
  case[4] = CodeTuple(
    y := 1,
    y := y + 1,
    y := y + 1,
    y := y + 1,
    y
  )

print(switch.value)
```
