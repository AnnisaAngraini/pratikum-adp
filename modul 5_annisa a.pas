program modul_5;
uses crt;
var
  nilai_x: array[-10..10] of integer;
  y: array[-10..10] of real;
  x: integer;
begin
  clrscr;
  writeln ('Program menentukan nilai f(x) dengan array');
  writeln ('Tentukan nilai f(x) untuk x=[-10,10] dengan syarat:' );
  writeln ('* f(x)= x^2 + 2x,  jika x>0');
  writeln ('* f(x)= 1/x,       jika x<0');
  writeln ('* f(x)= 10,        jika x=0');
  writeln ('Jawab');
  for x := -10 to 10 do
    nilai_x[x] := x;

  for x := -10 to 10 do
  begin
    if x > 0 then
      y[x] := x * x + 2 * x
    else if x < 0 then
      y[x] := 1 / x
    else
      y[x] := 10;
  end;
  writeln('----------------------');
  writeln('|   x   |     f(x)   |');
  writeln('|-------|------------|');
  for x := -10 to 10 do
    writeln('| ', nilai_x[x]:4, '  | ', y[x]:8:3, '   |');
  writeln('----------------------');
end.