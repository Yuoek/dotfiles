# flex

<!-- mtoc-start -->

* [flex 函数与变量](#flex-函数与变量)
* [文件内容](#文件内容)
* [示例](#示例)

<!-- mtoc-end -->
## flex 函数与变量
- yylex()
- yytext
- yyleng
- yyin
- yyout

- %option noyywrap;
- %option yylineno;
- %option reentrant;

## 文件内容
count.l
```markdown
头文件部分
%%
规则部分
%%
子程序部分
```

## 示例
**示例1: 字符统计**
```markdown
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
```

**編译运行**
```bash
flex cout.l
gcc lex.yy.c -o count -lfl
./count
```

输入字符后按 Ctrl+d 结束

**示例2: 计算器**
```markdown

```
