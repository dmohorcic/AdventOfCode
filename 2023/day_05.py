class Interval:
    """
    Interval of type [start, end)
    """

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"<Interval [{self.start}, {self.end})>"
    
    def copy(self):
        return Interval(self.start, self.end)

    def get_intersection(self, other: "Interval"):
        """
        Get intersection with the other interval, split other if necessary

        Args:
            other (Interval): Other interval

        Returns:
            Interval: Interval that has an intersection with self
            List[Interval]: Intervals that do not have an intersection with self
        """

        intersection_interval = None
        other_intervals = list()

        # other is in self completely
        if (self.start <= other.start) and (other.end <= self.end):
            intersection_interval = other.copy()
        # self is in other completely
        elif (other.start <= self.start) and (self.end <= other.end):
            intersection_interval = self.copy()
            other_intervals = [Interval(other.start, self.start), Interval(self.end, other.end)]
        # left intersection
        elif (other.start < self.start) and (self.start < other.end) and (other.end < self.end):
            intersection_interval = Interval(self.start, other.end)
            other_intervals = [Interval(other.start, self.start)]
        # right intersection
        elif (self.start < other.start) and (other.start < self.end) and (self.end < other.end):
            intersection_interval = Interval(other.start, self.end)
            other_intervals = [Interval(self.end, other.end)]
        # no intersection
        else:
            other_intervals = [other]

        return intersection_interval, other_intervals


""" a = Interval(3, 7)
print("other is in self")
print(a.get_intersection(Interval(4, 5)))
print(a.get_intersection(Interval(3, 7)))
print("\nself is in other")
print(a.get_intersection(Interval(0, 10)))
print("\nleft intersection")
print(a.get_intersection(Interval(0, 5)))
print("\nright intersection")
print(a.get_intersection(Interval(5, 10)))
print("\noutside")
print(a.get_intersection(Interval(0, 3)))
print(a.get_intersection(Interval(7, 10)))
print() """


class ProjectionInterval:
    def __init__(self, source_start, destination_start, range_len):
        self.src_interval = Interval(source_start, source_start+range_len)
        self.dest_interval = Interval(destination_start, destination_start+range_len)
    
    def __repr__(self):
        return f"<ProjectionInterval {self.src_interval} -> {self.dest_interval}>"
    
    def project_intervals(self, intervals_to_project):
        projected_intervals = list()
        leftover_intervals = list()

        for interval in intervals_to_project:
            intersection, outside = self.src_interval.get_intersection(interval)
            if intersection is not None:
                # project intersection
                projected_intervals.append(Interval(
                    start=intersection.start-self.src_interval.start+self.dest_interval.start,
                    end=intersection.end-self.src_interval.start+self.dest_interval.start
                    ))
            leftover_intervals += outside

        return projected_intervals, leftover_intervals


class ProjectionMap:
    def __init__(self, projection_intervals, name):
        self.projection_intervals = projection_intervals
        self.name = name
    
    def __repr__(self):
        return f"<ProjectionMap {self.name}>"
    
    def project_interval(self, to_be_projected: list):
        already_projected = list()
        for projection in self.projection_intervals:
            projected, to_be_projected = projection.project_intervals(to_be_projected)
            already_projected += projected
        return already_projected + to_be_projected


def main():
    with open("2023/day_05.in", "r") as f:
        seeds = [Interval(int(x), int(x)+1) for x in f.readline()[6:].strip().split(" ")]
        f.readline(); f.readline()
        map_names = ["seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water",
                "water_to_light", "light_to_temperature", "temperature_to_humidity",
                "humidity_to_location"]
        maps = list()
        for map_name in map_names:
            line = f.readline().strip()
            projection_intervals = list()
            while line:
                dest_start, source_start, range_len = (int(x) for x in line.split(" "))
                projection_intervals.append(ProjectionInterval(source_start, dest_start, range_len))
                line = f.readline().strip()
            f.readline()
            projection_map = ProjectionMap(projection_intervals, map_name)
            maps.append(projection_map)
    
    # task 1
    min_location = float("inf")
    for seed in seeds:
        intervals = [seed]
        for map in maps:
            intervals = map.project_interval(intervals)
        min_location = min(min_location, min(i.start for i in intervals))
    print(min_location)

    # task 2
    seed_ranges = [Interval(x.start, x.start+y.start) for x, y in zip(seeds[::2], seeds[1::2])]
    min_location = float("inf")
    for seed in seed_ranges:
        intervals = [seed]
        for map in maps:
            intervals = map.project_interval(intervals)
        min_location = min(min_location, min(i.start for i in intervals))
    print(min_location)

if __name__ == "__main__":
    main()
