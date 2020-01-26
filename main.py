def read_file():
   try:
       filename = "breakfast_menu.txt"
       file = open(filename, "r")
       text = file.read().strip()
       file.close()
   except:
       print("Check the name of the file.")
       exit(1)
   return text
  

def remove_unnecessary(text):
   rem = text
   rem = rem.replace('<?xml version="1.0" encoding="UTF-8"?>', "")
   rem = rem.replace("<food>", "")
   rem = rem.replace("<breakfast_menu>", "")
   rem = rem.replace("</food>", "")
   rem = rem.replace("<name>", "=name=")
   rem = rem.replace("</name>", "")
   rem = rem.replace("<price>", "=price=")
   rem = rem.replace("</price>", "")
   rem = rem.replace("<description>", "=description=")
   rem = rem.replace("</description>", "")
   rem = rem.replace("<calories>", "=calories=")
   rem = rem.replace("</calories>", "")
   rem = rem.replace("</breakfast_menu>", "")
   rem = rem.replace("$", "")
   rem = rem.replace("\n","")
   rem = rem.replace("\n\n\n", "\n")
   rem = rem.split("=")
   return rem
      
      
def build_names(rem):
   names = []
   for line in range(2, len(rem), 8):
       names.append(rem[line])
   return names


def build_prices(rem):
   prices = []
   for line in range(4,len(rem), 8):
       prices.append(float(rem[line]))
   return prices


def build_description(rem):
   description = []
   for line in range(6,len(rem), 8):
       description.append(rem[line])
   return description
  
  
def build_calories(rem):
   calories = []
   for line in range(8,len(rem), 8):
       calories.append(float(rem[line]))
   return calories
  
  
def calc_price_average(prices):
   try:
       total = 0
       for element in prices:
           total += element
       price_average = total / len(prices)
   except:
       print("File is empty.")
       exit(1)
   return price_average
  
  
def calc_calories_average(calories):
   total = 0
   for element in calories:
       total += element
   calories_average = total / len(calories)
   return calories_average
  
def display_menu(names, description, calories, prices, price_average, calories_average, rem):
   print("%-32s %-88s %-20s %-10s" % ("Names", "Description", "Calories", "Prices"))
   try:
       for index in range(0, len(rem)):
           print("%-32s %-88s %-20s %-10s" % (names[index], description[index], calories[index], prices[index]))
   except:
       pass
       print("%-1s %-119s %-1s %-14s %-4s %-1s" % (len(names),"Items", calories_average, "Calories Avg", round(price_average, 3), "Price Avg")) 
  
def main():
   text = read_file()
   rem = remove_unnecessary(text)
   names = build_names(rem)
   prices = build_prices(rem)
   description = build_description(rem)
   calories = build_calories(rem)
   price_average = calc_price_average(prices)
   calories_average = calc_calories_average(calories)
   display_menu(names, description, calories, prices, price_average, calories_average, rem)
  
main()