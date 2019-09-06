const API_URL = 'http://127.0.0.1:12345';

function initApp(API_URL){
	let button = document.getElementById('input');
	if(message){
		
	}
	button.addEventListener('click',(event)=>{
		if(message){
			let message = document.getElementById('value').value;
			let div = document.createElement('div');
			div.className = "container darker";
			let img = document.createElement('img');
			img.src = "src/user.jpeg";
			img.className = "right";
			let text = document.createElement('p');
			text.textContent = message;
			div.appendChild(img);
			div.appendChild(text);
			let body = document.getElementById('message')
			body.insertBefore(div,body.childNodes[0]);
			let options = {
				"message":message
			}
			let headers = {
				'Accept': 'application/json',
				'Content-Type': 'application/json'
			};
			fetch(API_URL+"/v1/ask", {body:JSON.stringify(options),method:"POST",headers:headers})
      		.then(function(response) {
        		if (!response.ok) {
          			throw Error(response.statusText);
        		} else {
          			return response.json();
        		}
			  })
			  
      		.catch(err => {
        		console.warn(`API_ERROR: ${err.message}`);
        		window.alert(err.message);
			  })
			  
			.then((response)=>{
				let div = document.createElement('div');
				div.className = "container";
				let img = document.createElement('img');
				img.src = "src/bot.jpeg";
				let text = document.createElement('p');
				text.textContent = response['message'];
				div.appendChild(img);
				div.appendChild(text);
				let body = document.getElementById('message')
				body.insertBefore(div,body.childNodes[0]);
			})
		}
	})
}





initApp(API_URL);


