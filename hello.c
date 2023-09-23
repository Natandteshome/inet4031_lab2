#include <stdio.h>

int main() {

    int a = 2;
    int b = 2;
    int c = a + b;

    char* users[] = {"User1", "User2", "User3"};
    int numOfUsers = sizeof(users) / sizeof(users[0]);

    printf("C says: Hello, World!\n");
    printf("%d + %d = %d\n", a, b, c);
    
    for(int i = 0; i < numOfUsers; i++) {
        printf("%s\n", users[i]);
    }

    return 0;
}
