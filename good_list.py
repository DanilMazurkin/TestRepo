from good import Good


class GoodList:
    """Represent GoodList"""

    def __init__(self):
        self.good_list = list()
        self.all_count = 0
    
    def get_good_list(self):
        """Возвращает good_list"""
        return self.good_list
    
    def load_goods_from_file(self, path_to_file):
        """Загружает товары из файлы в список GoodList."""
        with open(path_to_file, 'r', encoding='utf-8') as file:
            list_goods = file.readlines()

            for good_from_file in list_goods:
                price = int(good_from_file.split(":")[1])
                name = good_from_file.split(':')[0]
                count = int(good_from_file.split(':')[2])

                good_object = Good(
                    name=name,
                    price=price,
                    count=count,
                )

                self.all_count += count
                self.good_list.append(good_object)

    @staticmethod
    def get_mean_price_goods(goods_list):
        """Считает среднюю цену товаров."""
        sum_goods_price = 0
        count_goods = 0

        for good_object in goods_list:
            sum_goods_price += good_object.price
            count_goods += good_object.count

        mean = sum_goods_price / count_goods

        return mean

    @staticmethod
    def get_good_with_max_price(goods_list):
        """Возвращает товар с максимальной ценой."""

        max_price = 0
        find_good = None

        for good in goods_list:
            if good.price > max_price:
                max_price = good.price
                find_good = good

        return find_good

    @staticmethod
    def get_good_with_min_price(goods_list):
        """Возвращает товар с минимальной ценой."""
        min_price = 10000
        find_good = None

        for good in goods_list:
            if good.price < min_price:
                min_price = good.price
                find_good = good

        return find_good

    @staticmethod
    def get_good_with_max_count(goods_list):
        """Возвращает товар с максимальным количеством."""
        max_count = 0
        find_good = None

        for good in goods_list:
            if good.count > max_count:
                max_count = good.count
                find_good = good

        return find_good

    @staticmethod
    def get_good_with_min_count(goods_list):
        """Возвращает товар с минимальным количеством."""
        min_count = 1000
        find_good = None

        for good in goods_list:
            if good.count < min_count:
                min_count = good.count
                find_good = good

        return find_good

    def __eq__(self, other):
        return self.all_count == other.all_count
