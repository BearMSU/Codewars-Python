function saleHotdogs(n){
​
  if (n < 5) {
    ppu = 100;  
  } else if (n >= 5 && n < 10) {
    ppu = 95;
  } else {
    ppu = 90
  }
  return n * ppu;
}