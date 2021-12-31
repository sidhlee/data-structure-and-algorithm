# Data Structure and Algorithm

A personal learning space for data structure and algorithm.
Notes and codes are created from many sources including:

- From Colt Steele's Udemy course: [JavaScript Algorithms and Data Structures Masterclass](https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/)

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

## Enabling jsdom methods with node environment

When your jest `testEnvironment` is `jsdom` (by default), it mocks methods on the global `window` object such as `performance`. If you set it to `node`, you need to provide your own global methods.

You can specify `setupFilesAfterEnv` inside `jest.config.js` file.

```js
module.exports = {
  setupFilesAfterEnv: ['./setup.js'],
};
```

Then, within the specified setup file, define the global method you want to add.

```js
global.performance = require('perf_hooks').performance;
```

- Source: [SO](https://stackoverflow.com/a/57825692)

## Mocking inner function with jest

If a function A is calling function B directly within the same module, it is not possible to mock A and test its call.

- [Direct function calls cannot be mocked](https://stackoverflow.com/a/55193363)

Also, after using `doMock` you need to flush the cached module by calling `jest.resetModules` to be able to import/require mocked modules.

- [Resetting cache after doMock](https://stackoverflow.com/a/57160160)

- [Mocking class instantiation within a method](https://stackoverflow.com/a/64549323)

## References

- [Using TypeScript with Jest](https://jestjs.io/docs/getting-started#using-typescript)

## Resources

- [Visualgo - for visualizing algorithms and stepping through pseudo codes](https://visualgo.net/en)
