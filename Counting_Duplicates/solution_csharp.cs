using System;
using System.Linq;

public class Kata
{
  public static int DuplicateCount(string str)
  {
    return str.Select(x => x.ToString())
      .ToList()
      .GroupBy(x => x, StringComparer.InvariantCultureIgnoreCase)
      .Where(x => x.Count() > 1)
      .Count();
  }
}