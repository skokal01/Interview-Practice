class Point(object):
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b
def maxPoints(points):
      """
      :type points: List[Point]
      :rtype: int
      """
      if len(points) < 2:
          return len(points)

      result = 0
      import pdb
      pdb.set_trace()
      for i in xrange(len(points)):
          slope = {'inf':0}
          same = 0
          slope_max = 0
          for j in xrange(i+1,len(points)):
              if points[i].x == points[j].x and points[i].y == points[j].y:
                  same += 1
                  continue
              # Same x-cordinate so slope becomes ifninity
              if points[i].x == points[j].x:
                  slope['inf'] += 1
              else:
                  k = 1.0*(points[i].y - points[j].y) / (points[i].x - points[j].x)
                  if k in slope:
                      slope[k] += 1
                  else:
                      slope[k] = 1
          result = max(result, max(slope.values())+same+1)

      return result

if __name__ == "__main__":
#     print maxPoints([Point(0,0)])
#     print maxPoints([Point(0,0),Point(0,0)])
     print maxPoints([Point(0,0),Point(94911151,94911150),Point(94911152,94911151)])
