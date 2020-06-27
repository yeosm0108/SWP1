from cgi import parse_qs
from mytemplate import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a', [''])[0]
	b = d.get('b', [''])[0]


	if '' not in [a,b]:
		a, b = int(a), int(b)
		sum = a + b
		product = a * b
		response_body = html(sum = sum, product = product) 
	else:
		response_body = html(sum = 0, product = 0)

	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]

