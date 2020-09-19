function createPhoneNumber(numbers){
  return (numbers == '') ? '' : numbers.join('').replace(/(...)(...)(.*)/, '($1) $2-$3');
}
