# RayMG
A simple custom image file I made with Python

## How to use
There are four files:
* create
* viewer
* ray2png
* png2ray
  
"create" requires a JSON file specifying the image
to create. It is structured in this format:

```
{
  "output": "name.raymg", // Name for the outputted image (must end in .raymg)
  "width": 83, // Number of pixels for the width of the image
  "height": 1, // Number of pixels for the height of the image
  "values": [ // An array containing RGBA values for the image
    205, 147, 132, 140, 29, 53, 1, 255,
    ... rest of the values
  ]
}
```

The height multiplied by the width, multiplied by 4 must
result in the amount of flat integers in the values array.
All values must be an integer. Floats will result in an error.
Once you are done, drag the JSON file onto the create
executable.

"viewer" requires a .raymg image file. Simply drag it onto
the executable and the image will display.

"ray2png" also requires a .raymg image file. Drag it onto
the executable and a "output.png" file will be outputted.

"png2ray" requires a .png file. Drag it onto the executable
and a "output.raymg" file will appear.
