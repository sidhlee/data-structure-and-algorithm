# Recursion

Recursion is commonly used in places where you deal with nested data structure (eg. trees, graphs, etc).

## Examples

Some of the examples using recursions are:

- JSON.parse, JSON.stringify
- DOM traversal algorithms eg. document.getElementById
- Object traversal

## How recursion works

Things that recursions are/do:

- Recursion uses the callstack to create temporary scope and store intermediate results.
- A recursive function calls itself with different input being reduced to a certain **base case**.

## Helper method recursion

A helper method recursion keeps a global variable in the outer function and defines a inner function to call recursively while modifying the variable in the outer scope. Upon hitting the base case, the outer function returns the variable. With helper method recursion, final return value is generated in the same order as the recursive call.

```js
function outer(input) {
  const outerScopedVariable = [];
  function helper(helperInput) {
    if (helperInput < 0) return;
    // modify outerScopedVariable
    helper(helperInput--);
  }
  helper(input);
  return outerScopedVariable;
}
```

## Pure recursion

A pure recursive function has to return the same datatype that we want to ultimately get after the recurs on. A temporary variable is created and initialized inside the function and modified using input before being returned. With pure recursion, the final return value is generated while backtracking. Spread operator or methods to merge temp object with the return value of recursive call is used. (eg. concat, Object.assign, ...)

```js
function pure(input) {
  const temp = [];
  if (input.length === 0) return temp;
  // add things to temp array based on input
  return temp.concat(pure(arr.slice(1)));
}
```
