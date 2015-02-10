Security Presentation at UOI
============================

## HTTP is not secure!, 1hr:
- Marios goes on a (possibly known like Facebook) website via HTTP and logs in while Kostis is MitMing him. Marios logs in with his password and I sniff it.
    - What just happened? We'll show that we can sniff easily all HTTP traffic and alter it to our liking.
- Marios works on his laptop and downloads some software (eg. VLC).
    - He doesn't verify the authenticity of the software he just downloaded and runs it. The VLC binary he's running has been altered by Kostis.
- Ways to defend:
    - HTTPS
    - Checksum (SHA)
    - Briefly: GPG
- Further: Anyone can host a valid HTTPS site, should you trust any HTTPS site to download and run softwarefrom? NO!
