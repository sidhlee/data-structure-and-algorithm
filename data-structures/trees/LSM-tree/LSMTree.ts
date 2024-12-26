type Comparable = string | number;

class LSMTree {
  private memtable: Map<Comparable, Comparable>;
  private sstables: Map<Comparable, Comparable>[];
  private memtableSizeLimit: number;

  constructor(memtableSizeLimit: number = 5) {
    this.memtable = new Map();
    this.sstables = [];
    this.memtableSizeLimit = memtableSizeLimit;
  }

  insert(key: Comparable, value: Comparable) {
    this.memtable.set(key, value);
    if (this.memtable.size >= this.memtableSizeLimit) {
      this.flushMemtableToSSTable();
    }
  }

  search(key: Comparable): Comparable | undefined {
    if (this.memtable.has(key)) {
      return this.memtable.get(key);
    }
    for (const sstable of this.sstables) {
      if (sstable.has(key)) {
        return sstable.get(key);
      }
    }
    return undefined;
  }

  delete(key: Comparable) {
    if (this.memtable.has(key)) {
      this.memtable.delete(key);
    } else {
      for (const sstable of this.sstables) {
        if (sstable.has(key)) {
          sstable.delete(key);
          break;
        }
      }
    }
  }

  private flushMemtableToSSTable() {
    const newSSTable = new Map(this.memtable);
    this.sstables.push(newSSTable);
    this.memtable.clear();
    this.compactSSTables();
  }

  private compactSSTables() {
    if (this.sstables.length > 1) {
      const mergedSSTable = new Map<Comparable, Comparable>();
      for (const sstable of this.sstables) {
        for (const [key, value] of Array.from(sstable)) {
          mergedSSTable.set(key, value);
        }
      }
      this.sstables = [mergedSSTable];
    }
  }

  getMemtable() {
    return new Map(this.memtable);
  }

  getSSTables() {
    return this.sstables.map((sstable) => new Map(sstable));
  }

  getSSTableCount(): number {
    return this.sstables.length;
  }

  // Add more methods as needed
}

export { LSMTree };
