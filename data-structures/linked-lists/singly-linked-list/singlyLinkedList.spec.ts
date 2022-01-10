import Node from './node';
import * as node from './node'; // for mocking default export
import SinglyLinkedList from './singlyLinkedList';

describe('SinglyLinkedList', () => {
  it('should have head, tail and length', () => {
    const singlyLinkedList = new SinglyLinkedList();
    expect(singlyLinkedList.head).not.toBeUndefined();
    expect(singlyLinkedList.tail).not.toBeUndefined();
    expect(singlyLinkedList.length).not.toBeUndefined();
  });

  describe('push', () => {
    it('should create a new node', () => {
      const NodeMock = jest
        .spyOn(node as any, 'default')
        .mockImplementationOnce(() => ({}));
      new SinglyLinkedList().push('hello');
      expect(NodeMock).toBeCalledWith('hello');
    });

    it('should increment length', () => {
      const singlyLinkedList = new SinglyLinkedList();
      singlyLinkedList.push('hello');
      expect(singlyLinkedList.length).toBe(1);
    });

    it('should set head on first push', () => {
      const singlyLinkedList = new SinglyLinkedList();
      singlyLinkedList.push('hello');
      expect(singlyLinkedList.head?.val).toBe('hello');
    });

    it('should set tail correctly', () => {
      const singlyLinkedList = new SinglyLinkedList();
      singlyLinkedList.push('hello');
      expect(singlyLinkedList.tail?.val).toBe('hello');
    });

    it("should set old tail's next", () => {
      const singlyLinkedList = new SinglyLinkedList();
      singlyLinkedList.push('hello');
      singlyLinkedList.push('world');
      expect(singlyLinkedList.head?.val).toBe('hello');
      expect(singlyLinkedList.head?.next?.val).toBe('world');
    });

    it('should return the instance', () => {
      const singlyLinkedList = new SinglyLinkedList();
      expect(singlyLinkedList.push('hello')).toBe(singlyLinkedList);
    });
  });

  describe('pop', () => {
    let threeNodeList: SinglyLinkedList<string>;
    let secondLastNode: Node<string>;
    beforeEach(() => {
      threeNodeList = new SinglyLinkedList<string>()
        .push('first')
        .push('second')
        .push('third');
      secondLastNode = threeNodeList?.head?.next as Node<string>;
    });
    it('returns undefined when there are no nodes', () => {
      const singlyLinkedList = new SinglyLinkedList();
      expect(singlyLinkedList.pop()).toBeUndefined();
    });

    it('sets the next of the 2nd last node to be null', () => {
      threeNodeList.pop();
      expect(secondLastNode?.next).toBe(null);
    });

    it('sets the 2nd last node to be tail', () => {
      threeNodeList.pop();
      expect(threeNodeList.tail).toBe(secondLastNode);
    });

    it('decrements the length by one', () => {
      expect(threeNodeList.length).toBe(3);
      threeNodeList.pop();
      expect(threeNodeList.length).toBe(2);
    });

    it('returns the removed node', () => {
      const removedNodeValue = threeNodeList.pop();
      expect(removedNodeValue).toBe('third');
    });

    it('should set head and tail to be null when popping only node', () => {
      const singlyLinkedList = new SinglyLinkedList();
      singlyLinkedList.push('only node');
      singlyLinkedList.pop();
      expect(singlyLinkedList.head).toBe(null);
      expect(singlyLinkedList.tail).toBe(null);
    });
  });

  describe('shift', () => {
    let threeNodeList: SinglyLinkedList<string>;
    let secondNode: Node<string>;
    beforeEach(() => {
      threeNodeList = new SinglyLinkedList<string>()
        .push('first')
        .push('second')
        .push('third');
      secondNode = threeNodeList?.head?.next as Node<string>;
    });
    it('returns undefined when there are no nodes', () => {
      const singlyLinkedList = new SinglyLinkedList();
      expect(singlyLinkedList.shift()).toBeUndefined();
    });

    it('sets the 2nd node to be the head', () => {
      threeNodeList.shift();
      expect(threeNodeList.head).toBe(secondNode);
    });

    it('decrements length by one', () => {
      expect(threeNodeList.length).toBe(3);
      threeNodeList.shift();
      expect(threeNodeList.length).toBe(2);
    });

    it('returns the removed node', () => {
      const removedNodeValue = threeNodeList.shift();
      expect(removedNodeValue).toBe('first');
    });

    it('should set head and tail to be null when shift only node', () => {
      const singlyLinkedList = new SinglyLinkedList();
      singlyLinkedList.push('only node');
      singlyLinkedList.shift();
      expect(singlyLinkedList.head).toBe(null);
      expect(singlyLinkedList.tail).toBe(null);
    });
  });

  describe('unshift', () => {
    let singlyLinkedList: SinglyLinkedList<string>;
    beforeEach(() => {
      singlyLinkedList = new SinglyLinkedList<string>();
    });

    it('should create a new node', () => {
      const NodeMock = jest
        .spyOn(node as any, 'default')
        .mockImplementationOnce(() => ({}));
      singlyLinkedList.unshift('hello');
      expect(NodeMock).toBeCalledWith('hello');
    });

    it('should increment length', () => {
      singlyLinkedList.unshift('hello');
      expect(singlyLinkedList.length).toBe(1);
    });

    it('should set head on first unshift', () => {
      singlyLinkedList.unshift('hello');
      expect(singlyLinkedList.head?.val).toBe('hello');
    });

    it('should set tail correctly', () => {
      singlyLinkedList.unshift('hello');
      expect(singlyLinkedList.tail?.val).toBe('hello');
    });

    it("should set new head's next", () => {
      singlyLinkedList.unshift('world');
      expect(singlyLinkedList.head?.next).toBe(null);
      singlyLinkedList.unshift('hello');
      expect(singlyLinkedList.head?.val).toBe('hello');
      expect(singlyLinkedList.head?.next?.val).toBe('world');
    });

    it('should return the instance', () => {
      expect(singlyLinkedList.unshift('hello')).toBe(singlyLinkedList);
    });
  });

  describe('get', () => {
    let list: SinglyLinkedList<string>;
    beforeEach(() => {
      list = new SinglyLinkedList<string>()
        .push('first')
        .push('second')
        .push('third');
    });
    it('should return correct node', () => {
      expect(list.get(2)?.val).toBe('third');
    });
    it('should return undefined for index out of range', () => {
      expect(list.get(-1)).toBe(undefined);
      expect(list.get(3)).toBe(undefined);
    });
    it('should return undefined when list is empty', () => {
      const list = new SinglyLinkedList();
      expect(list.get(4)).toBe(undefined);
    });

    it('should find the only node', () => {
      const list = new SinglyLinkedList().push('only item');
      expect(list.get(0)?.val).toBe('only item');
    });
  });

  describe('set', () => {
    it('should update the value of the target node', () => {
      const list = new SinglyLinkedList()
        .push('first')
        .push('second')
        .push('third')
        .set('two', 1);
      expect(list.head?.next?.val).toBe('two');
    });

    it('should throw when setting on an empty list', () => {
      const list = new SinglyLinkedList();
      expect(() => list.set('hey', 0)).toThrowError();
    });
  });

  describe('insert', () => {
    it('unshift the new node if index is 0', () => {
      const list = new SinglyLinkedList().push('one').insert('zero', 0);
      expect(list.head?.val).toBe('zero');
    });
    it('pushes the new node if index == length', () => {
      const list = new SinglyLinkedList().push('one').insert('last', 1);
      expect(list.tail?.val).toBe('last');
    });
    it('inserts node at the given index', () => {
      const list = new SinglyLinkedList().push('one').push('two');
      list.insert('one and a half', 1);
      expect(list.head?.next?.val).toBe('one and a half');
    });
    it('works with an empty list when the index is 0', () => {
      const list = new SinglyLinkedList().insert('new node', 0);
      expect(list.head?.val).toBe('new node');
    });
    it('throws when the index is invalid', () => {
      const list = new SinglyLinkedList();
      expect(() => list.insert('item', 1)).toThrowError();
    });
    it('should increment length', () => {
      const list = new SinglyLinkedList()
        .push('one')
        .push('two')
        .insert('item', 1);
      expect(list.length).toBe(3);
    });
  });

  describe('remove', () => {
    let list: SinglyLinkedList<string>;
    beforeEach(() => {
      list = new SinglyLinkedList<string>()
        .push('first')
        .push('second')
        .push('third');
    });
    it('returns undefined for invalid index', () => {
      expect(list.remove(-1)).toBeUndefined();
      expect(list.remove(3)).toBeUndefined();
    });

    it('returns undefined when the list is empty', () => {
      const list = new SinglyLinkedList();
      expect(list.remove(0)).toBeUndefined;
    });

    it('returns correct value when there is one node', () => {
      const list = new SinglyLinkedList().push('only node');
      expect(list.remove(0)).toBe('only node');
    });

    it('removes head and returns value', () => {
      expect(list.remove(0)).toBe('first');
      expect(list.head?.val).toBe('second');
    });

    it('removes tail and returns value', () => {
      expect(list.remove(2)).toBe('third');
      expect(list.tail?.val).toBe('second');
    });

    it('removes node in the middle and returns value', () => {
      expect(list.remove(1)).toBe('second');
    });

    it('connects prev and next after removing', () => {
      list.remove(1);
      expect(list.head?.next).toBe(list.tail);
    });
  });

  describe('reverse', () => {
    let list: SinglyLinkedList<string>;
    beforeEach(() => {
      list = new SinglyLinkedList<string>()
        .push('first')
        .push('second')
        .push('third')
        .push('fourth')
        .push('fifth');
    });

    it('works', () => {
      list.reverse();
      expect(list.head?.val).toBe('fifth');
      expect(list.head?.next?.val).toBe('fourth');
      expect(list.head?.next?.next?.val).toBe('third');
      expect(list.head?.next?.next?.next?.val).toBe('second');
      expect(list.head?.next?.next?.next?.next?.val).toBe('first');
      expect(list.tail?.val).toBe('first');
    });
    it('should have tail set to null', () => {
      list.reverse();
      expect(list.tail?.next).toBe(null);
    });

    it('should do nothing for list with one node', () => {
      const list = new SinglyLinkedList().push('one');
      expect(list.head?.val).toBe('one');
      expect(list.tail?.val).toBe('one');
      expect(list.length).toBe(1);
      list.reverse();
      expect(list.head?.val).toBe('one');
      expect(list.tail?.val).toBe('one');
      expect(list.length).toBe(1);
    });

    it('should do nothing for an empty list', () => {
      const list = new SinglyLinkedList();
      expect(list.head).toBe(null);
      expect(list.tail).toBe(null);
      expect(list.length).toBe(0);
      list.reverse();
      expect(list.head).toBe(null);
      expect(list.tail).toBe(null);
      expect(list.length).toBe(0);
    });
  });
});
