// Adds the current date and time
let today = new Date();
let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
let time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
let dateTime = date+' '+time;

document.querySelector('#date-and-time').insertAdjacentHTML('afterbegin', dateTime)