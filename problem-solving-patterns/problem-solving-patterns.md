# Problem Solving Patterns

From Colt Steele's Udemy course: [JavaScript Algorithms and Data Structures Masterclass](https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/)

## An Example

Write a function called `same` which accepts two arrays. The function should return true if every value in the array has its corresponding value squared in the second array. The frequency of the values must be the same.

```js
same([1, 2, 3], [4, 1, 9]); // true
same([1, 2, 3], [1, 9]); // false
same([1, 2, 1], [4, 4, 1]); // false
```

## Jest Setup

- Install `@types/jest` to enable intellisense on Jest.
- To use ES6 import/export, install `@babel/plugin-transform-modules-commonjs` and add `.babelrc` file to include plugin.

## References

- [Using TypeScript with Jest](https://jestjs.io/docs/getting-started#using-typescript)

## Test Explorer

If nvm is used to install node, you need to symlink the `which node` to the expected global path for node, otherwise, test explorer plugins will not work.

```bash
sudo ln -s "$(which node)" /usr/bin/node

# if the above is not allowed
sudo ln -s "$(which node)" /usr/local/bin
```
