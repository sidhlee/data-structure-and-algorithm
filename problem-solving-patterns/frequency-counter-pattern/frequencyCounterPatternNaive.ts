// O(n^2) solution
export function same(arr1: number[], arr2: number[]) {
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
