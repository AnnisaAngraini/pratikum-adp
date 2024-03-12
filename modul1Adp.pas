Program Modul_1_Pengenalan_Pemograman;
Uses crt;
Var
    j, k, l, m, n: byte;
    a, b, c, d: real;
Begin
    clrscr;
    writeln ('Masukan Nilai-Nilai berikut');
    WriteLn ('===========================');
    write   ('Masukan nilai j :');
    readln  (j);
    write   ('Masukan nilai k :');
    readln  (k);
    write   ('Masukan nilai l :');
    readln  (l);
    write   ('Masukan nilai m :');
    readln  (m);
    write   ('Masukan nilai n :');
    readln  (n);
    writeln ();
    a:= (j*j*j) + (k*k) - l ;
    b:= j*k*l*m*n;
    c:= sqrt(j+k+l+m+n);
    d:= (j/k);
    writeln ('Hasil dari j^3 + k^2 - l adalah ',a:0:2);
    writeln ('Hasil dari (j * k * l * m * n) adalah ',b:0:2);
    writeln ('Hasil dari √(j + k + l + m + n) adalah ',c:0:2);
    writeln ('Hasil dari j:k adalah  ',d:0:2);
end.