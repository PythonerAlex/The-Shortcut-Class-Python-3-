# import colorama
# from colorama import init
# init()
# from colorama import Fore, Back, Style
# import math


class Shortcuts:
    def __init__(self):
        pass


    def sort(list):
        for n in range(len(list) - 1, 0, -1):
            for no in range(n):
                if list[no] > list[no+1]:
                    temp = list[no]
                    list[no] = list[no+1]
                    list[no+1] = temp
        return list


    def max(list):
        max = list[0]
        for n in list:
            if n > max:
                max = n
        return max


    def min(list):
        min = list[0]
        for n in list:
            if n < min:
                min = n
        return min


    def even(list):
        even_list = []
        for n in list:
            if n % 2 == 0:
                even_list.append(n)
        return even_list


    def odd(list):
        odd_list = []
        for n in list:
            if n % 2 != 0:
                odd_list.append(n)
        return odd_list


    def add(list):
        result = 0
        for n in range(len(list)):
            result = result+list[n]
        return result


    def half(list):
        new_list = []
        for n in list:
            new_list.append(n / 2)
        return new_list


    def double(list):
        new_list = []
        for n in list:
            new_list.append(n * 2)
        return new_list


    def mean(list):
        total_value = Shortcuts.add(list)
        mean = total_value / len(list)
        return mean


    def median(list):
        new_list = Shortcuts.sort(list)
        length = len(new_list)
        index = int(length / 2)
        if int(index % 2) == 1:
            result = new_list[index]
        else:
            result = [new_list[index], new_list[index] - 1]
        return result


    def standard_deviation(list):
        mean = Shortcuts.mean(list)
        result = 0
        for n in list:
            semi_result = (n - mean) ** 2
            result = result + semi_result
        result = math.sqrt(result)
        return result


def main():
     numbers = [3, 2, 4, 5, 1]
     sc = Shortcuts
     result = sc.sort(numbers)
     print(result)


if __name__ == "__main__":
    # execute only if run as a script
    import math

    main()
# change
