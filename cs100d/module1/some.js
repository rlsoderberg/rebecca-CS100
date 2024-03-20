document.getElementById('UserAgent').value = navigator.userAgent; 
  
function displayText01(){
if (navigator.userAgent == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/122.0.2365.92")
{var text = document.getElementById("textField01");
text.style.display = "block"}
else
{var text = document.getElementById("textField02");
text.style.display = "block"}
}

function displayText02(){
if (navigator.userAgent == "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
    {var text = document.getElementById("textField11");
    text.style.display = "block"}
else
    {var text = document.getElementById("textField12");
    text.style.display = "block"}
}