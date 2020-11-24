// O(N *  M)
function twoNumberProducts(array1, array2){
	let products = []

	for(let i = 0;i < array1.length; i++){
		for(let j = 0;j < array2.length; j++){
			products.push(array1[i] * array2[j]);
		}
	}
	return products;
}
