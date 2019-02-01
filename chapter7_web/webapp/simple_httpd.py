'''
用python建構 web服務器 ，需要有這5行code
'''

# 導入 HTTP server 和 CGI model  (HTTP伺服器和CGI模塊)
from http.server import HTTPServer, CGIHTTPRequestHandler

# 指定一個端口
port = 8080

# 創建一個 HTTP server
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)

# 顯示一個友好的消息，並啟動server (服務器)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

