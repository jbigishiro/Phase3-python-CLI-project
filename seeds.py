
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Supplier, Product

if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    
    suppliers_list = ['Zenit Co', 'Prodigy Ltd', 'Titan Co', 'Nexus Co', 'Aqua Ltd', 'Lunar Ltd',
                 'Veritas Ltd', 'Crimson Ltd', 'Eclipse Ltd', 'Pinnacle Ltd','Opulent Ltd',
                 'TerraTech Ltd','Sapphire Ltd', 'Vivid Co', 'Cascade Co', 'Apex Global',
                 'Luminous Ltd', 'Aegis Co','Elysian Co', 'Stellar Ltd', 'Iris Ltd', 'Wakeup Ltd', 
                 'Myfake Ltd', 'Novel Ltd']
    
    addresses_list = [ "1234 Elm Street, Springfield, IL 12345", "5678 Maple Avenue, Oakville, CA 67890", "9101 Oak Lane, Portland, OR 90123", 
                      "2345 Pine Street, Charleston, SC 34567", "6789 Cedar Road, Denver, CO 56789", "123 Ivy Lane, Atlanta, GA 12345",
                     "456 Oak Street, Seattle, WA 45678", "789 Maple Avenue, Austin, TX 78901", "234 Elm Lane, Miami, FL 23456", "567 Pine Road, Chicago, IL 56789",
                     "890 Cedar Street, New York, NY 89012", "1234 Oak Avenue, Los Angeles, CA 12345", "5678 Maple Lane, San Francisco, CA 56789",
                     "910 Ivy Road, Boston, MA 91011", "2345 Pine Avenue, Dallas, TX 23456", "678 Cedar Lane, Houston, TX 67890",
                     "9012 Elm Street, Philadelphia, PA 90123", "3456 Oak Road, Phoenix, AZ 34567", "789 Maple Avenue, San Diego, CA 78901", 
                     "123 Pine Lane, Washington, DC 12345",  "456 Ivy Road, Miami, FL 45678", "789 Cedar Street, Denver, CO 78901", "234 Maple Avenue, Atlanta, GA 23456", 
                     "567 Oak Road, Seattle, WA 56789", "890 Pine Lane, Austin, TX 89012", "1234 Elm Street, Chicago, IL 12345", "5678 Maple Avenue, New York, NY 56789", 
                     "910 Pine Road, Los Angeles, CA 91011", "234 Cedar Lane, San Francisco, CA 23456","567 Ivy Street, Boston, MA 56789" ]



    products_list = [ "Smartphone", "Coffee Maker", "Fitness Tracker", "Bluetooth Speaker", "Travel Backpack",
                      "Wireless Headphones", "Portable Charger", "Digital Camera", "Yoga Mat", "Gaming Console",
                      "Kitchen Knife Set", "Smart Watch", "Air Purifier", "Electric Toothbrush", "Robot Vacuum Cleaner",
                      "Wireless Earbuds", "Outdoor Tent", "E-book Reader", "Blender", "Sneakers", "Desktop Computer",
                      "Camping Chair", "Hair Dryer", "Drone", "Cookware Set", "Action Camera", "LED TV", "Instant Pot",
                      "Fitness Dumbbells", "Coffee Grinder" ]
    
    
    with Session() as session:
        session.query(Supplier).delete()
        session.query(Product).delete()

        suppliers = []
        for i in range(20):
            supplier = Supplier(
                name=random.choice(suppliers_list),
                address=random.choice(addresses_list),
            )

            suppliers.append(supplier)

        session.add_all(suppliers)
        session.commit()

        products = []
        for supplier in suppliers:
            for i in range(random.randint(1, 5)):
                product = Product(
                    name=random.choice(products_list),
                    unit_price=random.uniform(100.00, 300.00),
                    supplier_id=supplier.id
                )

                products.append(product)

        session.bulk_save_objects(products)
        session.commit()