from cgi import parse_qs
from template_pm import html

def application(environ, start_response):
	c = parse_qs(environ['QUERY_STRING'])
	a = c.get('a', [''])[0]
	b = c.get('b', [''])[0]
	r1 = 0
	r2 = 0
	if '' not in [a, b]:
		a, b = int(a), int(b)
		r1 = a + b
		r2 = a * b
	printstr = "Plus = " + str(r1) + " Multiply = " + str(r2)
	response_body = html + printstr
	start_response('200 OK', [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))])
	return [response_body]

