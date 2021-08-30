public static string Longest(string s1, string s2) 
{
    var chars = s1.ToCharArray()
                .Concat(s2.ToCharArray())
                .ToHashSet()
                .OrderBy(c => c);
                
    return string.Join("", chars);
}