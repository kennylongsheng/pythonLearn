import random
import time

array_length = 20
table_x = 4
table_y = 4
sorting_algo_cnt = 6
compare_counter = 0
swap_counter = 0
debug_level = 0

def compare_x_y_greater(x, y):
    global compare_counter
    compare_counter += 1
    if (x>y):
        return False
    else:
        return True

def swap_x_y(temp_array, x, y):
    global swap_counter
    swap_counter += 1
    if debug_level > 1:
        print("Before Swap:" + str(temp_array))
    temp_num = temp_array[x]
    temp_array[x] = temp_array[y]
    temp_array[y] = temp_num
    if debug_level > 1:
        print("After Swap:" + str(temp_array))
    return temp_array

def print_status(sort, sorted_array):
    global compare_counter, swap_counter
    if sort:
            print("Sorted_array: " + str(sorted_array))
    print("Compare_cnt: " + str(compare_counter) + "; Swap_cnt: " + str(swap_counter) + "\n")

def print_table(table, x, y):
    global table_y, table_x
    for idx_y in range(table_y):
        print("---", end="")
    print("\n")
    for idx_y in range(table_y):
        for idx_x in range(table_x):
            if ((x == idx_x) and (y == idx_y)):
                print("*" + str(table[idx_y][idx_x]), end=" ")
            else:
                print(" " + str(table[idx_y][idx_x]), end=" ")
        print("\n")
    for idx_y in range(table_y):
        print("---", end="")
    print("\n")

