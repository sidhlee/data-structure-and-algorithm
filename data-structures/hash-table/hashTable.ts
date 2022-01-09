/**
 * Converts string key to the valid index of the table
 * @param key the key maps to the value we're storing to the table
 * @param tableSize length of the array we store values
 * @returns the index of the table where the value of the key is to be stored
 */
export function hashString(key: string, tableSize: number = 13) {
  const WEIRD_PRIME = 31;
  // iterate through the string character and get sum of the character code
  // than mod by the length of the array to get the valid index
  let total = 0;
  // limiting number of characters to iterate for constant time hashing
  for (let i = 0; i < Math.min(key.length, 100); i++) {
    const charCode = key[i].charCodeAt(0) - 96; // alphabet begins at 96
    total = (total * WEIRD_PRIME + charCode) % tableSize;
  }
  return total;
}

export class HashTable {
  keyMap: any[];
  constructor(size = 53) {
    this.keyMap = new Array(size);
  }

  set(key: string, value: any) {
    const index = this.hash(key);
    if (!this.keyMap[index]) {
      this.keyMap[index] = [];
    }
    // save key to find the key inside the "chain" after finding the index by hash
    this.keyMap[index].push([key, value]);
  }

  get(key: string) {
    const index = this.hash(key);
    const chain = this.keyMap[index];
    if (chain) {
      for (let i = 0; i < chain.length; i++) {
        if (chain[i][0] === key) {
          return chain[i][1];
        }
      }
    }
    return undefined;
  }

  keys() {
    const keys = [];
    for (let i = 0; i < this.keyMap.length; i++) {
      if (this.keyMap[i]) {
        for (let j = 0; j < this.keyMap[i].length; j++) {
          keys.push(this.keyMap[i][j][0]);
        }
      }
    }
    return keys;
  }

  values() {
    const values = [];
    for (let i = 0; i < this.keyMap.length; i++) {
      if (this.keyMap[i]) {
        for (let j = 0; j < this.keyMap[i].length; j++) {
          values.push(this.keyMap[i][j][1]);
        }
      }
    }
    return values;
  }

  private hash(key: string) {
    return hashString(key, this.keyMap.length);
  }
}
