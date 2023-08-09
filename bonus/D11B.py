def get_nums():
    with open('../files/avg_num.txt', 'r') as file:
        data = file.readlines()
    nums = [float(num.strip('\n')) for num in data]
    return nums


def get_avg():
    nums = get_nums()
    total_nums = len(get_nums())
    total_sum = sum(nums)
    avg = total_sum/total_nums
    print(avg)


get_avg()


