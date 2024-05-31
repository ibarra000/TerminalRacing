from lib import *

def main():
    car1 = Vehicle("Civic", 0.5, 4000, 10, "-")
    car2 = Vehicle("Civic", 1, 3000, 10, "-")
    strip = Track(0.3, 1.225, 0.5, [car1,car2], 10)
    strip.start()

if __name__ == '__main__':
    main()
    