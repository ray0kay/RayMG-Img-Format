import zlib
import sys

try:
    from PIL import Image # type: ignore
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow==11.2.1'])
    from PIL import Image # type: ignore

def load(name: str):
    with open(name, 'rb') as f:
        magic = f.read(4)
        if magic != b'RAY1':
            raise ValueError('Not a valid .raymg file')
        width = int.from_bytes(f.read(4), 'big')
        height = int.from_bytes(f.read(4), 'big')
        size = int.from_bytes(f.read(4), 'big')
        data = zlib.decompress(f.read(size))
        return width, height, data

def show(name: str):
    width, height, data = load(name)
    image = Image.new('RGBA', (width, height))
    pixels = [tuple(data[i:i+4]) for i in range(0, len(data), 4)]
    image.putdata(pixels)
    image.show()

if len(sys.argv) > 1:
    file = sys.argv[1]
    show(file)
else:
    sys.exit(1)