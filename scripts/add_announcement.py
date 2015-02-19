from bs4 import BeautifulSoup
from libmproxy.protocol.http import decoded

DOMAIN = "uoi.gr"
MESSAGE = """We are here."""

def response(context, flow):
    context.log(flow.response.headers["content-type"])
    if flow.request.pretty_host(hostheader=True).endswith(DOMAIN) and \
        "text/html" in flow.response.headers["content-type"]:
        with decoded(flow.response):
            html = BeautifulSoup(flow.response.content)
            if html.body:
                div = html.new_tag("div")
                div.string = MESSAGE
                html.body.insert(0, div)
                flow.response.content = str(html)
                context.log("div inserted")
