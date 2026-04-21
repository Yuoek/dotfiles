%{
#include <calc.tab.h>
%}

%%
[0-9]+ { yylval = atoi(yytext); return NUMBER; }
"+"    { return ADD; }
"-"    { return SUB; }
"*"    { return MUL; }
"/"    { return DIV; }
"("    { return OP; }
")"    { return CP; }
\n     { return EOL; }
[ \t]  { }
.      { printf("unknow char: \c\n", *yytext); }
%%
