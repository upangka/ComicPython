

class AirplaneMixin:
    """飞机混入类"""
    def fly_in_the_air(self):
        print("飞...")

class ShipMixin:
    """船混入类"""
    def sail_on_the_sea(self):
        print("游...")

class FlyingBoat(AirplaneMixin, ShipMixin):
    pass

