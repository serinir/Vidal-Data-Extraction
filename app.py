from http import server,HTTPStatus
#handler c'est comment on va servire , heda \
# howa le plus simple eyserbess le fichier courrent direct
handler = server.SimpleHTTPRequestHandler
address = '127.0.0.1/vidal'
port = 8000
#tuple fiha l'addres en premier puis le port
addr_port = (address,port)
# heda howa le serveur http 
httpd = server.HTTPServer(addr_port,handler)
# hna pour lui dir serbess a wlidi
httpd.serve_forever()
