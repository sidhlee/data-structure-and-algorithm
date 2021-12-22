import {
  capitalizeFirst,
  capitalizeWords,
  collectOddValues,
  collectOddValuesPure,
  collectStrings,
  factorial,
  fib,
  flatten,
  flattenPure,
  isPalindrome,
  nestedEvenSum,
  power,
  productOfArray,
  reverse,
  someRecursive,
  stringifyNumbers,
  sumRange,
} from './recursion';

describe('collectOddValues', () => {
  it('works', () => {
    expect(collectOddValues([1, 2, 3, 4, 5])).toEqual([1, 3, 5]);
  });
});

describe('collectOddValuesPure', () => {
  it('works', () => {
    expect(collectOddValuesPure([1, 2, 3, 4, 5])).toEqual([1, 3, 5]);
  });
});

describe('power', () => {
  it('should return one for the exponent of zero', () => {
    expect(power(2, 0)).toBe(1);
  });
  it('should work', () => {
    expect(power(2, 2)).toBe(4);
    expect(power(2, 4)).toBe(16);
  });
});

describe('factorial', () => {
  it('should return factorial', () => {
    expect(factorial(1)).toBe(1);
    expect(factorial(2)).toBe(2);
    expect(factorial(4)).toBe(24);
    expect(factorial(7)).toBe(5040);
  });

  it('should return 1 given 0', () => {
    expect(factorial(0)).toBe(1);
  });
});

describe('productOfArray', () => {
  it('should work', () => {
    expect(productOfArray([1, 2, 3])).toBe(6);
    expect(productOfArray([1, 2, 3, 10])).toBe(60);
  });
  it('should throw when given an empty array', () => {
    // must call inside another function
    expect(() => productOfArray([])).toThrow(
      'array must have at least one number'
    );
  });
});

describe('sumRange', () => {
  it('should work', () => {
    expect(sumRange(6)).toBe(21);
    expect(sumRange(10)).toBe(55);
  });
});

describe('fib', () => {
  it('should work', () => {
    expect(fib(4)).toBe(3);
    expect(fib(10)).toBe(55);
    expect(fib(28)).toBe(317811);
    expect(fib(35)).toBe(9227465);
  });
});

describe('reverse', () => {
  it('should work', () => {
    expect(reverse('abc')).toBe('cba');
  });
});

describe('isPalindrome', () => {
  it('should return false if not palindrome', () => {
    expect(isPalindrome('awesome')).toBe(false);
    expect(isPalindrome('foobar')).toBe(false);
    expect(isPalindrome('amanaplanacanalpandemonium')).toBe(false);
  });

  it('should return true if palindrome', () => {
    expect(isPalindrome('tacocat')).toBe(true);
    expect(isPalindrome('amanaplanacanalpanama')).toBe(true);
  });
});

describe('someRecursive', () => {
  const isOdd = (num: number) => num % 2 !== 0;
  it('should return true', () => {
    expect(someRecursive([1, 2, 3, 4], isOdd)).toBe(true);
    expect(someRecursive([4, 6, 9], isOdd)).toBe(true);
  });

  it('should return false', () => {
    expect(someRecursive([4, 6, 8], isOdd)).toBe(false);
    expect(someRecursive([4, 6, 8], (val) => val > 10)).toBe(false);
  });
});

describe('flattenPure', () => {
  it('works', () => {
    expect(flattenPure([1, 2, 3, [4, 5]])).toEqual([1, 2, 3, 4, 5]);
    expect(flattenPure([1, [2, [3, 4], [[5]]]])).toEqual([1, 2, 3, 4, 5]);
    expect(flattenPure([[1], [2], [3]])).toEqual([1, 2, 3]);
    expect(flattenPure([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])).toEqual([1, 2, 3]);
  });
});

describe('flatten', () => {
  it('works', () => {
    expect(flatten([1, 2, 3, [4, 5]])).toEqual([1, 2, 3, 4, 5]);
    expect(flatten([1, [2, [3, 4], [[5]]]])).toEqual([1, 2, 3, 4, 5]);
    expect(flatten([[1], [2], [3]])).toEqual([1, 2, 3]);
    expect(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])).toEqual([1, 2, 3]);
  });
});

describe('capitalizeFirst', () => {
  it('works', () => {
    expect(capitalizeFirst(['car', 'taco', 'banana'])).toEqual([
      'Car',
      'Taco',
      'Banana',
    ]);
  });
});

describe('nestedEvenSum', () => {
  it('works', () => {
    const obj1 = {
      outer: 2,
      obj: {
        inner: 2,
        otherObj: {
          superInner: 2,
          notANumber: true,
          alsoNotANumber: 'yup',
        },
      },
    };

    const obj2 = {
      a: 2,
      b: { b: 2, bb: { b: 3, bb: { b: 2 } } },
      c: { c: { c: 2 }, cc: 'ball', ccc: 5 },
      d: 1,
      e: { e: { e: 2 }, ee: 'car' },
    };

    expect(nestedEvenSum(obj1)).toBe(6);
    expect(nestedEvenSum(obj2)).toBe(10);
  });
});

describe('capitalizeWords', () => {
  it('works', () => {
    let words = ['i', 'am', 'learning', 'recursion'];
    expect(capitalizeWords(words)).toEqual([
      'I',
      'AM',
      'LEARNING',
      'RECURSION',
    ]);
  });
});

describe('stringifyNumbers', () => {
  it('works', () => {
    let obj = {
      num: 1,
      test: [],
      data: {
        val: 4,
        info: {
          isRight: true,
          random: 66,
        },
      },
    };

    const expected = {
      num: '1',
      test: [],
      data: {
        val: '4',
        info: {
          isRight: true,
          random: '66',
        },
      },
    };

    expect(stringifyNumbers(obj)).toEqual(expected);
  });
});

describe('collectStrings', () => {
  it('works', () => {
    const obj = {
      stuff: 'foo',
      data: {
        val: {
          thing: {
            info: 'bar',
            moreInfo: {
              evenMoreInfo: {
                weMadeIt: 'baz',
              },
            },
          },
        },
      },
    };

    expect(collectStrings(obj)).toEqual(['foo', 'bar', 'baz']);
  });
});
