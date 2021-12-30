export default class Node<T> {
  constructor(public val: T, public next: Node<T> | null = null) {}
}
