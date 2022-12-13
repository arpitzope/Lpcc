%{
    #include<math.h>
    #include<stdio.h>
    #include<string.h>
    int yylval;
    void yyerror();
    int yylex();
%}

%token OB CB num sqrt_fun alpha POW comma NL;

%%
START: s NL START | s NL;
s: sqrt_fun OB num CB { $$ = sqrt($3);
printf("%d\n\n",$$);} |
POW OB num comma num CB {printf("%.2f\n\n",pow($3,$5));}

;


%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter expression\n");
    yyparse();
}

void yyerror()
{
    printf("Invalid\n");
}
