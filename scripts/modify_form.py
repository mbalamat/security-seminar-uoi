print "up and running"
def request(context, flow):
	with open("forms.txt", "a") as f:
		#f.write("requested\n")
		if "application/x-www-form-urlencoded" in flow.request.headers["content-type"]:
			form = flow.request.get_form_urlencoded()
			#f.write("incoming\n")
			f.write(str(form))
			f.write("\n")
			flow.request.set_form_urlencoded(form)
