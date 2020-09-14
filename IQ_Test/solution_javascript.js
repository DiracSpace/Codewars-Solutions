function iqTest(numbers) {
  var odd = [], even = [];
  const list = numbers.split(" ");
  var i;
  for (i = 0; i < list.length; i++) {
    if (list[i] % 2 == 0) {
      odd.push(i);
    } else {
      even.push(i);
    }
  }
  if (Math.min(odd.length, even.length) == odd.length) {
    return Number(odd[0] + 1);
  } else {
    return Number(even[0] + 1);
  }
}
