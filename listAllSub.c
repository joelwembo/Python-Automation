#include <stdio.h>
#include <dirent.h>
  
int main(void)
{
    struct dirent *direntry;  // Pointer for directory entry
    // opendir() returns a pointer of DIR type. 
    DIR *dr = opendir(".");
    if (dr == NULL)  // opendir returns NULL if couldn't open directory
    {
        printf("Could not open current directory" );
        return 0;
    }
    // for readdir()
    while ((direntry = readdir(dr)) != NULL)
            printf("%s\n", direntry->d_name);
    closedir(dr);    
    return 0;
}
