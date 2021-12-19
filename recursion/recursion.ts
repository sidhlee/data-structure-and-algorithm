// Helper method recursion
export function collectOddValues(arr: number[]) {
  let result = [] as number[];

  function helper(helperInput: number[]) {
    if (helperInput.length === 0) return;
    const isOdd = helperInput[0] % 2 !== 0;
    if (isOdd) {
      result.push(helperInput[0]);
    }
    helper(helperInput.slice(1));
  }
  helper(arr);

  return result;
}

// Pure recursion
export function collectOddValuesPure(arr: number[]): number[] {
  let newArr = [] as number[];
  if (arr.length === 0) return newArr;
  const isOdd = arr[0] % 2 !== 0;
  if (isOdd) {
    newArr.push(arr[0]);
  }
  return newArr.concat(collectOddValuesPure(arr.slice(1)));
}
