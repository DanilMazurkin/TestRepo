from good_list import GoodList


def run_program():
    """Здесь будет содержаться вся логика работы программы"""
    good_list = GoodList()
    good_list.load_goods_from_file('./list_goods.txt')
    good_list_from_file = good_list.get_good_list()

    mean_price = good_list.get_mean_price_goods(good_list_from_file)
    good_with_max_price = good_list.get_good_with_max_price(good_list_from_file)

    print(mean_price)
    print(good_with_max_price)


if __name__ == "__main__":
    run_program()
