import Chance from 'chance';
import stats from 'stats-lite';
import { timeFunc } from '../../utils';
import { hashString, HashTable } from './hashTable';

const chance = new Chance();

describe('hashString', () => {
  it('should return valid index', () => {
    const words = [...Array(50)].map(() => chance.word());
    const indices = words.map((word) => {
      return hashString(word, 13);
    });
    const isEveryIndexValid = indices.every((index) => index < 13);
    expect(isEveryIndexValid).toBe(true);
  });

  it('should have constant time regardless of the string length', () => {
    // create word first to not include the time for generating random string
    const smallWord = chance.word({ length: 1 });
    const mediumWord = chance.word({ length: 100 });
    const largeWord = chance.word({ length: 10000 });

    const [timeA] = timeFunc(() => hashString(smallWord));
    const [timeB] = timeFunc(() => hashString(mediumWord));
    const [timeC] = timeFunc(() => hashString(largeWord));

    const hasConstantTime = stats.stdev([timeA, timeB, timeC]) < 1;

    expect(hasConstantTime).toBe(true);
  });

  it('returns evenly distributed indices', () => {
    const words = [...Array(1000)].map(() => chance.word());
    const indices = words.map((word) => {
      return hashString(word);
    });

    const numberOfIndices = indices.reduce(
      (obj: { [key: string]: number }, index: number) => {
        if (obj[index]) {
          obj[index]++;
        } else {
          obj[index] = 1;
        }
        return obj;
      },
      {}
    );

    const indexCounts = Object.values(numberOfIndices);
    const uniqueIndices = Object.keys(numberOfIndices).map((index) =>
      parseInt(index)
    );

    const stdev = stats.stdev(indexCounts);
    const maxIndex = Math.max(...indices);
    expect(uniqueIndices.length).toBeGreaterThanOrEqual(maxIndex);
    expect(stdev).toBeLessThan(10);
  });
});

describe('HashMap', () => {
  let hashTable: HashTable;
  beforeEach(() => {
    hashTable = new HashTable();
    hashTable.set('one', 1);
    hashTable.set('five', 5);
    hashTable.set('three', 3);
    hashTable.set('four', 4);
    hashTable.set('two', 2);
  });
  it('should be able to set and get', () => {
    expect(hashTable.get('one')).toBe(1);
    expect(hashTable.get('two')).toBe(2);
    expect(hashTable.get('three')).toBe(3);
    expect(hashTable.get('four')).toBe(4);
    expect(hashTable.get('five')).toBe(5);
  });

  describe('get', () => {
    it('should return undefined if key is not found', () => {
      const hashTable = new HashTable();
      expect(hashTable.get('unknown key')).toBeUndefined();
    });
  });

  describe('keys', () => {
    it('should return all keys in table', () => {
      const keys = hashTable.keys();
      expect(keys.length).toBe(5);
      keys.forEach((key) => {
        expect(
          ['one', 'two', 'three', 'four', 'five'].find((v) => v === key)
        ).not.toBeUndefined();
      });
    });
  });

  describe('values', () => {
    it('should return all values in table', () => {
      const values = hashTable.values();
      expect(values.length).toBe(5);
      values.forEach((key) => {
        expect([1, 2, 3, 4, 5].find((v) => v === key)).not.toBeUndefined();
      });
    });
  });
});
