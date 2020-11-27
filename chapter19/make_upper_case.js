function max_upper_case(array){
	let new_array = [];
	for(let i = 0;i < array.length; i++){
		new_array[i] = array[i].toUpperCase()
	}
	return new_array
}

function max_upper_case_inplace(array){
	let new_array = []
	for(let i = 0;i < array.length; i++){
		new_array[i] = new_array[i].toUpperCase()
	}
	return new_array;
}
