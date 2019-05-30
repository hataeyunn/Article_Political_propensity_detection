confirm("기사를 분석하시겠습니까?");

var send ="kkk";
chrome.tabs.getSelected(null, function (tab) {
    send = tab.url;
});

document.write("<script type='text/javascript' src='socket.js'><"+"/script>");
var socket = io.connect('http://localhost:801');  //localhost濡??곌껐?⑸땲??
//var socket = io.connect('http://34.73.96.234:5000');
socket.on('news', function (data) {  // ?쒕쾭?먯꽌 news ?대깽?멸? ?쇱뼱?????곗씠?곕? 諛쏆뒿?덈떎.
    console.log(data);
    socket.emit('my other event', { url: send });   //?쒕쾭??my other event ?대깽?몃? 蹂대깄?덈떎.

});



