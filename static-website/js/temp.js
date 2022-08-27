var data;
      
var form = document.getElementById('upload_form');

form.onsubmit = async (e) => {
e.preventDefault();
const form = e.currentTarget;
const url = 'http://127.0.0.1:8000/api/upload/'

try {
  const formData = new FormData(form);
  const response = await fetch(url, {
      method: 'POST',
      body: formData
  });
  var data_temp = await response.json();
  data=data_temp
  console.log(data_temp);
//   console.log(response);
} catch (error) {
  console.error(error);
}

}

function fun() {
    
}