# Bitwise Operations

Bitwise Operations you can use to solve algorithm challenges.

## XOR (^) operator

https://dev.to/bladesensei/xor-operator-in-programming-use-case-34ng

XOR (exclusive or) operator returns true(1) if two input bits are different, false if the same.

```text
>>> 8^5
13
>>> 5^8
13
>>> bin(8)
'0b1000'
>>> bin(5)
'0b101'

1000
0101
----
1101

>>> int('1101', 2)
13
```

Therefore, any number XOR 0 is equal to the number itself.

```py
0 ^ 0 == 0
1 ^ 1 == 0
A ^ 0 == a
A ^ A == 0
```

XOR operation has the associative property.
Rearranging the terms will not change the result.

```py
a^b^c == c^b^a
```

This properties can be used to find the only number in a array that appears odd number of times.

```py
a^b^c^a^b == a^a^b^b^c == 0^0^c == c
```
