chrome.tabs.executeScript({
    code:'document.getElementById("articleBodyContents").innerText'   
}, function(result){
    var BodyText = result[0];
    document.querySelector('#result').innerHTML = BodyText;

})