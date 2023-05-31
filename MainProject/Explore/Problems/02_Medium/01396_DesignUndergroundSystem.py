# Medium 1396. Design Underground System

class UndergroundSystem:
    def __init__(self):
        self.stations = {}  # stationId -> stationName
        self.checkins = {}  # cardId -> [stationId, t]
        self.stats = {}  # (stationId1, stationId2) -> [cnt, total_time, avg_time, avg_valid]

    def register_station(self, stationName):
        stationId = self.stations.get(stationName)
        if stationId is not None: return stationId
        stationId = len(self.stations)
        self.stations[stationName] = stationId
        return stationId

    def checkIn(self, id, stationName, t):
        stationId1 = self.register_station(stationName)
        check = self.checkins.get(id)
        if check: check[0], check[1] = stationId1, t
        else: self.checkins[id] = [stationId1, t]

    def checkOut(self, id, stationName, t):
        stationId2 = self.register_station(stationName)
        check = self.checkins[id]
        stationId1 = check[0]
        stat_key = (stationId1, stationId2)
        stat = self.stats.get(stat_key)
        if stat is None:
            stat = [0, 0, 0, True]
            self.stats[stat_key] = stat
        stat[0] += 1
        stat[1] += t - check[1]
        stat[3] = False

    def getAverageTime(self, startStation, endStation):
        stationId1 = self.register_station(startStation)
        stationId2 = self.register_station(endStation)
        stat = self.stats.get((stationId1, stationId2))
        if stat is None: return 0.0
        if stat[3]: return stat[2]
        stat[2], stat[3] = stat[1] / stat[0], True
        return stat[2]

class UndergroundSystem:
    def __init__(self):
        self.checkins = {}  # cardId -> [stationName, t]
        self.stats = {}  # (startStation, endStation) -> [cnt, total_time, avg_time]

    def checkIn(self, id, stationName, t):
        self.checkins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        check = self.checkins.pop(id)
        stat_key = (check[0], stationName)
        stat = self.stats.get(stat_key)
        if stat is None:
            stat = [0, 0, 0]
            self.stats[stat_key] = stat
        stat[0] += 1
        stat[1] += t - check[1]
        stat[2] = stat[1] / stat[0]

    def getAverageTime(self, startStation, endStation):
        stat = self.stats.get((startStation, endStation))
        return 0.0 if stat is None else stat[2]

obj = UndergroundSystem()
obj.checkIn(45,"Leyton",3)
obj.checkIn(32,"Paradise",8)
obj.checkIn(27,"Leyton",10)
obj.checkOut(45,"Waterloo",15)
obj.checkOut(27,"Waterloo",20)
obj.checkOut(32,"Cambridge",22)
print(obj.getAverageTime("Paradise","Cambridge"))
print(obj.getAverageTime("Leyton","Waterloo"))
obj.checkIn(10,"Leyton",24)
print(obj.getAverageTime("Leyton","Waterloo"))
obj.checkOut(10,"Waterloo",38)
print(obj.getAverageTime("Leyton","Waterloo"))