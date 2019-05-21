confirm("기사 분석을 보시겠습니까?");

var send ="kkk";
chrome.tabs.getSelected(null, function (tab) {
    send = tab.url;
});

document.write("<script type='text/javascript' src='socket.js'><"+"/script>");
var socket = io.connect('http://localhost:801');  //localhost로 연결합니다.
socket.on('news', function (data) {  // 서버에서 news 이벤트가 일어날 때 데이터를 받습니다.
    console.log(data);
    socket.emit('my other event', { url: send });   //서버에 my other event 이벤트를 보냅니다.

});



