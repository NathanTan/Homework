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
void *getHairCut();
void *cutHair();

/* Semaphores */
sem_t mutex;
sem_t customer;
sem_t barber;
sem_t customerDone;
sem_t barberDone;

/* Other Globals */
int customers;

int main(int argc, char** argv)
{
   int chairs = 0;
   int i = 0;

   /* Semaphore Initalization */
   if (sem_init(&mutex, 0, 1) == -1)
   {  printf("Error\n"); exit(1);  }

   if (sem_init(&customer, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }

   if (sem_init(&barber, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }

   if (sem_init(&customerDone, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }

   if (sem_init(&barberDone, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }

   // Deal with command line arguments.
   for (i = 1; i < argc; i += 2) {
      if (strcmp(argv[i], "-c") == 0) {
         chairs = atoi(argv[i + 1]);
      }
   }

   /* Create threads */
   pthread_t threads[chairs + 1];
   
   /* Barber */
   pthread

   for (i = 0; i < NUM_THREADS; i++) 
   {
      pthread_create(&threads[i], NULL, getHairCut, NULL);
   }

   return;
}

// Executed by the barber
void *cutHair() {
   int hairCutTime = 10;

   while(1) 
   {
      printf("BARBER: Waiting for customer\n");
      sem_wait(&customer);
      sem_post(&barber);
      printf("BARBER: Starting haircuit (%d seconds)\n", hairCutTime);

      sleep(hairCutTime);

      printf("BARBER: Hair cut done\n");

      sem_wait(&customerDone);
      sem_post(&barberDone);
   }
}

void *getHairCut() {
   while(1) {
      sem_wait(&mutex);
      if (customers == chairs) {
         sem_post(&mutex);
         balk()
      }

      customers++;
      sem_post(&mutex);

      sem_post(&customer);
      sem_wait(&barber);

      sleep(10); // Wait for hair to be cut

      sem_post(&customer);
      sem_wait(&barberDone);

      sem_wait(&mutex);
      customers--;
      sem_post(&mutex);
   }
}

