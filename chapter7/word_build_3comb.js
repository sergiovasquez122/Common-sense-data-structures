// O(N**3)
function wordBuilder(array) {
	let collection = [];
	for(let i = 0; i < array.length; i++) {
		for(let j = 0; j < array.length; j++) {
			for(let k = 0; k < array.length; k++) {
				if (i !== j && j !== k && i !== k) {
					collection.push(array[i] + array[j] + array[k]);
				}
			}
		}
	}
	return collection;
}
