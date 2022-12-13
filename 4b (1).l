%{
    #include"y.tab.h"
%}

%%

sqrt return sqrt_fun;
[0-9]+ {yylval = atoi(yytext); return num;}
[(] return OB;
[)] return CB;
pow return POW;
, return comma;
[\n] return NL;

%%
