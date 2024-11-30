#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char *fun(char *str)
{
    char *ovels = "aeiouAEIOU";
    char *out;
    int i,j,index=0;
    out = malloc(strlen(str));
    for (i = 0; i<strlen(str); i++)
    {
        for (j=0;j<strlen(ovels); j++)
        {
            if (str[i] == ovels[j])
            {
                break;
            }
        }
        if (j<strlen(ovels))
            continue;

        out[index] = str[i]; 
        index++;
    }
    out[index]=0;
    return out;
}

int main()
{
    char *str="KAmal";
    printf("%s",fun(str));
}
