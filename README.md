# labrotation-ai

Create images with shapes on it like that:
python createShapes border_width
It creates 28x28 pixel images with 1 pixel margin, where no shapes are drawn, and draws one shape with black borders on that image. Border_width 0 would mean the shapes are filled. There will be 123201 rectangles and as many ellipses. Pictures of rectangles and ellipses will take around 500MB on the disk each. There are 40 million possible triangles. That would be to many, so I created 200000 randomly. The images will be in the folder 'images' with according subfolders.
The size variable is a list with 2 entries: [horizontal width, vertical height]
The area variable is a list which contains 4 entries: [nth pixel from the left, nth pixel from the top, horizontal width in pixel, vertical height in pixel]
Up until now I tried to elimate cases in which the area of the shape is 0.
I did not look for doules. The Triangle with the pointlist [[1,2],[2,2],[3,3]] is the same as the one with pointlist [[2,2],[1,2],[3,3]] and there are at least 4 more. That means we have every triangle six times.
I do not know if there are doubles for rectangles or ellipses.
