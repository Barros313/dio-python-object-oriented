import inheritance.animal as Animal
import inheritance.vehicle as Vehicle

def main():
    truck = Vehicle.Truck(False, color="Black", plate="ABC-1234", wheel_number=4)

    print(truck)

    return None


if __name__ == "__main__":
    main()