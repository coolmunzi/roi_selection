# **Introduction**

Roi selection script allows you to select the regoin of interest of your
choice using simple mouse click. x & y coordinates of your mouse click are 
then stored in a csv file at the end.

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
8. Polygonal Region of ineterest selected by you will be shown in an opencv window and (x,y) coordinates
of points clicked will be saved in a csv file named 'roi_coordinates.csv'

