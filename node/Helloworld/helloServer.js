
var http = require("http")

http.createServer(function ( request, response) {
    // Http status: 200: OK
    // Content Type: text/plain
    response.writeHead(200, {'Content-Type': 'text/plain'});
    // send the response body as "Hello world"
    response.end('Hello world\n');
}).listen(8082);
// console will print this msg
console.log('Server running at http://127.0.0.1:8081/');

