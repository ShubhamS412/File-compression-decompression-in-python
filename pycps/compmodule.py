import zlib, base64

def compress(inputfile,outputfile):
    d = open(inputfile,'r').read()
    d_bytes = bytes(d,'utf-8')
    compress_data = base64.b64encode(zlib.compress(d_bytes,9)) 
    decoded_data = compress_data.decode('utf-8')
    cp_file = open(outputfile,'w')
    cp_file.write(decoded_data)
    
#compress('demo.txt','op.txt')

def decompress(inputfile,outputfile):
    file_ctent = open(inputfile,'r').read()
    encoded_data = file_ctent.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    dcoded_data = decompressed_data.decode('utf-8')
    dp_file = open(outputfile,'w')
    dp_file.write(dcoded_data)
    #file.close()
    
#decompress('op.txt', 'dc1.txt')
