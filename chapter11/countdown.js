function countdown(number){
	console.log(number);

	if(number === 0){
		return
	} else{
		return countdown(number - 1)
	}
}
