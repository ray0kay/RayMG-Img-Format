import zlib
import sys
import json

def save(name: str, width: int, height: int, pixels: list):
    assert len(pixels) == width * height * 4, "Pixel data must match image size (RGBA)"
    pixels = zlib.compress(bytearray(pixels))

    with open(name, 'wb') as f:
        f.write(b'RAY1')  # Magic header
        f.write(width.to_bytes(4, 'big'))
        f.write(height.to_bytes(4, 'big'))
        f.write(len(pixels).to_bytes(4, 'big'))
        f.write(pixels)

"""
JSON Spec File Structure:
{
  "output": "name.raymg",
  "width": 1,
  "height": 1,
  "values": [1, 2, 3, 255]
}
"""

if (len(sys.argv) > 1):
    with open(sys.argv[1], 'r') as f:
        data = json.load(f)
        name = data['output']
        width = data['width']
        height = data['height']
        pixels = data['values']
        save(name, width, height, pixels)
else:
    sys.exit(1)