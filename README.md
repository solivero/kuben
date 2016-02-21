# Rubik's cube in Blender

This add-on for Blender creates a 3D model of a rubik's cube, which can be solved interactively using a custom UI.

- Cube model creation
- UI controls for manipulating the cube
- Algorithm parser

### Usage
In an empty scene, add a cube from the *Add* menu (not mesh->cube!). In the object menu to the right you will find the UI for cube operations.
Note that you must use the the **blender render engine**, be in **object mode** and use **texture viewport shading** to view the cube correctly.
![Imgur](http://i.imgur.com/l4vkSTe.png "Cube interface")
### Version
0.1

This project is in very early stages an highly experimental
### Installation
Zip all .py files. In Blender goto *File*->*User preferences*->*Add-ons*->*Install from file* and choose the zip you just created. You should now be able to search for and activate "Rubiks cube" addon.

### Todos

- Animate
- Rendered view
- Autosolve
- Realistic Materials
