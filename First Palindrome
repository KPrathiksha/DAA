#include <stdio.h>
#include <string.h>

int main() {
    char words[][10] = {"abc", "car","ada", "racecar","cool"};
    int n = 5;  

    for (int i = 0; i < n; i++) {
        int len = strlen(words[i]);
        int j, is_palindrome = 1;

        for (j = 0; j < len / 2; j++) {
            if (words[i][j] != words[i][len - j - 1]) {
                is_palindrome = 0;
                break;
            }
        }

        if (is_palindrome) {
            printf("%s\n", words[i]);
            return 0;
        }
    }

    printf("No palindromic string found\n");
    return 0;
}
