%{
#include <stdio.h>

int chars = 0;
int words = 0;
int lines = 0;
%}

%% 
[a-zA-Z]+ { words++; chars += strlen(yytext); }
\n        { chars++; lines++;}
.         { chars++; }
%%

int main(){
  yylex();
  printf("Chars: %d, Words: %d, Lines: %d\n", chars, words, lines);
  return 0;
}
