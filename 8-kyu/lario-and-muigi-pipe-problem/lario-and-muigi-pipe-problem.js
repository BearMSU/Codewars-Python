function pipeFix(numbers){
  const min = numbers[0]
  const max = numbers[numbers.length - 1];
  let fixedPipe = [];
  for (i = min; i <= max; i++) {
    fixedPipe.push(i);
  }
  return fixedPipe;
}