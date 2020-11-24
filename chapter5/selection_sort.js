// (N-1) + (N-2) + (N-3) + ... + 1
// ((N - 1) * (N)) / 2
function selection_sort(array){
	for(let i = 0;i < array.length - 1; i++){
		let lowest_number_idx = i;
		for(let j = i + 1;j < array.length; j++){
			if(array[i] < array[lowest_number_idx]){
				lowest_number_idx = j;
			}
		}
	}
	if(lowest_number_idx != i){
		let temp = array[i];
		array[i] = array[lowest_number_idx];
		array[lowest_number_idx] = temp;
	}
	return array;
}
