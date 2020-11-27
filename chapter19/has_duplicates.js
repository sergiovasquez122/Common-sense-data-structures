function has_duplicate_values(array){
	for(let i = 0;i < array.length; i++){
		for(let j = 0; j < array.length; j++){
			if(i != j && array[i] == array[j]){
				return true;
			}
		}
	}
	return false;
}

function has_duplicates_v2(array){
	let existing_values = {};
	for(let i = 0;i < array.length;i++){
		if(!existing_values[array[i]]){
			existing_values[array[i]] = true;
		} else {
			return true;
		}
	}
	return false;
}

function has_duplicates_v3(array){
	array.sort((a, b) => (a < b) ? -1 : 1);

	for(let i = 0;i < array.length - 1; i++){
		if(array[i] == array[i + 1]){
			return true;
		}
	}
	return false;
}
