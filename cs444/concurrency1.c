#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{

	unsigned int eax;
	unsigned int ebx;
	unsigned int ecx;
	unsigned int edx;

	char vendor[13];
	
	eax = 0x01;

	__asm__ __volatile__(
	                     "cpuid;"
	                     : "=a"(eax), "=b"(ebx), "=c"(ecx), "=d"(edx)
	                     : "a"(eax)
	                     );
	
	if(ecx & 0x40000000){
        //use rdrand
        
        unsigned int rand = 0;
        unsigned char ok = 0;
        while((int)ok){
            __asm__ __volatile__ (
                "rdrand %0; setc %1" : "=r" (rand), "=qm" (ok)
            );
        }
        printf("%d\n", rand);
    }
	else{
        //use mt19937
  
        printf("Using mt19937\n");
        
	}

	return 0;
}