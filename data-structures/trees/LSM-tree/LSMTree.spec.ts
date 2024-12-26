import { LSMTree } from './LSMTree';

describe('LSMTree', () => {
  let lsmTree: LSMTree;

  beforeEach(() => {
    lsmTree = new LSMTree(3); // Set memtable size limit to 3 for testing
  });

  describe('insert', () => {
    it('should insert key-value pairs into the memtable', () => {
      lsmTree.insert('key1', 'value1');
      expect(lsmTree.search('key1')).toBe('value1');
    });

    it('should flush memtable to SSTable when size limit is reached', () => {
      lsmTree.insert('key1', 'value1');
      lsmTree.insert('key2', 'value2');
      lsmTree.insert('key3', 'value3');
      expect(lsmTree.search('key1')).toBe('value1');
      expect(lsmTree.search('key2')).toBe('value2');
      expect(lsmTree.search('key3')).toBe('value3');
      lsmTree.insert('key4', 'value4');
      expect(lsmTree.search('key1')).toBe('value1'); // Should be in SSTable
      expect(lsmTree.search('key4')).toBe('value4'); // Should be in memtable
    });
  });

  describe('search', () => {
    it('should return undefined for non-existent keys', () => {
      expect(lsmTree.search('nonExistentKey')).toBeUndefined();
    });

    it('should return the correct value for existing keys in the memtable', () => {
      lsmTree.insert('key2', 'value2');
      expect(lsmTree.search('key2')).toBe('value2');
    });

    it('should return the correct value for existing keys in SSTables', () => {
      lsmTree.insert('key1', 'value1');
      lsmTree.insert('key2', 'value2');
      lsmTree.insert('key3', 'value3');
      lsmTree.insert('key4', 'value4'); // This should trigger a flush
      expect(lsmTree.search('key1')).toBe('value1');
      expect(lsmTree.search('key2')).toBe('value2');
      expect(lsmTree.search('key3')).toBe('value3');
      expect(lsmTree.search('key4')).toBe('value4');
    });
  });

  describe('delete', () => {
    it('should delete keys from the memtable', () => {
      lsmTree.insert('key1', 'value1');
      lsmTree.delete('key1');
      expect(lsmTree.search('key1')).toBeUndefined();
    });

    it('should delete keys from SSTables', () => {
      lsmTree.insert('key1', 'value1');
      lsmTree.insert('key2', 'value2');
      lsmTree.insert('key3', 'value3');
      lsmTree.insert('key4', 'value4'); // This should trigger a flush
      lsmTree.delete('key1');
      expect(lsmTree.search('key1')).toBeUndefined();
    });
  });

  describe('compactSSTables', () => {
    it('should merge multiple SSTables into one', () => {
      lsmTree.insert('key1', 'value1');
      lsmTree.insert('key2', 'value2');
      lsmTree.insert('key3', 'value3');
      lsmTree.insert('key4', 'value4'); // This should trigger a flush
      lsmTree.insert('key5', 'value5');
      lsmTree.insert('key6', 'value6'); // This should trigger another flush
      expect(lsmTree.getSSTableCount()).toBe(1);
      expect(lsmTree.search('key1')).toBe('value1');
      expect(lsmTree.search('key6')).toBe('value6');
    });
  });

  describe('edge cases', () => {
    it('should handle inserting and deleting the same key', () => {
      lsmTree.insert('key1', 'value1');
      lsmTree.delete('key1');
      expect(lsmTree.search('key1')).toBeUndefined();
      lsmTree.insert('key1', 'value2');
      expect(lsmTree.search('key1')).toBe('value2');
    });

    it('should handle inserting duplicate keys', () => {
      lsmTree.insert('key1', 'value1');
      lsmTree.insert('key1', 'value2');
      expect(lsmTree.search('key1')).toBe('value2');
    });
  });

  describe('state', () => {
    it('should return the current state of the memtable and SSTables', () => {
      lsmTree.insert('key1', 'value1');
      lsmTree.insert('key2', 'value2');
      expect(lsmTree.getMemtable().size).toBe(2);
      expect(lsmTree.getSSTables().length).toBe(0);
      lsmTree.insert('key3', 'value3');
      expect(lsmTree.getMemtable().size).toBe(0);
      expect(lsmTree.getSSTables().length).toBe(1);
      expect(lsmTree.getSSTables()[0].size).toBe(3);
    });
  });
});
