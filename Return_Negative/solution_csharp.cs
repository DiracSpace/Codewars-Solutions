public static int MakeNegative(int number)
{
    switch (Math.Sign(number))
    {
        case -1:
            return number;
        case 0:
            return -Math.Abs(number);
        default:
            return 0;
    }
}

public static int MakeNegative(int number)
{
    return Math.Sign(number) switch
    {
        -1 => number,
        0 => -Math.Abs(number),
        _ => 0,
    };
}