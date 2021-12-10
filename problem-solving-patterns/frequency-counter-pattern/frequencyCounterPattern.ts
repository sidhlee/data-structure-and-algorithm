// O(n) Solution using dictionary
export function same(arr1: number[], arr2: number[]) {
  // convert input arrays into counter dictionary (number: count)
  const arr1Dict = getCounterDict(arr1);
  const arr2Dict = getCounterDict(arr2);
  // loop through items in first array
  for (const num in arr1Dict) {
    // check the squared number is in second array dict
    const squared = (parseInt(num) ** 2).toString();
    if (!(squared in arr2Dict)) return false;
    // check the count is the same in second array dict
    if (arr1Dict[num] !== arr2Dict[squared]) return false;
  }
  return true;
}

type Item = number | string;

function getCounterDict(arr: Item[]) {
  return arr.reduce((dict: { [key: Item]: number }, item: Item) => {
    dict[item] = dict[item] ? dict[item] + 1 : 1;
    return dict;
  }, {});
}

// O(n^2) solution
export function sameNaive(arr1: number[], arr2: number[]) {
  // Validate - if all items in the array have the same frequency, two arrays must have the same size.
  if (arr1.length !== arr2.length) {
    return false;
  }

  // Loop over the first array
  for (let i = 0; i < arr1.length; i++) {
    // Find the item from the second array
    const foundIndex = arr2.findIndex((squared) => squared === arr1[i] ** 2);
    // If the item cannot be found, return false
    if (foundIndex === -1) return false;
    // If the item is found, remove it from the second array to make sure we only count the matched item once.
    // This is how we check the item has the same frequency in both arrays.
    arr2.splice(foundIndex, 1);
  }
  // If finished looping, and found all corresponding item in the second array, return true.
  return true;
}

export function isAnagram(str1: string, str2: string) {
  const str1Dict = getCounterDict(str1.split(''));
  const str2Dict = getCounterDict(str2.split(''));
  for (const char of str1) {
    if (!(char in str2Dict)) return false;
    if (str1Dict[char] !== str2Dict[char]) return false;
  }
  return true;
}

export function sameFrequency(num1: number, num2: number) {
  const num1Str = num1.toString();
  const num2Str = num2.toString();
  if (num1Str.length !== num2Str.length) return false;

  const num1Dict = getCounterDict(num1Str.split(''));
  const num2Dict = getCounterDict(num2Str.split(''));
  for (const key in num1Dict) {
    if (!(key in num2Dict)) return false;
    if (num1Dict[key] !== num2Dict[key]) return false;
  }
  return true;
}

// defining as number[] | string[] will not work
// always define the item type first then use it as an array of it
type Arg = number | string;

export function areThereDuplicates(...args: Arg[]) {
  const argsDict = args.reduce((dict: { [key: Arg]: number }, arg: Arg) => {
    dict[arg] = dict[arg] ? dict[arg] + 1 : 1;
    return dict;
  }, {});
  for (const arg in argsDict) {
    if (argsDict[arg] > 1) return true;
  }
  return false;
}
