# Problem Solving Patterns

From Colt Steele's Udemy course: [JavaScript Algorithms and Data Structures Masterclass](https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/)

## Jest Setup

- Install `@types/jest` to enable intellisense on Jest.
- To use ES6 import/export, install `@babel/plugin-transform-modules-commonjs` and add `.babelrc` file to include plugin.

## Test Explorer

If nvm is used to install node, you need to symlink the `which node` to the expected global path for node, otherwise, test explorer plugins will not work.

```bash
sudo ln -s "$(which node)" /usr/bin/node

# if the above is not allowed
sudo ln -s "$(which node)" /usr/local/bin
```

## References

- [Using TypeScript with Jest](https://jestjs.io/docs/getting-started#using-typescript)
