import Node from './node';
import * as node from './node'; // for mocking default export
import DoublyLinkedList from './doublyLinkedList';
import SinglyLinkedList from '../singly-linked-list/singlyLinkedList';
import { timeFunc } from '../../../utils';

describe('DoublyLinkedList', () => {
  it('should have head, tail and length', () => {
    const doublyLinkedList = new DoublyLinkedList();
    expect(doublyLinkedList.head).not.toBeUndefined();
    expect(doublyLinkedList.tail).not.toBeUndefined();
    expect(doublyLinkedList.length).not.toBeUndefined();
  });

  describe('push', () => {
    let doublyLinkedList: DoublyLinkedList<string>;
    beforeEach(() => {
      doublyLinkedList = new DoublyLinkedList<string>();
    });
    it('should create a new node', () => {
      const NodeMock = jest
        .spyOn(node as any, 'default')
        .mockImplementationOnce(() => ({}));
      new DoublyLinkedList().push('hello');
      expect(NodeMock).toBeCalledWith('hello');
    });

    it('should increment length', () => {
      doublyLinkedList.push('hello');
      expect(doublyLinkedList.length).toBe(1);
    });

    it('should set head on first push', () => {
      doublyLinkedList.push('hello');
      expect(doublyLinkedList.head?.val).toBe('hello');
    });

    it('should set tail correctly', () => {
      doublyLinkedList.push('hello');
      expect(doublyLinkedList.tail?.val).toBe('hello');
    });

    it("should set old tail's next", () => {
      doublyLinkedList.push('hello').push('world');
      expect(doublyLinkedList.head?.val).toBe('hello');
      expect(doublyLinkedList.head?.next?.val).toBe('world');
    });

    it("should have only node's prev set to null", () => {
      doublyLinkedList.push('first');
      expect(doublyLinkedList.tail?.prev).toBe(null);
    });

    it('should set prev on the new node', () => {
      doublyLinkedList.push('first').push('second');
      expect(doublyLinkedList.tail?.prev?.val).toBe('first');
    });

    it('should return the instance', () => {
      const doublyLinkedList = new DoublyLinkedList();
      expect(doublyLinkedList.push('hello')).toBe(doublyLinkedList);
    });
  });

  describe('pop', () => {
    let threeNodeList: DoublyLinkedList<string>;
    let secondLastNode: Node<string>;
    beforeEach(() => {
      threeNodeList = new DoublyLinkedList<string>()
        .push('first')
        .push('second')
        .push('third');
      secondLastNode = threeNodeList?.head?.next as Node<string>;
    });
    it('returns undefined when there are no nodes', () => {
      const doublyLinkedList = new DoublyLinkedList();
      expect(doublyLinkedList.pop()).toBeUndefined();
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
      const doublyLinkedList = new DoublyLinkedList();
      doublyLinkedList.push('only node');
      doublyLinkedList.pop();
      expect(doublyLinkedList.head).toBe(null);
      expect(doublyLinkedList.tail).toBe(null);
    });
  });

  describe('shift', () => {
    let threeNodeList: DoublyLinkedList<string>;
    let secondNode: Node<string>;
    beforeEach(() => {
      threeNodeList = new DoublyLinkedList<string>()
        .push('first')
        .push('second')
        .push('third');
      secondNode = threeNodeList?.head?.next as Node<string>;
    });
    it('returns undefined when there are no nodes', () => {
      const doublyLinkedList = new DoublyLinkedList();
      expect(doublyLinkedList.shift()).toBeUndefined();
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
      const doublyLinkedList = new DoublyLinkedList();
      doublyLinkedList.push('only node');
      doublyLinkedList.shift();
      expect(doublyLinkedList.head).toBe(null);
      expect(doublyLinkedList.tail).toBe(null);
    });

    it("should set new head's prev to be null", () => {
      threeNodeList.shift();
      expect(threeNodeList.head?.prev).toBe(null);
    });
  });

  describe('unshift', () => {
    let doublyLinkedList: DoublyLinkedList<string>;
    beforeEach(() => {
      doublyLinkedList = new DoublyLinkedList<string>();
    });

    it('should create a new node', () => {
      const NodeMock = jest
        .spyOn(node as any, 'default')
        .mockImplementationOnce(() => ({}));
      doublyLinkedList.unshift('hello');
      expect(NodeMock).toBeCalledWith('hello');
    });

    it('should increment length', () => {
      doublyLinkedList.unshift('hello');
      expect(doublyLinkedList.length).toBe(1);
    });

    it('should set head on first unshift', () => {
      doublyLinkedList.unshift('hello');
      expect(doublyLinkedList.head?.val).toBe('hello');
    });

    it('should set tail correctly', () => {
      doublyLinkedList.unshift('hello');
      expect(doublyLinkedList.tail?.val).toBe('hello');
    });

    it("should set new head's next", () => {
      doublyLinkedList.unshift('world');
      expect(doublyLinkedList.head?.next).toBe(null);
      doublyLinkedList.unshift('hello');
      expect(doublyLinkedList.head?.val).toBe('hello');
      expect(doublyLinkedList.head?.next?.val).toBe('world');
    });

    it('should return the instance', () => {
      expect(doublyLinkedList.unshift('hello')).toBe(doublyLinkedList);
    });

    it("should set old head's prev to the new node", () => {
      doublyLinkedList.unshift('first').unshift('second');
      expect(doublyLinkedList.tail?.prev?.val).toBe('second');
    });
  });

  describe('get', () => {
    let list: DoublyLinkedList<string>;
    beforeEach(() => {
      list = new DoublyLinkedList<string>()
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
      const list = new DoublyLinkedList();
      expect(list.get(4)).toBe(undefined);
    });

    it('should find the only node', () => {
      const list = new DoublyLinkedList().push('only item');
      expect(list.get(0)?.val).toBe('only item');
    });

    it('should work faster when getting value near the end', () => {
      const singlyLinkedList = new SinglyLinkedList();
      const doublyLinkedList = new DoublyLinkedList();
      for (let i = 0; i < 10000; i++) {
        singlyLinkedList.push('item');
        doublyLinkedList.push('item');
      }
      const [singlyDelta] = timeFunc(() => singlyLinkedList.get(9999));
      const [doublyDelta] = timeFunc(() => doublyLinkedList.get(9999));
      expect(doublyDelta).toBeLessThan(singlyDelta / 2);
    });
  });

  describe('set', () => {
    let list: DoublyLinkedList<string>;
    beforeEach(() => {
      list = new DoublyLinkedList<string>()
        .push('first')
        .push('second')
        .push('third');
    });
    it('should update the value of the target node', () => {
      list.set('two', 1);
      expect(list.head?.next?.val).toBe('two');
    });

    it('should correctly set prev', () => {
      list.set('two', 1);
      expect(list.get(1)?.prev?.val).toBe('first');
    });

    it('should throw when setting on an empty list', () => {
      const list = new DoublyLinkedList();
      expect(() => list.set('hey', 0)).toThrowError();
    });
  });

  describe('insert', () => {
    let list: DoublyLinkedList<string>;
    beforeEach(() => {
      list = new DoublyLinkedList<string>()
        .push('first')
        .push('second')
        .push('third');
    });
    it('unshift the new node if index is 0', () => {
      list.insert('zero', 0);
      expect(list.head?.val).toBe('zero');
    });
    it('pushes the new node if index == length', () => {
      list.insert('last', 3);
      expect(list.tail?.val).toBe('last');
    });
    it('inserts node at the given index', () => {
      list.insert('one and a half', 1);
      expect(list.head?.next?.val).toBe('one and a half');
    });
    it('works with an empty list when the index is 0', () => {
      const list = new DoublyLinkedList().insert('new node', 0);
      expect(list.head?.val).toBe('new node');
    });
    it('throws when the index is invalid', () => {
      const list = new DoublyLinkedList();
      expect(() => list.insert('item', 1)).toThrowError();
    });
    it('should increment length', () => {
      expect(list.length).toBe(3);
    });

    it('should correctly set prev', () => {
      list.insert('second last', list.length - 1);
      expect(list.tail?.prev?.val).toBe('second last');
      expect(list.tail?.prev?.prev?.val).toBe('second');
    });
  });

  describe('remove', () => {
    let list: DoublyLinkedList<string>;
    beforeEach(() => {
      list = new DoublyLinkedList<string>()
        .push('first')
        .push('second')
        .push('third');
    });
    it('returns undefined for invalid index', () => {
      expect(list.remove(-1)).toBeUndefined();
      expect(list.remove(3)).toBeUndefined();
    });

    it('returns undefined when the list is empty', () => {
      const list = new DoublyLinkedList();
      expect(list.remove(0)).toBeUndefined;
    });

    it('returns correct value when there is one node', () => {
      const list = new DoublyLinkedList().push('only node');
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

    it('sets prev correctly after removing', () => {
      list.remove(1);
      expect(list.tail?.prev?.val).toBe('first');
    });
  });

  describe('reverse', () => {
    let list: DoublyLinkedList<string>;
    beforeEach(() => {
      list = new DoublyLinkedList<string>()
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
      const list = new DoublyLinkedList().push('one');
      expect(list.head?.val).toBe('one');
      expect(list.tail?.val).toBe('one');
      expect(list.length).toBe(1);
      list.reverse();
      expect(list.head?.val).toBe('one');
      expect(list.tail?.val).toBe('one');
      expect(list.length).toBe(1);
    });

    it('should do nothing for an empty list', () => {
      const list = new DoublyLinkedList();
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
