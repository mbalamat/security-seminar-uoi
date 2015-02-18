print "up and running"
def request(context, flow):
	with open("forms.txt", "a") as f:
		if "application/x-www-form-urlencoded" in flow.request.headers["content-type"]:
			f.write(str(flow.live.c.server_conn))
			form = flow.request.get_form_urlencoded()
			f.write("\n")
			f.write(str(form))
			f.write("\n")
			flow.request.set_form_urlencoded(form)