class sorting:
    def initial_status(self):
        global compare_counter, swap_counter, table_x, table_y
        compare_counter = 0
        swap_counter = 0
        self.unsorted_array = self.initial_array.copy()
        self.sorted_array.clear()
        for idx_y in range(table_y):
            for(idx_x) in range(table_x):
                self.young_table[idx_y][idx_x] = float('inf')
        if debug_level > 1:
            print(self.unsorted_array)
            print(self.young_table)

    def champion_problem(self, temp_array):
        temp_min = temp_array[0]
        temp_min_idx = 0

        for index in range(len(temp_array)):
            if (compare_x_y_greater(temp_min, temp_array[index]) == 0):
                temp_min = temp_array[index]
                temp_min_idx = index
        if debug_level > 1:
            print(temp_min)
        return (temp_min, temp_min_idx)

    def selection_sort(self, temp_array):
        head_idx = 0
        temp_min = temp_array[head_idx]

        while head_idx < (len(temp_array) - 1):
            temp_min, temp_min_idx = self.champion_problem(temp_array[head_idx:])
            swap_x_y(temp_array, head_idx, (temp_min_idx + head_idx))
            head_idx += 1
            if debug_level > 0:
                print(head_idx, temp_array)
        return temp_array

    def insertion_sort(self, temp_array):
        temp_min, temp_min_idx = self.champion_problem(temp_array)

        length_idx = 1
        while length_idx < (len(temp_array)):
            head_idx = length_idx
            while (head_idx > 0) and (compare_x_y_greater(temp_array[head_idx-1], temp_array[head_idx]) == 0):
                swap_x_y(temp_array, head_idx, (head_idx -1))
                head_idx -= 1
            length_idx += 1
            if debug_level > 0:
                print(length_idx, temp_array)
        return temp_array

    def merge_sort(self, temp_array, sort_sel):
        half_size = int(len(temp_array) / 2)
        temp_arr_0 = temp_array[0:half_size]
        temp_arr_1 = temp_array[(half_size):]
        arr_idx_0 = 0
        arr_idx_1 = 0

        if sort_sel == 0:
            temp_arr_0 = self.selection_sort(temp_arr_0)
            temp_arr_1 = self.selection_sort(temp_arr_1)
        elif sort_sel == 1:
            temp_arr_0 = self.insertion_sort(temp_arr_0)
            temp_arr_1 = self.insertion_sort(temp_arr_1)

        for idx in range(len(temp_array)):
            if arr_idx_0 < half_size and arr_idx_1 < half_size:
                if not (compare_x_y_greater(temp_arr_0[arr_idx_0], temp_arr_1[arr_idx_1])):
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
            if debug_level > 0:
                print(idx, temp_array)
        return temp_array

    def binary_search(self, temp_array, value):
        half_size = int(len(temp_array) / 2)
        half_num = temp_array[half_size]
        if debug_level > 1:
            print(half_size, half_num, temp_array)
        if(half_num == value):
            return True
        elif(compare_x_y_greater(half_num, value) and (len(temp_array) > 1)):
            return self.binary_search(temp_array[half_size:], value)
        elif(compare_x_y_greater(value, half_num) and (len(temp_array) > 1)):
            return self.binary_search(temp_array[0:half_size], value)
        else:
            return False

    def young_reorder_new(self, x, y):
        if debug_level > 1:
            print(x,y)
            print_table(self.young_table, -1, -1)
        if ((x == 0) and (y == 0)):
            return 0
        if (y == 0):
            if(self.young_table[y][x-1] > self.young_table[y][x]):
                temp_num = self.young_table[y][x]
                self.young_table[y][x] = self.young_table[y][x-1]
                self.young_table[y][x-1] = temp_num
                self.young_reorder_new(x-1, y)
            return 0
        if (x == 0):
            if(self.young_table[y-1][x] > self.young_table[y][x]):
                temp_num = self.young_table[y][x]
                self.young_table[y][x] = self.young_table[y-1][x]
                self.young_table[y-1][x] = temp_num
                self.young_reorder_new(x, y-1)
            return 0
        if(self.young_table[y][x-1] > self.young_table[y][x]):
            temp_num = self.young_table[y][x]
            self.young_table[y][x] = self.young_table[y][x-1]
            self.young_table[y][x-1] = temp_num
            self.young_reorder_new(x-1, y)
        if(self.young_table[y-1][x] > self.young_table[y][x]):
            temp_num = self.young_table[y][x]
            self.young_table[y][x] = self.young_table[y-1][x]
            self.young_table[y-1][x] = temp_num
            self.young_reorder_new(x, y-1)

    def young_insert(self, x, y, value):
        if not (self.young_table[y][x] == float('inf')):
            if debug_level > 1:
                print("Table FULL")
        else:
            if debug_level > 1:
                print("Table INSERT")
            self.young_table[y][x] = value
            self.young_reorder_new(x, y)

    def young_search(self, x, y, value):
        global table_x, table_y
        if debug_level > 0:
            print("Search: " + str(value) + " ; x_y:" + str(x) + "_" + str(y))
            print_table(self.young_table, x, y)
        if((x<0) or (x>=table_x) or (y<0) or (y>=table_y)):
            return False
        elif(value == self.young_table[y][x]):
            return True
        elif(value > self.young_table[y][x]):
            return self.young_search(x, y+1, value)
        elif(value < self.young_table[y][x]):
            return self.young_search(x-1, y, value)

    def main(self, sort_select):
        global sorting_algo_cnt, array_length, table_x, table_y

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
                    self.sorted_array = self.merge_sort(self.unsorted_array, 0)
                    print_status(idx, self.sorted_array)
                    self.initial_status()
                    print("Insertion Sort + Merge Sort")
                    self.sorted_array = self.merge_sort(self.unsorted_array, 1)
                elif (idx == 4):
                    print("Selection Sort + Binary Search")
                    self.sorted_array = self.selection_sort(self.unsorted_array)
                    search_value = random.randint(0, array_length)
                    found_value = self.binary_search(self.sorted_array, search_value)
                    print(search_value, found_value)
                elif (idx == 5):
                    print("Young Tableau Search")
                    for length_idx in range(len(self.unsorted_array)):
                        self.young_insert(table_x - 1 , table_y - 1 , self.unsorted_array[length_idx])
                    search_value = random.randint(0, array_length)
                    found_value = self.young_search(table_x - 1 , 0 , search_value)
                    print(search_value, found_value)
                else:
                    print("Other Sorting Algorithm On-going")

                print_status(idx, self.sorted_array)

    def __init__(self):
        global array_length, table_x, table_y

        self.initial_array = []
        self.unsorted_array = []
        self.sorted_array = []
        self.sorting_en = []
        self.young_table = [[(j) for j in range(table_y)] for i in range(table_x)]

        random.seed(time.time())
        while len(self.initial_array) != array_length :
            temp_int = random.randint(0,(array_length))
            if not (temp_int in self.initial_array):
                self.initial_array.append(temp_int);
        print(self.initial_array)
