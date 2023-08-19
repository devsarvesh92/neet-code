# Parking System
# Parking Garage
# Parking Floor
# Driver
# Vechicle


import datetime
import decimal
import uuid


class NotEnoughMoney(Exception):
    ...


class Vechicle:
    """
    Vechicle
    """

    def __init__(self, wheels: int) -> None:
        self.wheels = wheels

    def get_parking_size(self) -> int:
        return self.wheels // 4


class Driver:
    "Driver"

    def __init__(
        self, vechicle: Vechicle, id: uuid.UUID, balance: decimal.Decimal
    ) -> None:
        self.vechicle = vechicle
        self.id = id
        self.balance = balance

    def charge(self, amount: decimal.Decimal) -> None:
        if amount <= self.balance:
            print(f"Paid parking amount{amount=}")
            self.balance -= amount
        else:
            raise NotEnoughMoney(
                "Not sufficient funds, please let me work here for your funds 😤"
            )


class ParkingFloor:
    """Parking floor"""

    def __init__(self, spots: int) -> None:
        self.spots = [0] * spots
        self.vechicle_map = {}

    def park(self, vechicle: Vechicle):
        l, r = 0, 0
        spot_size: int = vechicle.get_parking_size()

        while r < len(self.spots):
            if self.spots[r] != 0:
                l = r + 1
            if r - l + 1 == spot_size:
                for k in range(l, r + 1):
                    self.spots[k] = 1
                self.vechicle_map[vechicle] = [l, r]
                return True
            r += 1
        return False

    def remove(self, vechicle: Vechicle):
        if self.vechicle_map.get(vechicle) is not None:
            start, end = self.vechicle_map.get(vechicle)
            for spot in range(start, end + 1):
                self.spots[spot] = 0
                return True
        return False


class ParkingGarage:
    def __init__(self, floors: int, spots: int) -> None:
        self.parking_floors = [ParkingFloor(spots=spots) for i in range(floors)]

    def park(self, vechicle: Vechicle) -> bool:
        for id, floor in enumerate(self.parking_floors):
            if floor.park(vechicle=vechicle):
                print(f"Parked {vechicle.wheels} at floor={id}")
                return True
        return False

    def remove(self, vechicle: Vechicle) -> bool:
        for id, floor in enumerate(self.parking_floors):
            if floor.remove(vechicle=vechicle):
                print(f"Removed {vechicle.wheels} at floor={id}")
                return True
        return False


class ParkingSystem:
    def __init__(
        self, parking_garage: ParkingGarage, hourly_rate: decimal.Decimal
    ) -> None:
        self.parking_garage = parking_garage
        self.hourly_rate = hourly_rate
        self.timings = {}

    def park(
        self, driver: Driver, in_time: datetime.datetime = datetime.datetime.utcnow()
    ) -> bool:
        is_parked = self.parking_garage.park(driver.vechicle)
        if is_parked:
            self.timings[driver.id] = in_time
            print("Parked sucessfully")
            return True
        return False

    def remove(
        self, driver: Driver, out_time: datetime.datetime = datetime.datetime.utcnow()
    ) -> bool:
        removed = self.parking_garage.remove(driver.vechicle)
        if removed:
            in_time: datetime.datetime = self.timings[driver.id]
            parking_hours = (out_time - in_time).seconds / 3600
            parking_charge: decimal.Decimal = decimal.Decimal(
                str(parking_hours * 24 * self.hourly_rate)
            )
            driver.charge(parking_charge)
            return True
        return False


vechicle = Vechicle(4)
driver = Driver(vechicle=vechicle, id=uuid.uuid4(), balance=decimal.Decimal("10000.00"))

garage = ParkingGarage(floors=3, spots=10)
parking_system = ParkingSystem(parking_garage=garage, hourly_rate=10)

parking_system.park(driver=driver)
parking_system.remove(
    driver=driver, out_time=datetime.datetime.utcnow().replace(hour=23)
)
