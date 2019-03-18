using System;
using System.Collections.Generic;
using System.IO;
class Solution 
{
    
    static void Main(String[] args) 
    {
        /* Enter your code here. 
        Read input from STDIN. Print output to STDOUT. 
        Your class should be named Solution */
        
        int cases = int.Parse(Console.ReadLine());
        for(int c=1; c<=cases; c++)
        {
            int n_start = int.Parse(Console.ReadLine());
            int n_end = int.Parse(Console.ReadLine());
            
            List<Pt> prev = CalculatePtCoord(n_start);
            for (int n=n_start+1; n<=n_end; n++)
            {
                List<Pt> curr = CalculatePtCoord(n);

                List<Pt> mSum = CalculateMinkowskiSum(prev, curr);

                QuickHull qh = new QuickHull(mSum);
                qh.Execute();
                List<Pt> convexHull = qh.GetHull();

                PlotMinkowskiSum(prev, curr, convexHull);

                prev = convexHull;
            }
                                    
            Console.WriteLine(prev.Count());
        }
        
        
    }
    
    
    
    
    
    
    
    
    
    
    static List<Pt> CalculatePtCoord(int n)
    {
            List<Pt> pts = new List<Pt>();
            double theta;
            for (int k=1; k<=n; k++)
            {
                theta = (2 * k - 1) * Math.PI / n;
                pts.Add(new Pt()
                {
                    x = Math.Cos(theta),
                    y = Math.Sin(theta),
                });
            }
            return pts;
    }



    static List<Pt> CalculateMinkowskiSum(List<Pt> pts_nSmall, List<Pt> pts_nLarge)
    {
            List<Pt> mSum = new List<Pt>();

            // Special treatment for the first pt, skip the last point of pts_nSmall
            Pt h = pts_nLarge.First();
            for (int j = 0; j < pts_nSmall.Count()-1; j++)
            {
                Pt l = pts_nSmall[j];
                mSum.Add(new Pt()
                {
                    x = l.x + h.x,
                    y = l.y + h.y,
                });
            }


            for (int i=1; i<pts_nLarge.Count()-1; i++)
            {
                h = pts_nLarge[i];

                for(int j = 0; j<pts_nSmall.Count(); j++)
                {
                    Pt l = pts_nSmall[j];
                    mSum.Add(new Pt()
                    {
                        x = l.x + h.x,
                        y = l.y + h.y,
                    });
                }
            }


            // Special treatment for the last pt, skip the first point of pts_nSmall
            h = pts_nLarge.Last();
            for (int j = 1; j < pts_nSmall.Count(); j++)
            {
                Pt l = pts_nSmall[j];
                mSum.Add(new Pt()
                {
                    x = l.x + h.x,
                    y = l.y + h.y,
                });
            }

            return mSum;
        }
    
    
    
    
    
    
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

            // Start from minX to maxX of the right side of the bisection line
            hull.AddRange(QuickHullRecursive(max, min, Side.Left));

            // Start from minX to maxX of the left side of the bisection line
            hull.AddRange(QuickHullRecursive(min, max, Side.Left));
            // Equivalent to the following
            //var dummy = QuickHullRecursive(min, max, Side.Left);
            //dummy.Reverse();
            //hull.AddRange(dummy);

        }


        public List<Pt> GetHull()
        {
            return hull;
        }



        private List<Pt> QuickHullRecursive(Pt Min, Pt Max, Side side)
        {
            List<Pt> ch = new List<Pt>();

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
                ch.Add(Min);
                return ch;
            }

            // Recurse for the two parts divided by new point
            ch.AddRange(QuickHullRecursive(Min, inPts[idx], side));
            ch.AddRange(QuickHullRecursive(inPts[idx], Max, side));

            return ch;
        }











        // Returns the square of distance between p and q.
        double dist(Pt p, Pt q)
        {
            return (p.y - q.y) * (p.y - q.y) + (p.x - q.x) * (p.x - q.x);
        }

        // Returns a value proportional to the distance between the point p 
        // and the line joining the points from p1 to p2
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

    
    
    
    
    
    
}