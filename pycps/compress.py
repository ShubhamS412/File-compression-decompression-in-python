import zlib, base64

d = open('demo.txt','r').read()
d_bytes = bytes(d,'utf-8')
compress_data = base64.b64encode(zlib.compress(d_bytes,9)) 
decoded_data = compress_data.decode('utf-8')
cp_file = open('compressed.txt','w')
cp_file.write(decoded_data)

decompressed_data = zlib.decompress(base64.b64decode(compress_data))
