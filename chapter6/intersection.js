function intersection(first_array, second_array){
	let result = [];

	for(let i = 0;i < first_array.length;i++){
		for(let j = 0;j < second_array.length;j++){
			if(first_array[i] == second_array[j]){
				result.push((first_array[i]);
			}
		}
	}
	return result;
}
