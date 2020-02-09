import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

parking_db = myclient["parking_db"]

parking = parking_db["parking"]


# print(myclient.list_database_names())
parking_lot_size = 0
parking_lot_capacity = 0




command_map = {
	"Create_parking_lot": 1,
	"Park": 2,
	"Slot_numbers_for_driver_of_age": 3,
	"Slot_number_for_car_with_number": 4,
	"Vehicle_registration_number_for_driver_of_age": 5,
	"Leave": 6
}

def get_command():
	try:
		command = input().strip()
	except EOFError:
		return -1, ""
	return command_map[command.split()[0]], command

def make_parking_lot(command):
	global parking_lot_size, parking_lot_capacity, parking
	temp = command.split(' ')
	parking_lot_size = int(temp[1])
	parking.delete_many({})

def park(command):
	global parking_lot_size, parking_lot_capacity, parking
	temp = command.split(' ')
	if(parking_lot_size == parking_lot_capacity):
		print("Sorry No Space In the Parking")
		return
	reg_no = temp[1]
	age = int(temp[3])
	parking_lot_size += 1

	all_slots = parking.find({}).sort("slot_no", pymongo.ASCENDING)
	empty_slot = 1
	for slot in all_slots:
		if(slot["slot_no"] == empty_slot):
			empty_slot += 1
		else:
			break
	slot_info = {
		"slot_no": empty_slot,
		"reg_no": reg_no,
		"driver_age": age
	}
	parking.insert_one(slot_info)


def find_slots_for_driver_age(command):
	global parking_lot_size, parking_lot_capacity, parking
	age = int(command.split(' ')[1])
	slots = parking.find({"driver_age": age})
	print("Slot Numbers are:")
	for slot in slots:
		print(slot["slot_no"])

def find_slot_no(command):
	global parking_lot_size, parking_lot_capacity, parking
	reg_no = command.split(' ')[1]
	slot = parking.find_one({"reg_no" : reg_no})
	print("Slot Number is:", slot["slot_no"])


def find_regs(command):
	global parking_lot_size, parking_lot_capacity, parking
	age = int(command.split(' ')[1])
	slots = parking.find({"driver_age": age})
	print("Registration Numbers are:")
	for slot in slots:
		print(slot["reg_no"])

def leave_parking(command):
	global parking_lot_size, parking_lot_capacity, parking
	if(parking_lot_size == 0):
		print("Parking is empty")
		return
	slot_no = int(command.split()[1])
	parking.delete_one({"slot_no": slot_no})
	parking_lot_size -= 1


def exec(command_type, command):
	if(command_type == 1):
		print(command, "running", ".........")

		make_parking_lot(command)

		print("Done..........")
	elif(command_type == 2):
		print(command, "running", ".........")

		park(command)

		print("Done..........")
	elif(command_type == 3):
		print(command, "running", ".........")

		find_slots_for_driver_age(command)

		print("Done..........")
	elif(command_type == 4):
		print(command, "running", ".........")

		find_slot_no(command)

		print("Done..........")
	elif(command_type == 5):
		print(command, "running", ".........")

		find_regs(command)

		print("Done..........")
	elif(command_type == 6):
		print(command, "running", ".........")

		leave_parking(command)

		print("Done..........")
	else:
		print(command, "Some Problem with the Input")


def main():
	command_type, command = get_command()
	while(command_type != -1):
		# print(command_type, command)
		exec(command_type, command)
		command_type, command = get_command()

if __name__ == '__main__':
	main()