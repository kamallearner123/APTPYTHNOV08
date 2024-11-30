#include<stdio.h>
#include<stdlib.h>
int *swaparr(int *a, int len)
{
    int *out;
    out = malloc(len*sizeof(int));
    int i;
    for (i=0; i<len; i++)
    {
        out[a[i]] = i;        
    }

    
    for (i=0; i<len; i++)
        printf("%d ",out[i]);

    return out;
}

int main()
{
    int a[7] = {5,6,1,2,3,4,0};
    int *out = NULL;

    out = swaparr(a,7);
}
