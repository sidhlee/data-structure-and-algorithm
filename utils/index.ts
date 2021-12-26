/**
 *
 * @param cb wrapper function returns measuring function executed with arguments
 * @returns
 */
export function timeFunc(cb: () => any) {
  const start = performance.now();
  const result = cb();
  const end = performance.now();
  const delta = end - start;
  return [delta, result] as const;
}
