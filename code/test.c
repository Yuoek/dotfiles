
#include <stdio.h>

int main() {
    setvbuf(stdout, NULL, _IONBF, 0); // 关闭 stdout 缓冲
    int i;
    for (i = 0; i < 10; i++) {
        printf("%d\n", i);
    }
    return 0;
}
