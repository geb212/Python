class IceCream:
  # Add a constructor here
  
  def __repr__(self):
    return "{} Ice Cream".format(self.flavor)
  
  def __init__(self,flavor):
    self.flavor = flavor

chocolate_ice_cream = IceCream("Chocolate")
strawberry_ice_cream = IceCream("Strawberry")
rum_raisin_ice_cream = IceCream("Rum Raisin")

print("I'm enjoying {}".format(chocolate_ice_cream))
