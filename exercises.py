#Comments are text that will not be executed in your code. Rather comments are for other programmers to read.
# All of the exercises below are commented out. Write your Javascript code after each exercise.
#Variables and Data Types
#Print each variable and test your code in the terminal using the Python interpreter
#example
greeting = 'Hello Prepster'
print(greeting); #this should print 'Hello Prepster'

#1 Variables with a String value
#Declare variables named first_name, last_name, birth_place, hobby, role_model, famous_quote, fav_president, fav_food, fav_color, fav_song
first_name = 'Sid'
last_name = 'Dod'
birth_place = 'Murica'
hobby = 'Slacklines'
role_model = 'Musk the Snail'
famous_quote = 'Where there is a will there is a way'
fav_president = 'Trump'
fav_food = 'sushi'
fav_color = 'red'
fav_song = 'Yiyongjun Jinxinqu'

#Assign your own string values to each variable and print each variable.
print(first_name)
print(last_name)
print(birth_place)
print(hobby)
print(role_model)
print(famous_quote)
print(fav_president)
print(fav_food)
print(fav_color)
print(fav_song)

#2 String Concatenation
#Declare a variable named full_name and concatenate first_name and last_name. Print the full_name variable.
full_name = first_name + ' ' + last_name
print(full_name)

#Declare a variable named intro that creates the following sentence:
#'Hello, my name is x and I was born in y.' Where x is full_name and y is birth_place. Print the intro variable.
intro = 'Hello, my name is ' + full_name + ' and I was born in ' + birth_place
print(intro)

#Declare a variable named about_me that creates the following sentence:
#'My hobby is x, my favorite song is y, and I like to eat z.' Where x is hobby, y is fav_song and z is fav_food. Print the about_me variable.
about_me = 'My hobby is ' + hobby + ' my favorite song is ' + fav_song + 'and I like to eat ' + fav_food
print(about_me)

#3 Spacing with tabs and newlines
#Declare a variable named my_hero that the following sentence using a tab:
#'My hero is x and his famous quote is y.' Where x is role_model and y is famous_quote. Print the my_hero variable.
my_hero = 'My hero is ' + role_model + ' and his famous quote ' + famous_quote
print(my_hero)

#Declare a variable named my_favs that creates the following sentence and returns a new line after each numbered item.
#'This is what I like: 1. hobby 2. fav_color 3. fav_song
#Print the my_favs variable.
my_favs = 'This is what I like: 1. ' + hobby + '2. '+ fav_color + '3. ' + fav_song
print(my_favs)

#4 Variables with a Number value
#Declare variables named age,
age = 76
weight = 185
shoe_size = 11
fav_number = 5
yen_rate = 110
bitcoin_value = 500
todays_temperature = 85
hawaii_population = 1400000
countries_traveled = 1000
number_of_siblings = 0

#Assign your own number values to each variable and print each variable.

print(age)
print(weight)
print(shoe_size)
print(fav_number)
print(yen_rate)
print(bitcoin_value)
print(todays_temperature)
print(hawaii_population)
print(countries_traveled)
print(number_of_siblings)

#5 Number as Strings Concatenation
#Declare a variable named self_intro that creates the following sentence:
#'Aloha, my name is x and I am y years old and my shoe size is z.' Where x is full_name, y is age and z is shoe_size. Print the self_intro variable.
self_intro = 'Aloha, my name is ' + full_name + ' and I am ' + str(age) +' years old and my shoe size is ' + str(shoe_size) + '.'
print(self_intro)

#Declare a variable named market_update that creates the following sentence:
#"Today's bitcoin value is x and the yen exchange rate is y." Where x is bitcoin_value and y is yen_rate. Print the market_update variable.
market_update = 'Today\'s bitcoin value is ' + str(bitcoin_value) + ' and the yen exchange rate is ' + str(yen_rate) +'.'
print(market_update)

#Declare a variable named about_hawaii that creates the following sentence:
#"Did you know that Hawaii's population is x and the average temperatue is y?" Where x is hawaii_population and y is todays_temperature. Print the about_hawaii variable.
about_hawaii = 'Did you know that Hawaii\'s population is ' + str(hawaii_population) + ' and the average temperatue is' + str(todays_temperature) + '?'
print(about_hawaii)

