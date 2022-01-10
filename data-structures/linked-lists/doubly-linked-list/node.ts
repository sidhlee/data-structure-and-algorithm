export default class Node<T> {
  constructor(
    public val: T,
    public prev: Node<T> | null = null,
    public next: Node<T> | null = null
  ) {}
}
