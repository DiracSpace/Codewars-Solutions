using System.Linq;
using System;

public static class Kata 
{
    public static int MaxSequence(int[] arr)
    {
        if (arr.Length == 0) return 0;

        var positives = arr.Where(number => number > 0).Count();
        if (arr.Length == positives)
            return arr.Sum();
        else
        {
            // kadanes algorithm
            int max_now = 0;
            int max_total = 0;

            foreach (var item in arr)
            {
                max_now += item;

                if (max_now < 0)
                    max_now = 0;

                if (max_total < max_now)
                    max_total = Math.Max(max_total, max_now);
                
            }

            return max_total;
        }
    }
}