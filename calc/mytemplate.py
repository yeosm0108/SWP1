def html(sum, product):
	return front + "<p>sum = {0}<br>product = {1}</p>".format(sum, product) + back


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

