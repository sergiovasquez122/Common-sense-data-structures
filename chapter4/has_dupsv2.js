function hasDuplicateValue(array){
	let existing_numbers = [];
	for(let i = 0;i < array.length; i++){
		if(existing_numbers[array[i]] === 1){
			return true;
		} else{
			existing_numbers[array[i]] = 1;
		}
	}
	return false;
}
