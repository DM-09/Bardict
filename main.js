function getAPI() {
  document.getElementById("res").innerHTML = '<br>검색중... <br>　' 
  
  var text = 'https://bardict-api.vercel.app/get/' + document.getElementById("search").value
  
  const xhr = new XMLHttpRequest();
 
  xhr.open('GET', text, true);
  xhr.responseType = 'json';
  xhr.send();

  xhr.onload = function() {
    const re = xhr.response;
    document.getElementById("res").innerHTML = '<br>' + re.res + '<br>　' 
  }
}
