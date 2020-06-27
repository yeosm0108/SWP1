def htmlResult(sum, product):
	return front + "<p>sum = {0}<br>product = {1}</p>".format(sum, product) + back


def htmlEmpty():
	return front + back


def htmlAlert(str alertMessage):
	return front + '<script> alert("' + alertMessage + '")</script>'



front=b"""
<html>
	<body>
		<form action="">
			a = <input type=number name="a"> <br>
			b = <input type=number name="b"> <br>
			<button type="submit">Calculate</button>
		</form>
"""


back=b"""
	</body>
</html>
"""

