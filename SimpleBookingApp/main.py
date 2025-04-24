from functions import FlightManager

def main():
    flight_manager = FlightManager()

    while True:
        print("\n------Üdvözlöm a Simple Booking App-ban--------")
        print("1. Elérhető járatok megtekintése")
        print("2. Légitársaság járatainak megtekintése")
        print("3. Járat foglalása")
        print("4. Foglalás ellenőrzése")
        print("5. Foglalás törlése")
        print("6. Kilépés")

        try:
            choice = int(input("Válasszon egy opciót: "))
            if choice == 1:
                flight_manager.view_available_flights()
            elif choice == 2:
                flight_manager.view_filghts_by_company()
            elif choice == 3:
                flight_manager.book_flight()
            elif choice == 4:
                flight_manager.check_flight()
            elif choice == 5:
                flight_manager.cancel_flight()
            elif choice == 6:
                print("\nKöszönjük hogy a Simple Booking App-ot használta. Viszlát")
                break
            else:
                print("\nHbiás választás. Kérem válasszon egy helyes számot")

        except ValueError:
            print("\nÉrvénytelen szám. Kérem válasszon 1 és 5 között egy számot")

if __name__ == '__main__':
    main()


