def start(context, argv):
    context.poisoned = set()
def request(context, flow):
    host = flow.client_conn.connection.getpeername()[0]
    if flow.request.pretty_host(hostheader=True).endswith("ecourse.uoi.gr") and \
        not host in context.poisoned:
        flow.request.headers["cookie"] = ["foo"]
        context.poisoned.add(host)