#6 Variables with a List value
#Declare a variable named fab_five and assign it a list containing five of your all time favorite snacks. Print the fab_five variable.
fab_five = ['']
print(fab_five)

#Declare a variable named plate_lunch and assign it a list containing five of your favorite lunch items. Print the plate_lunch variable.
plate_lunch  = ['katsu', 'saba', 'pho', 'burger', 'pizza']
print(plate_lunch)

#Declare a variable named ice_cream and assign it a list containing three of your favorite ice cream flavors. Print the ice_cream variable.
ice_cream = ['vanilla', 'dulce de leche', 'rocky road']
print(ice_cream)

#Declare a variable named west_siiiiide and assign it a list containing states found on the west coast of the US. Print the west_siiiiide variable.
west_siiiiide = ['California', 'Oregon', 'Washington']
print(west_siiiiide)

#Declare a variable named mega_millions and assign it a list containing the Mega Millions Lottery results for May, 4, 2018
#https://www.lotteryusa.com/mega-millions/. Print the mega_millions variable
mega_millions = [4, 5, 10, 12, 18, 21]
print(mega_millions)

#Declare a variable named hamajang and assign it a list containing six different data types. Print the hamajang variable.
hamajang = ['string', 99, True, ['more_stuff'], { 'key': 'value'}, ('what', 'is', 'this')]
print(hamajang)

#Declare a variable named dynamic_duos and assign it a list containing 3 lists, with each list containing items that pairs well with each other. Print the dynamic_duos variable.
my_duos = [['nes', 'snes', 'sfc', 'ps1'], ['safeway', 'wholefoods', 'foodland', 'times'], ['cat', 'dog', 'goat']]
dynamic_duos = [['gin', 'tonic'], ['peanut butter', 'celery'], ['bacon', 'cheeseburger']]
print(dynamic_duos)

#Print the following:
#Gin
print(dynamic_duos[0][0])

#peanut butter
print(dynamic_duos[1][0])

#cheeseburger
print(dynamic_duos[2][1])


#7 Accessing values in List
vics_list = ['Hendricks gin', 'Fever Tree tonic', 'Costco pub mix', 'cool ranch doritos', 'oreos', 'Safeway fried chicken', 'Morning Glass coffee']

#Print the entire list.
print(vics_list)
#Print the length of the list.
print(len(vics_list))

#Print only the first element in the list.
print(vics_list[0])

#Print only the last element in the list.
print(vics_list[len(vics_list) - 1])

#Print 'Safeway fried chicken'
print(vics_list[5])

#Replace 'cool ranch doritos' with 'carrot cake' and print the list.
vics_list[4] = 'carrot cake'
print(vics_list)

#Print the last element in the list using -1
print(vics_list[len(vics_list) - 1])

#8 Variables with a Dictionary value
#Declare a variable named car and create the following key-value pairs:
# - key: brand string value: Tesla,
# - key: model string value: Model 3,
# - key: price number value: 35000,
# - key: color string value: red,
# - key: production boolean value: False,
# - key: features list value: moon roof, leather seats, iphone docker
car = {
    'brand': 'Tesla',
    'model': 'Model 3',
    'price': '35000',
    'color': 'red',
    'production': False,
    'features': ['moon roof', 'leader seats', 'iphone docker'],
}
#Print the car variable.
print(car)

#Declare a variable named footwear and create the following key-value pairs:
# - key: brand string value: Vivo Barefoot,
# - key: url string value: https://www.vivobarefoot.com/us,
# - key: gender string value: Mens,
# - key: type string value: Ababa Canvas,
# - key: price number value: 80,
# - key: color list value: tan, black stripes, gum
# - key: ordered boolean value: True
footwear = {
    'brand': 'Vivo Barefoot',
    'url': 'https://www.vivobarefoot.com/us',
    'gender': '35000',
    'the_type': 'red',
    'color': ['tan', 'black stripes', 'gum'],
    'ordered': True,
}
#Print the footwear variable.

print(footwear)

