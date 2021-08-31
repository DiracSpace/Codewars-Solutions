function makeNegative(num) {
    switch (Math.sign(num)) {
        case -1:
            return num;
        case 1:
            return -Math.abs(num);
        default:
            return 0;
    }
}