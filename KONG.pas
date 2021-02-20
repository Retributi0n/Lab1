program qqq;
var x :LongWord = 10;
 m:longword;
Function LCM:LongWord;

Begin
  m:=trunc(exp(16*ln(2)));
  x:= (1664525*x+1013904223) mod m;
  LCM:= x;
End;


Begin
writeln(LCM)
End.