#Declare a variable named bank and create the following key-value pairs:
# - key: name  string value: First Hawaiian Bank,
# - key: employees number value: 2200,
# - key: headquarters string value: Honolulu,
# - key: revenue number value: 700000000,
# - key: nasdaq string value: FHB,
# - key: products list value: savings, loans, trust, wealth management,
# - key: executive dictionary value: name: Robert Harrison, title CEO, salary: 2000000

#Print the bank variable.
bank = {
    'name': 'First Hawaiian Bank',
    'employees': 2200,
    'headquarters': 'Honolulu',
    'revenue': 700000000,
    'nasdaq': 'FHB',
    'products': ['savings', 'loans', 'trust', 'wealth management'],
    'executive': {'name': 'Robert Harrison', 'title': 'CEO', 'salary': 2000000}
}
print(bank)

#Declare a variable pandas and assign it an EMPTY dictionary.
#You will add the following key-value pairs:
# - key: name string value: Panda Express
# - key: restaurants number value: 2000
# - key: cuisine string value: Gourmet Chinese Food
# - key: menu list value: Orange Chicken, Walnut Shrimp, Sweet and Sour pork
# - key: highest_revenue string value: Ala Moana Center Food Court

#Print the pandas variable.
pandas = {}
pandas['name'] = 'Panda Express'
pandas['restaurants'] = 2000
pandas['cuisine'] = 'Gourmet Chinese Food'
pandas['menu'] = ['Orange Chicken', 'Walnut Shrimp', 'Sweet and Sour Pork']
pandas['highest_revenue'] = 'Ala Moana Shopping Center Food Court'
print(pandas)

#Declare a variable named bucket_list and assign it to an EMPTY dictionary.
#You will add the following key-value pairs:
# - key: travel string value of your choice
# - key: learn string value of your choice
# - key: weight number value of your choice
# - key: to_dos list value of your choice
# - key: meet_person string value of your choice

#Print the bucket_list variable.
bucket_list = {}
bucket_list['travel'] = 'South Pacific'
bucket_list['learn'] = 'Programming'
bucket_list['weight'] = 168
bucket_list['to_dos'] = ['Hike the Inca Trail to Machu Picchu', 'Visit Angkor Wat','Cruise on a junk boat through Halong Bay']
bucket_list['meet_person'] = 'President Obama'
print(bucket_list)

#9 Variable with a Tuple value
#Declare a variable named bruce_bio and assign a tuple containing the following values: Bruce Lee, male, 32, San Francisco, [Kung-Fu Master, actor, philosopher]

#Print the bruce_bio variable.
bruce_bio = ('Bruce Lee', 'male', 32, 'San Fransico', ['Kung-Fu Master', 'actor', 'philosopher'] )
print(bruce_bio)


#Declare a variable named movies and assign a tuple containing the following values: [The Big Boss, 1971],[Fist of Fury, 1972], [The Way of the Dragon, 1972], [The Game of Death, 1972]

#Print the movies variable.
movies = (['The Big Boss', 1971],['Fist of Fury', 1972], ['The Way of the Dragon', 1972], ['The Game of Death', 1972])
print(movies)

#Declare a variable named updated_bio and add the bruce_bio and movies tuples together. Print the updated_bio variable.
updated_bio = bruce_bio + movies
print(updated_bio)


#Print the following values:
#The length of the updated_bio tuple
print(len(updated_bio))
#Bruce Lee
print(updated_bio[0])
#Index position 1
print(updated_bio[1])
#['Game of Death', 1972]
print(updated_bio[8])
#philosopher
print(updated_bio[4][2])
#1971
print(updated_bio[5][1])
#The Way of the Dragon
print(updated_bio[7][0])
#Fist of Fury
print(updated_bio[6][0])
#The last value using -1
print(updated_bio[-1])
#Game of Death using -1
print(updated_bio[-1][0])



#10 Variables with a Boolean value
#Declare the following variables and assign either a True or false value for each.
#, female, american, likes_coding, is_hungry, has_a_dog,

female = True
american = True
likes_coding = True
is_hungry = True
has_a_dog = False

#Print each variable that you declare.
print(female)
print(american)
print(likes_coding)
print(is_hungry)
print(has_a_dog)
