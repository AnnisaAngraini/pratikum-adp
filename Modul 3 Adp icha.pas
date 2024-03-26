program Perulangan;
uses crt;
var
  a, b, n, i: Integer;
  
begin
clrscr;
writeln ('Bilangan Kelipatan 4 yang Ouputnya "Dor"');
writeln ('========================================');
   a  :=1;
   b  :=8;
   n  :=80;
   
for i:=1 to n do
  begin
    if (a mod 4 = 0)  then
      write ('DOR' :5 )
    else if (a mod b=0) then
      write ('DOR':5)
    else
      write (a:5);

    if (a mod b= 0) then
      writeln();
    inc(a);
  end;
end.
