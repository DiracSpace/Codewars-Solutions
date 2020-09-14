// not completed on Codewars
// original solution but its inefficient
function color(a) {
  if(a[0] == a[1]) { return a[0] };
  if((a == 'BG' || a == 'GB')) { return 'R' };
  if((a == 'RG' || a == 'GR')) { return 'B' } else { return 'G' };
}

function triangle(row) {
  let res = '';
  for (let i = 1; i < row.length; i++) {
    res += color(row[i - 1] + row[i]);
  }
  return (row.length == 1) ? row : triangle(res);
}
