
    public struct Pt
    {
        public double x;
        public double y;
    }

    class QuickHull
    {
        enum Side { Right = -1, LieOn = 0, Left = 1 };


        public QuickHull(List<Pt> coords)
        {
            if(coords == null || coords.Count() < 3)
            {
                throw new Exception("Convex hull do not exist");
            }

            inPts = coords;
        }

        private List<Pt> inPts;
        private List<Pt> hull;


        public void Execute()
        {
            hull = new List<Pt>();

            // Find the points with min and max x
            Pt min = new Pt() { x = double.MaxValue, y = double.MaxValue};
            Pt max = new Pt() { x = double.MinValue, y = double.MinValue};

            foreach (Pt p in inPts)
            {
                if (p.x > max.x)
                {
                    max.x = p.x;
                    max.y = p.y;
                }
                else if (p.x < min.x)
                {
                    min.x = p.x;
                    min.y = p.y;
                }
            }

            QuickHullRecursive(min, max, Side.Right);
            QuickHullRecursive(min, max, Side.Left);

            hull.Add(max);
        }


        public List<Pt> GetHull()
        {
            return hull;
        }



        void QuickHullRecursive(Pt Min, Pt Max, Side side)
        {
            double maxDist = 0.0;
            int idx = -1;

            foreach(var pt in inPts)
            {
                if(findSide(Min,Max,pt) == side)
                {
                    double d = lineDist(Min, Max, pt);
                    if(d > maxDist)
                    {
                        maxDist = d;
                        idx = inPts.IndexOf(pt);
                    }
                }
            }

            // if no point is found, add the two end points the the convex hull
            if(idx == -1)
            {
                hull.Add(Min);
                return;
            }

            // Recurse for the two parts divided by new point
            QuickHullRecursive(Min, inPts[idx], side);
            QuickHullRecursive(inPts[idx], Max, side);


        }











        // Returns the square of distance between p and q.
        double dist(Pt p, Pt q)
        {
            return (p.y - q.y) * (p.y - q.y) + (p.x - q.x) * (p.x - q.x);
        }

        // Returns a value proportional to the distance between the point p 
        // and the line joining the points p1 and p2
        double lineDist(Pt p1, Pt p2, Pt q)
        {


            return Math.Abs((q.y - p1.y) * (p2.x- p1.x) - (p2.y- p1.y) * (q.x - p1.x));
        }


        // Returns the side of point p with respect to line
        // joining points from p1 to p2.
        Side findSide(Pt p1, Pt p2, Pt p)
        {
            // Line of p1 and p2 is: (y2-y1)/(x2-x1) = (y-y1)/(x-x1)
            // y = (y2-y1)*(x-x1)/(x2-x1) + y1
            // 
            // For y=mx+c, 
            // if (y-mx-c) > 0, up
            // if (y-mx-c) < 0, down

            double val = (p.y - p1.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p.x - p1.x);

            if (val > 0)
                return Side.Right;
            else if (val < 0)
                return Side.Left;
            else
                return Side.LieOn;

        }
    }
