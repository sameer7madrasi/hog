import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

