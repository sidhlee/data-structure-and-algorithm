# Frequency Counters Pattern

When you have to compare more than two data instances, you can create a dictionary (or JavaScript object) to find the matching item with O(1) and make comparison for each item with O(n) time.
This pattern is useful when:

- to avoid nested loop (O(n^2)) for iterating through each array.
- need to compare more than two arrays
- need to compare frequency of occurrence (eg. number of certain item)

## Compare frequency of items

Write a function called `same` which accepts two arrays. The function should return true if every value in the array has its corresponding value squared in the second array. The frequency of the values must be the same.

```js
same([1, 2, 3], [4, 1, 9]); // true
same([1, 2, 3], [1, 9]); // false
same([1, 2, 1], [4, 4, 1]); // false
```

## Anagram

An anagram is a word that you can form by re-arranging existing letters in another word (eg. cinema and iceman).
Given a two string, write a function to determine if the second string is the anagram of the first.

```js
isAnagram('', ''); // true
isAnagram('aaz', 'zza'); // false
isAnagram('anagram', 'nagaram'); // true
isAnagram('rat', 'car'); // false
isAnagram('awesome', 'awesom'); // false
isAnagram('qwerty', 'qeyrwt'); // true
isAnagram('texttwisttime', 'timetwisttext'); // true
```
