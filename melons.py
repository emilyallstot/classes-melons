"""This file should have our melon-type classes in it."""

class Melon(object):
    def get_base_price(self):
        return 5.0

class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty < 3:
            total = self.get_base_price() * qty
        else:
            total = 0.75 * self.get_base_price() * qty

        return total

class CantaloupeOrder(Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty < 5:
            total = self.get_base_price() * qty
        else:
            total = 0.5 * self.get_base_price() * qty

        return total

class CasabaOrder(Melon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
     
        total = (self.get_base_price() + 1) * 1.5 * qty
        
        return total

class SharlynOrder(Melon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
     
        total = self.get_base_price() * 1.5 * qty
        
        return total

class SantaClausOrder(Melon):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
     
        total = self.get_base_price() * 1.5 * qty
        
        return total

class ChristmasOrder(Melon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
     
        total = self.get_base_price() * qty
        
        return total

class HornedMelonOrder(Melon):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
     
        total = self.get_base_price() * 1.5 * qty
        
        return total

class XiguaOrder(Melon):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
     
        total = self.get_base_price() * 1.5 * 2 * qty
        
        return total

class OgenOrder(Melon):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
     
        total = (self.get_base_price() + 1) * qty
        
        return total