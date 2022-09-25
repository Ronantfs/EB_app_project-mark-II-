var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var questionId = this.dataset.question
		var action = this.dataset.action
		console.log('questionId:', questionId, 'Action:', action)

        console.log('USER:', user)
		if (user == 'AnonymousUser'){
			console.log('User is not authenticated')
			
		}else{
			updateUserOrder(questionId, action)
		}

	})
}

function updateUserOrder(questionId, action){
    console.log('User is authenticated sending data')
    
    var url = '/update_item/'

		fetch(url, {
			method:'POST', //sending post-type data
			headers:{
				'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'questionId': questionId, 'action':action}) //send string'd data-object
		})
		.then((response) => {
            console.log(response);
		   return response.json();
		})
		.then((data) => {
            console.log(data)
		    location.reload()
		})
}
