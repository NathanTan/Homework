/* barberShop.c */
/* The Barber Shop concurrency problem */
/* Solution algorithm is taken from the Little Book of Semaphores */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>

typedef struct ThreadParams
{
   int placeholder;
} ThreadParams;

/* Function Headers */

/* Semaphores */

sem_t mutex;
sem_t customer;
sem_t barber;
sem_t customerDone;
sem_t barberDone;

int main(int argc, char** argv)
{
   int chairs = 0;
   int i = 0;

   /* Semaphore Initalization */
   /*if (sem_init(&mutex, 0, 1) == -1)
   {  printf("Error\n"); exit(1);  }
   
   if (sem_init(&customer, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }
   
   if (sem_init(&barber, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }
   
   if (sem_init(&customerDone, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }
   
   if (sem_init(&barberDone, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }
*/
   for (i = 0; i < argc; i += 2) {
      printf("i: %d\n", i);
      if (strcmp(argv[i], "-c") == 0) {


         chairs = atoi(argv[i + 1]);
      }
   }

   printf("%d chairs\n", chairs);



   return;
}
