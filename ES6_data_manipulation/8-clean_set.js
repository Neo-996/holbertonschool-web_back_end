export default function cleanSet(mySet, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  return Array.from(mySet)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
}
