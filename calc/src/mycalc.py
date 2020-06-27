from cgi import parse_qs
import mytemplate as mt

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a', [''])[0]
	b = d.get('b', [''])[0]

	
	if environ['QUERY_STRING'] == '':
		response_body = mt.htmlEmpty()
	elif ''  in [a,b]:
		if a == '' and b == "":
			response_body = mt.htmlAlert("Please enter number.")
		else:
			response_body = mt.htmlAlert("Please enter number correctly.")
	else:
		if not a.isdigit() or not b.isdigit():
			response_body = mt.htmlAlert("Please enter digits.")
		else:
			a, b = int(a), int(b)
			sum = a + b
			product = a * b
			response_body = mt.htmlResult(sum = sum, product = product) 

	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]

