import Node from './node';
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
      jest.isolateModules(async () => {
        jest.doMock('./node', () => ({
          __esModule: true,
          default: jest.fn().mockImplementation(() => ({})),
        }));
        const { default: Node } = await import('./node');
        const { default: SinglyLinkedList } = await import(
          './singlyLinkedList'
        );

        const singlyLinkedList = new SinglyLinkedList();
        singlyLinkedList.push('hello');
        // expect(singlyLinkedList.tail?.val).toBe('hello');
        expect(Node).toBeCalledWith('hello');
      });
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
      const removedNode = threeNodeList.pop();
      expect(removedNode?.val).toBe('third');
    });

    it('should set head and tail to be null when popping only node', () => {
      const singlyLinkedList = new SinglyLinkedList();
      singlyLinkedList.push('only node');
      singlyLinkedList.pop();
      expect(singlyLinkedList.head).toBe(null);
      expect(singlyLinkedList.tail).toBe(null);
    });
  });
});
