# **Introduction**

Roi selection tool allows you to select the region of interest of your
choice using simple mouse click. x & y coordinates of your mouse clicks are 
then stored in a csv file at the end. The produced csv file can be used for
computer vision based application development.

# **Demo**


![alt text](demo.gif)


# **Usage**
1. Clone the repo: `$git clone https://github.com/coolmunzi/roi_selection`
   
2. Create a virtual environment: `$conda create -n roi_selection python=3.6`
3. Install the dependencies: `$pip install -r requirements.txt`
4. Paste the image of your interest in the cloned directory and rename it to 'image.jpg'
5. Run the project: `$python roi_selection.py`
6. Select the region of your interest using _left click_ of the mouse
7. Once you have selected a polygonal shaped region of interest, click _middle button_ in mouse.
8. Polygonal Region of interest selected by you will be shown in an opencv window and (x,y) coordinates
of points clicked will be saved in a csv file named 'roi_coordinates.csv'

