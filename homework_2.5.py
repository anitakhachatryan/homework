class Country:

  def __init__(self, name, continent):
    self.name = name
    self.continent = continent
  
  def country_presentation(self):
    country_text = "Country of production is {} which is in {}".format(self.name, self.continent)

    return country_text
  
class Brand:

  def __init__(self, brand_name, start_date):
    self.brand_name = brand_name
    self.start_date = start_date

  def brand_presentation(self):
    brand_text = "{} brand was founded in {}.".format(self.brand_name, self.start_date)

    return brand_text

class Season:
  def __init__(self, season_name, avg_temp):
    self.season_name = season_name
    self.avg_temp = avg_temp
  
  def season_presentation(self):
    season_text = "Average temperature for {} is {}.".format(self.season_name, self.avg_temp)
    
    return season_text

class Product(Country, Brand, Season):

  def __init__(self, product_name, type_, price, quantity, name, continent, brand_name, start_date, season_name, avg_temp):

    self.product_name = product_name
    self.type_ = type_
    self.price = price
    self.quantity = quantity
    Country.__init__(self, name, continent)
    Brand.__init__(self, brand_name, start_date)
    Season.__init__(self, season_name, avg_temp)

  def product_presentation(self):
      product_text = "This is {}. This product belongs to {} type of products. Price is {} AMD per pcs. Minimum order quantity is {} pcs.".format(self.product_name, self.type_, self.price, self.quantity)

      return product_text

  def discount(self, sale):
      self.sale = sale
      final_price = self.price*(1-self.sale/100)
      
      return "Final discounted price is {} AMD".format(final_price)

  def quantity_incr(self):
      new_quantity = self.quantity + 2

      return "Increased quantity for discounted price is {}".format(new_quantity)

product1 = Product("Jacket", "Men's clothes", 75000, 1, "France", "Europe", "'Lacoste'", 1933, "winter", 0)

print(product1.product_presentation())
print(product1.discount(10))
print(product1.brand_presentation())
print(product1.quantity_incr())
print(product1.season_presentation())
print(product1.country_presentation())
