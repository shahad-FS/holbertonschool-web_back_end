function hasValuesFromArray(set, arr) {
	const isHas = arr.every((item) => set.has(item));
	return isHas;
}
export default hasValuesFromArray;
