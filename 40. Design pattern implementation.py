class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        raise NotImplementedError

class WeatherData(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = None
        self._humidity = None
        self._pressure = None

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def pressure(self):
        return self._pressure

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()

class CurrentConditionsDisplay(Observer):
    def __init__(self):
        self._temperature = None
        self._humidity = None

    def update(self, subject):
        if isinstance(subject, WeatherData):
            self._temperature = subject.temperature
            self._humidity = subject.humidity
            self.display()

    def display(self):
        print(f"Current conditions: {self._temperature}F degrees and {self._humidity}% humidity")

class StatisticsDisplay(Observer):
    def __init__(self):
        self._temperature = None

    def update(self, subject):
        if isinstance(subject, WeatherData):
            self._temperature = subject.temperature
            self.display()

    def display(self):
        print(f"Average/Max/Min temperature: {self._temperature}F")

class ForecastDisplay(Observer):
    def __init__(self):
        self._pressure = None

    def update(self, subject):
        if isinstance(subject, WeatherData):
            self._pressure = subject.pressure
            self.display()

    def display(self):
        print(f"Forecast pressure: {self._pressure}Pa")


weather_data = WeatherData()

current_display = CurrentConditionsDisplay()
statistics_display = StatisticsDisplay()
forecast_display = ForecastDisplay()

weather_data.attach(current_display)
weather_data.attach(statistics_display)
weather_data.attach(forecast_display)

weather_data.set_measurements(80, 65, 30.4)
weather_data.set_measurements(82, 70, 29.2)
weather_data.set_measurements(78, 90, 29.2)
