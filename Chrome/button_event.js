function myAlert(){
	alert('hello world');
}

//ºÏ¸¶Å© ±â´É
function bookmark() {
	window.open("bookmark.html","_blank", "width=500,height=500,0,status=0")
}

//¾È¾¸
function bookmark_list() {
	window.open("bookmarks_list.html","_blank", "width=500,height=500,0,status=0")
}
//ºÏ¸¶Å© ¸®½ºÆ®
function bookmarks_list() {
	chrome.tabs.create({'url':"chrome://bookmarks"})
}

//¾È¾¸
function save() {
  var htmlContent = ["your-content-here"];
  var bl = new Blob(htmlContent, {type: "text/html"});
  var a = document.createElement("a");
  a.href = URL.createObjectURL(bl);
  a.download = "your-download-name-here.html";
  a.hidden = true;
  document.body.appendChild(a);
  a.innerHTML = "something random - nobody will see this, it doesn't matter what you put here";
  a.click();
}



document.addEventListener('DOMContentLoaded', function(){
	var bookmarkURL = chrome.runtime.getURL("bookmark.html");
	document.getElementById('Scrap').addEventListener('click', myAlert);
	document.getElementById('Scrap').addEventListener('click', bookmark);
	document.getElementById('List').addEventListener('click', bookmarks_list);

});
		