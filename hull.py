from math import sqrt
import urllib.request

""" returns villages from a given file """
def return_villages(file) -> set:
    print("called: return_villages(file)")
    s = []
    with open(file, 'r') as f:
        for line in f:
            line = line.split(',')
            if(len(line) == 2):
                x = int(line[0])
                y = int(line[1].rstrip())
                tup1 = (x, y)
                s.append(tup1)
    return s

""" returns distance between two villages """
def distance_calculator(tup1, tup2) -> float:
    print("called: distance_calculator()")
    if(tup1 and tup2) is not None:
        print(tup1)
        print(tup2)
        xDiff = tup1[1] - tup2[1]
        yDiff = tup1[0] - tup2[0]
        c = sqrt((xDiff * xDiff) + (yDiff * yDiff))
        return c
    else:
        return None

def duration_calculator(distance, unitType) -> float:
    return 0

def show_world_settings(worldNum) -> bool:
    print("called: show_world_settings(worldNum)")
    url = ("http://www.twstats.com/en" + worldNum + "/index.php?page=settings")
    print(url)
    u2 = urllib.request.urlopen(url)
    for lines in u2.readlines():
            print(lines)


    return False

def convex_hull(points):
    """Computes the convex hull of a set of 2D points.

    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """

    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = sorted(set(points))

    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list.
    return lower[:-1] + upper[:-1]

# Example: convex hull of a 10-by-10 grid.
assert convex_hull([(i//10, i%10) for i in range(100)]) == [(0, 0), (9, 0), (9, 9), (0, 9)]

def main() -> bool:
    validWorld = False
    villageCoordsFile = "input.txt"
    world = 0
    world = str(input("World: "))
    show_world_settings(world)
    s = return_villages(villageCoordsFile)
    #print("Village List from File:")
    #print(s)
    print("Convex Hull List from Village List: ")
    hulls = convex_hull(s)
    #print(hulls)
    #print(distance_calculator(hulls[0], hulls[1]))

main()
