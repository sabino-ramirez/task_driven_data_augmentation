import subprocess as s

for index in range(1, 17):
	if index < 10:
		test_id = "00" + str(index)
	elif index < 100:
		test_id = "0" + str(index)
	else:
		test_id = str(index)

	s.run(["mkdir", "/home/sabino/task_driven_data_augmentation/dataset/summer_training/patient" + test_id])
