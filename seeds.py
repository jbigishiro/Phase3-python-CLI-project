from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Supplier, Product
import random
from faker import Faker

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)

    suppliers_list = set()
    addresses_list = set()
    
    while len(suppliers_list) < 15:
        suppliers_list.add(fake.company())

    while len(addresses_list) < 15:
        addresses_list.add(fake.address().replace("\n", " "))

    products_list =[ "Smartphone", "Coffee Maker", "Fitness Tracker", "Bluetooth Speaker", "Travel Backpack", "Wireless Headphones", "Portable Charger", "Digital Camera", "Yoga Mat", "Gaming Console",
                      "Kitchen Knife Set", "Smart Watch", "Air Purifier", "Electric Toothbrush", "Robot Vacuum Cleaner", "Wireless Earbuds", "Outdoor Tent", "E-book Reader", "Blender", "Sneakers", "Desktop Computer",
                      "Camping Chair", "Hair Dryer", "Drone", "Cookware Set", "Action Camera", "LED TV", "Instant Pot", "Fitness Dumbbells", "Coffee Grinder" ,"ZephyrMist Fan", "Gardening Tools", "Roller Skates",
                      "Zenith Glow", "Bike Helmet", "Fountain Pen", "Solar Charger", "Fireworks", "Cooling Towel", "Alarm Clock", "Energy Drink","Makeup Palette", "Wind Chimes", "Hiking Boots", "Bike Pump", "Lunar Calendar",
                      "Earthquake Kit","Scooter", "Body Lotion", "Luxury Watch", "Adventure Backpack", "Jewelry Box", "Flashlight", "Moonlit Candle", "Flower Seeds", "Snorkel Set", "Blender"]
    
    with Session() as session:
        session.query(Supplier).delete()
        session.query(Product).delete()

        suppliers = []
        for supplier_name, address in zip(suppliers_list, addresses_list):
            supplier = Supplier(
                name=supplier_name,
                address=address,
            )
            suppliers.append(supplier)

        session.add_all(suppliers)
        session.commit()

        products = []
        i=0
        for supplier in suppliers:
            for _ in range(random.randint(1, 5)):
                product = Product(
                    name=products_list[i],
                    unit_price=round(random.uniform(100.00, 300.00), 2),
                    supplier_id=supplier.id  # Associate product with a valid supplier
                )
                products.append(product)
                i+=1
        session.bulk_save_objects(products)
        session.commit()