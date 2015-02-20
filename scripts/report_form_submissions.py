def request(context, flow):
    if "application/x-www-form-urlencoded" in flow.request.headers["content-type"]:
        context.log("New form submission")
        context.log(str(flow.live.c.server_conn))
        form = flow.request.get_form_urlencoded()
        context.log(str(form))
        flow.request.set_form_urlencoded(form)
