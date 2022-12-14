console.log("JS script active")

var updateBtns = document.getElementsByClassName('update-cart')
//make buttons clickable & execute function with paramaters questionId
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
    console.log(questionId,action )
    
    var url = '/update_item/'
    var data = new FormData()
    data.append('questionId', questionId)
    data.append('action', action)
		fetch(url, {
			method:'POST', //sending post-type data
			headers:{
                'X-CSRFToken':csrftoken,
			}, 

			body: data        
		})
		.then((response) => {
            console.log('response: ', response);
		   return response.json();
		})
		.then((data) => {
            console.log('data: ', data)
		    location.reload()
		});
}
