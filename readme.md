# SQUAD Parking System Assignment

This is assignment project in python, and it simulates the working of a parking.

## Instructions for Ubuntu to run the Project 

1) Install Python3 [https://docs.python-guide.org/starting/install3/linux/](https://docs.python-guide.org/starting/install3/linux/) (Read Instructions to install Python3)
2) Install MongoDb by following the instructions provided at [https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
3) Start mongodb server using command:
sudo systemctl start mongodb
4) Install pymongo using command:
python3 -m pip install pymongo
5) Now, To run the project, clone the repository to your system
6) Now cd to the repo folder
7) Run the app.py file using command:
python3 app.py < input.txt

Example for input.txt:

Create_parking_lot 6
Park KA-01-HH-1234 driver_age 21
Park PB-01-HH-1234 driver_age 21
Slot_numbers_for_driver_of_age 21
Park PB-01-TG-2341 driver_age 40
Slot_number_for_car_with_number PB-01-HH-1234
Leave 2
Park HR-29-TG-3098 driver_age 39
Vehicle_registration_number_for_driver_of_age 18

## Instructions for Mac to run the Project
1) Install Python3 by following instructions at the link:
[https://docs.python-guide.org/starting/install3/osx/](https://docs.python-guide.org/starting/install3/osx/)
2) Install MongoDb by following instructions at the link:
[https://treehouse.github.io/installation-guides/mac/mongo-mac.html](https://treehouse.github.io/installation-guides/mac/mongo-mac.html)
3) Start mongodb server as given in the above link.
4) Install pymongo:
python -m pip install pymongo
5) Now, To run the project, clone the repository to your system and open the folder in the terminal
6) Run the app.py file using:
python3 [app.py](http://app.py/) < input.txt
