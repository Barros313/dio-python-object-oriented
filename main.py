import inheritance.animal as Animal
import inheritance.vehicle as Vehicle
import encapsulation.Account as Account
import encapsulation.Foo as Foo

def main():
    foo = Foo.Foo(10)

    print(foo.x())

    return None


if __name__ == "__main__":
    main()