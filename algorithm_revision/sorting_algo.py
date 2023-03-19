import random
import time

array_length = 10
sorting_algo_cnt = 5

class sorting:
	def compare_x_y_greater(self, x, y):
		self.compare_counter += 1
		if (x>y):
			return False
		else:
			return True

	def swap_x_y(self, temp_array, x, y):
		self.swap_counter += 1
		if self.debug_level > 1:
			print("Before Swap:" + str(temp_array))
		temp_num = temp_array[x]
		temp_array[x] = temp_array[y]
		temp_array[y] = temp_num
		if self.debug_level > 1:
			print("After Swap:" + str(temp_array))
		return temp_array

	def initial_status(self):
		self.compare_counter = 0
		self.swap_counter = 0
		self.unsorted_array = self.initial_array.copy()
		self.sorted_array.clear()
		if self.debug_level > 0:
			print(self.unsorted_array)

	def print_status(self, sort):
		if sort:
			print("Sorted_array: " + str(self.sorted_array))
		print("Compare_cnt: " + str(self.compare_counter) + "; Swap_cnt: " + str(self.swap_counter) + "\n")
		
	def champion_problem(self, temp_array):
		temp_min = temp_array[0]
		temp_min_idx = 0

		for index in range(len(temp_array)):
			if (self.compare_x_y_greater(temp_min, temp_array[index]) == 0):
				temp_min = temp_array[index]
				temp_min_idx = index
		if self.debug_level > 1:
			print(temp_min)
		return (temp_min, temp_min_idx)

	def selection_sort(self, temp_array):
		head_idx = 0
		temp_min = temp_array[head_idx]

		while head_idx < (len(temp_array) - 1):
			temp_min, temp_min_idx = self.champion_problem(temp_array[head_idx:])
			self.swap_x_y(temp_array, head_idx, (temp_min_idx + head_idx))
			head_idx += 1
			if self.debug_level > 0:
				print(head_idx, temp_array)
		return temp_array

	def insertion_sort(self, temp_array):
		temp_min, temp_min_idx = self.champion_problem(temp_array)

		length_idx = 1
		while length_idx < (len(temp_array)):
			head_idx = length_idx
			while (head_idx > 0) and (self.compare_x_y_greater(temp_array[head_idx-1], temp_array[head_idx]) == 0):
				self.swap_x_y(temp_array, head_idx, (head_idx -1))
				head_idx -= 1
			length_idx += 1
			if self.debug_level > 0:
				print(length_idx, temp_array)
		return temp_array

	def merge_sort(self, temp_array):
		half_size = int(len(temp_array) / 2)
		temp_arr_0 = temp_array[0:half_size]
		temp_arr_1 = temp_array[(half_size):]
		arr_idx_0 = 0
		arr_idx_1 = 0

		temp_arr_0 = self.selection_sort(temp_arr_0)
		temp_arr_1 = self.selection_sort(temp_arr_1)
		for idx in range(len(temp_array)):
			if arr_idx_0 < half_size and arr_idx_1 < half_size:
				if not (self.compare_x_y_greater(temp_arr_0[arr_idx_0], temp_arr_1[arr_idx_1])):
					temp_array[idx] = temp_arr_1[arr_idx_1]
					arr_idx_1 += 1
				else:
					temp_array[idx] = temp_arr_0[arr_idx_0]
					arr_idx_0 += 1
			elif arr_idx_0 < half_size and arr_idx_1 >= half_size:
				temp_array[idx] = temp_arr_0[arr_idx_0]
				arr_idx_0 += 1
			elif arr_idx_0 >= half_size and arr_idx_1 < half_size:
				temp_array[idx] = temp_arr_1[arr_idx_1]
				arr_idx_1 += 1
			print(idx, temp_array)
		return temp_array

	def binary_search(self, temp_array, value):
		half_size = int(len(temp_array) / 2)
		half_num = temp_array[half_size]
		print(half_size, half_num, temp_array)
		if(half_num == value):
			return True
		elif(self.compare_x_y_greater(half_num, value) and (len(temp_array) > 1)):
			return self.binary_search(temp_array[half_size:], value)
		elif(self.compare_x_y_greater(value, half_num) and (len(temp_array) > 1)):
			return self.binary_search(temp_array[0:half_size], value)
		else:
			return False


	def main(self, sort_select):
		global sorting_algo_cnt

		if (sort_select == "all" or sort_select == -1):
			for idx in range(sorting_algo_cnt):
				self.sorting_en.append(1)
		else:
			for idx in range(sorting_algo_cnt):
				self.sorting_en.append(0)
			self.sorting_en[sort_select] = 1

		for idx in range(sorting_algo_cnt):
			if(self.sorting_en[idx] == 1):
				self.initial_status()

				if (idx == 0):
					print("Champion problem")
					temp_min, temp_min_idx = self.champion_problem(self.unsorted_array)
					print(temp_min)
				elif (idx == 1):
					print("Selection Sort")
					self.sorted_array = self.selection_sort(self.unsorted_array)
				elif (idx == 2):
					print("Insertion Sort")
					self.sorted_array = self.insertion_sort(self.unsorted_array)
				elif (idx == 3):
					print("Selection Sort + Merge Sort")
					self.merge_sort(self.unsorted_array)
				elif (idx == 4):
					print("Selection Sort + Binary Search")
					self.sorted_array = self.selection_sort(self.unsorted_array)
					search_value = random.randint(0, array_length)
					found_value = self.binary_search(self.sorted_array, search_value)
					print(search_value, found_value)
				else:
					print("Other Sorting Algorithm On-going")

				self.print_status(idx)

	def __init__(self, debug_level):
		global array_length

		self.compare_counter = 0
		self.swap_counter = 0
		self.debug_level = debug_level
		self.initial_array = []
		self.unsorted_array = []
		self.sorted_array = []
		self.sorting_en = []

		random.seed(time.time())
		while len(self.initial_array) != array_length :
			temp_int = random.randint(0,(array_length))
			if not (temp_int in self.initial_array):
				self.initial_array.append(temp_int);
		print(self.initial_array)
