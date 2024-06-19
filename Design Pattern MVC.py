class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services, language="English"):
        if language == "Indonesia":
            print("Layanan yang Tersedia:")  # Pesan dalam bahasa Indonesia
        else:
            print("Services Provided:")  # Pesan default dalam bahasa Inggris
        for svc in services:
            print(svc,'')

    def list_pricing(self, services, language="English"):
        if language == "Indonesia":
            print("Tarif untuk Setiap Layanan:")  # Pesan dalam bahasa Indonesia
        else:
            print("Pricing for Services:")  # Pesan default dalam bahasa Inggris
        for svc in services:
            print("Untuk", Model.services[svc]['number'], svc, "anda membayar", Model.services[svc]['price'], "idr")
            # Pesan dalam bahasa Indonesia

class View2(object):
    def list_services(self, services):
        for svc in services:
            print (svc, '')

    def list_pricing(self, services):
        for svc in services:
            print ("Untuk", Model.services[svc]['number'], 
                    svc, "anda membayar idr", Model.services[svc]['price'])

class Controller(object):
    def __init__(self, language="English"):
        self.model = Model()
        if language == "Indonesia":
            self.view = View2()
        else:
            self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services, language="Indonesia" if isinstance(self.view, View2) else "English"))

    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services, language="Indonesia" if isinstance(self.view, View2) else "English"))

# Instansiasi objek
controller = Controller()
pilih_bahasa = input("Pilih bahasa: [1] English [2] Indonesia: ")
if pilih_bahasa == "2":
    controller = Controller("Indonesia")
elif pilih_bahasa == "1":
    controller = Controller("English")
else: 
    raise ValueError("Invalid language choice.")

print("Memproses...")
controller.get_services()
controller.get_pricing()
############################################################################
class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }
class View(object):
    def list_services(self, services):
        print("Services Provided:")
        for svc in services:
            print(svc,'')

    def list_pricing(self, services):
        print("Pricing for Services:")
        for svc in services:
            print("For", Model.services[svc]['number'],
                svc, "message you pay $", Model.services[svc]['price'])
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View

    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))

#Instansiasi objek
controller = Controller()
controller.get_services()
controller.get_pricing()

####################################################################
class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services):
        print("Services Provided:")
        for svc in services:
            print(svc,'')

    def list_pricing(self, services):
        print("Pricing for Services:")
        for svc in services:
            print("For", Model.services[svc]['number'],
                svc, "message you pay $", Model.services[svc]['price'])
            
class View2(object):
    def list_services(self, services):
        print("Layanan yang disediakan")
        for svc in services:
            print (svc, '')

    def list_pricing(self, services):
        print ('Tarif tiap layanan')
        for svc in services:
            print ("Untuk", Model.services[svc]['number'], 
                    svc, "anda membayar idr", Model.services[svc]['price'])

class Controller(object):
    def __init__(self, language="English"):
        self.model = Model()
        if language == "Indonesia":
            self.view = View2()
        else:
            self.view = View()
    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))
    
#Instansiasi objek
controller = Controller()
pilih_bahasa = input("What language do you choose: [1]English [2]Indonesia:")
if pilih_bahasa == "2":
    controller = Controller("Indonesia")
elif pilih_bahasa == "1":
    controller = Controller("English")
else: 
    raise ValueError ("Bahasa belum terdaftar")
controller.get_services()
controller.get_pricing()

class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }
class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc,'')
    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'],
            svc, "message you pay $",
            Model.services[svc]['price'])
 
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))
    def bid_price(self):
        tawar = input('What service do you want to bid? email, sms, voice: ')
        harga = input('Enter the price you want? ')
        if tawar in self.model.services:
            self.model.services[tawar]['price']=int(harga)
            print('price according to your bid:')
        else:
            print("x")

        self.get_pricing()
#Instansiasi objek
controller = Controller()
print("Services Provided:")
controller.get_services()
print("Pricing for Services:")
controller.get_pricing()
controller.bid_price()
