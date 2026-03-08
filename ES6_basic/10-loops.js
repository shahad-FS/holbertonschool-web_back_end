export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    let value = idx;
    idx = appendString + value;
  }

  return array;
}
