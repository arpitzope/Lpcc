{
#include<stdio.h>
#include "y.tab.h"
%}
%token BUILTIN UD WS ID OPEN_SQ CLOSE_SQ EQ NEW SC COMMA DIGIT 
%%
start :  varlist WS varlist  {printf(" NOT Valid Declaration \n");} 
        |  varlist UD DIGIT  {printf("Valid Declaration \n");}
        |  varlist  {printf("Valid Declaration \n");}
        |  varlist UD varlist {printf("Valid Declaration \n");}
        | varlist : varlist COMMA ID | ID;
%%

int yywrap()
{ return 1;
}

int main()
{
	printf("\nEnter variable declaration  :  ");
	yyparse();
	return 1;
}

int yyerror(char *s)
{
	fprintf(stderr,"s\n",s);
	return 1;
}
