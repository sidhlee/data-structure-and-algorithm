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
});
