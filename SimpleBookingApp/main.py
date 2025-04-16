from functions import FlightManager

def main():
    flight_manager = FlightManager()

    while True:
        print("\nÜdvözlöm a Simple Booking App-ban")
        print("1. Mutasd az elérhető járatokat")
        print("2. Járat foglalása")
        print("3. Járat ellenőrzése")
        print("4. Járat törlése")
        print("5. Kilépés")

        try:
            choice = int(input("Adja meg mit szeretne: "))
            if choice == 1:
                flight_manager.view_available_flights()
            elif choice == 2:
                flight_manager.book_flight()
            elif choice == 3:
                flight_manager.check_flight()
            elif choice == 4:
                flight_manager.cancel_flight()
            elif choice == 5:
                print("\nKöszönjük hogy a Simple Booking App-ot használta. Viszlát")
                break
            else:
                print("\nHbiás választás. Kérem válasszon egy helyes számot")

        except ValueError:
            print("\nHibás szám. Kérem válasszon 1 és 5 között egy számot")

if __name__ == '__main__':
    main()


