# # define your methods here.
# # ex1() - ex10()
# from Calculator import Calculator
# from Fighter import Fighter
# from Dwarf import Dwarf
# from Invoice import Invoice

# def sort_people(people_list, field, direction='asc'):
#     reverse_order = False if direction == 'asc' else True
#     people_list.sort(key=lambda x: x[field], reverse=reverse_order)

# def ex1():
#     people_list = [
#         {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
#         {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
#         {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
#     ]
#     sort_people(people_list, 'age', 'desc')
#     print(people_list) 

# def ex2():
#     people_list = [
#         {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
#         {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
#         {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
#     ]
#     new_list = list(filter(lambda p: p['sex'] == 'male', people_list))
#     print(new_list)

# def ex3():
#     def calc_bmi(people_list):
#         def calculate_bmi(person):
#             weight_kg = person['weight_kg']
#             height_meters = person['height_meters']
#             return (weight_kg / height_meters ** 2)

#         bmis = list(map(calculate_bmi, people_list))
#         return bmis

# # Example usage
#     people_list = [
#         {'id': 2, 'name': 'bob', 'weight_kg': 90, 'height_meters': 1.7},
#         {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
#     ]

#     bmi_results = calc_bmi(people_list)
#     print(bmi_results)

# def ex4():
#     people_list = [
#         {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
#         {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
#         {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
#     ]
#     new_list = list(filter(lambda p: p['age'] > 15, people_list))
#     print(new_list)

# def ex5():
#     class WordCounter:
#         def __init__(self, sentence):
#             self.sentence = sentence
#             self.word_count = None
#             self.shortest_word = None
#             self.longest_word = None

#         def count_words(self):
#             words = self.sentence.split()
#             self.word_count = len(words)
#             self.shortest_word = min(words, key=len)
#             self.longest_word = max(words, key=len)

#         def get_word_count(self):
#             return self.word_count

#         def get_shortest_word(self):
#             return len(self.shortest_word)

#         def get_longest_word(self):
#             return len(self.longest_word)

# # Example usage
#     sentence = "This is a test of the emergency broadcast system"
#     word_counter = WordCounter(sentence)
#     word_counter.count_words()
#     print(word_counter.get_word_count())    # Returns the number of all the words.
#     print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
#     print(word_counter.get_longest_word())

# def ex6():
#     class TaxMan:
#         def __init__(self, items, tax_rate):
#             self.items = items
#             self.tax_rate = float(tax_rate.strip('%')) / 100  # Convert tax rate to a decimal
#             self.total_with_tax = None

#         def calc_total(self):
#             total = sum(item["price"] for item in self.items)
#             tax_amount = total * self.tax_rate
#             self.total_with_tax = total + tax_amount

#         def get_total(self):
#             if self.total_with_tax is not None:
#                 return round(self.total_with_tax, 2)
#             else:
#                 raise ValueError("Total not calculated. Call calc_total() first.")

 
#     items = [
#     {"id": 1, "desc": "clock", "price": 1.00},
#     {"id": 2, "desc": "socks", "price": 2.00},
#     {"id": 3, "desc": "razor", "price": 3.00},
#     ]
#     tm = TaxMan(items, "10%")
#     tm.calc_total()
#     print(tm.get_total())
    
    

# def ex7():
#     calculator1 = Calculator(4, 3)
#     calculator1.add()
#     print(calculator1.getResult())

#     calculator2 = Calculator(4, 3)
#     calculator2.sub()
#     print(calculator2.getResult())

#     calculator3 = Calculator(2, 3)
#     calculator3.mul()
#     print(calculator3.getResult())

#     calculator4 = Calculator(8, 2)
#     calculator4.div()
#     print(calculator4.getResult())
        

# def ex8():
#     class CarCollector:
#         car_list = [
#             {"id":1, "price":10000},
#             {"id": 2, "price": 20000},
#             {"id":3, "price": 30000}

#         ]

#         car_dict = {
#              1: "Ford",
#              2: "Mazda",
#              3: "Chevy"
#         }

#         @staticmethod
#         def get_data():
#             return list(map(CarCollector._combine, CarCollector.car_list))
        
#         @staticmethod
#         def _combine(c):
#             #Todo...
#             return {
#                 'id': c['id'],
#                 'make': CarCollector.car_dict[c['id']],
#                 'price': c['price']
#             }


# def ex9():
#     f = Fighter(18)
#     d = Dwarf(15)
#     print(f)
#     print(d)
#     f.fight(d)
#     d.fight(f)
#     print(f)
#     print(d)


# def ex10():
#     from pprint import pprint

#     data = [
#         "1, 2322, 10.00, False",
#         "2, 5435, 60.30, True",
#         "3, 3433, 15.63, False",
#         "4, 8439, 12.77, False",
#         "5, 3424, 11.34, False",
#     ]

#     invoices = []
#     for item in data:
#         invoice_data = item.split(', ')
#         invoice = Invoice(*invoice_data)
#         invoices.append(invoice)

#     pprint(invoices)


