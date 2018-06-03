/* smokingProblem.c */
/* The Smoker and Agent concurrency problem */
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
void balk();
void *administerA();
void *administerB();
void *administerC();
void *smoke();
void *pusherA();

/* Semaphores */
sem_t agentSem;
sem_t tobacco;
sem_t tobaccoSem;
sem_t paperSem;
sem_t matchSem;
sem_t paper;
sem_t match;

/* Other Globals */
int customers;
int chairs;

int main(int argc, char** argv)
{
   chairs = 0;
   int i = 0;

   /* Semaphore Initalization */
   if (sem_init(&agentSem, 0, 1) == -1)
   {  printf("Error\n"); exit(1);  }

   if (sem_init(&tabacco, 0, 1) == -1)
   {  printf("Error\n"); exit(1);  }

   if (sem_init(&paper, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }

   if (sem_init(&match, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }

   if (sem_init(&tobaccoSem, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }
   
   if (sem_init(&paperSem, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }
   
   if (sem_init(&matchSem, 0, 0) == -1)
   {  printf("Error\n"); exit(1);  }
   
   // Deal with command line arguments.
   for (i = 1; i < argc; i += 2) {
      if (strcmp(argv[i], "-c") == 0) {
         chairs = atoi(argv[i + 1]);
         if (chairs == 0) 
         {
            printf("\t\t\t----------------------------\n");
            printf("\t\t\t- WARNING: No chairs.\n");
            printf("\t\t\t- No customers will be able\n");
            printf("\t\t\t- to enter the shop\n");
            printf("\t\t\t----------------------------\n\n");
         }
      }
      
      if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
         printf("\tUsage: %s [-c] [Number of availible chairs]\n\n");
         exit(0);
      }
   }

   /* Seed random number generator */
   srand(14);

   /* Create threads */
   pthread_t threads[chairs + 1];

   /* Barber */
   pthread_create(&threads[0], NULL, cutHair, NULL);

   for (i = 1; i < chairs + 1; i++) 
   {
      //      printf("SYSTEM: creating customer\n");
      pthread_create(&threads[i], NULL, getHairCut, NULL);
   }


   for (i = 0; i < chairs + 1; i++) 
   {
      pthread_join(threads[i], NULL);
   }

   return 0;
}

void *administerA() {
   sem_wait(&agentSem);
   sem_post(&tabacco);
   sem_post(&paper);
}
void *administerB() {
   sem_wait(&agentSem);
   sem_post(&paper);
   sem_post(&match);
}
void *administerC() {
   sem_wait(&agentSem);
   sem_post(&tabacco);
   sem_post(&match);
}

void *smoke() {


}

void *pusher() {
   sem_wait(&tabacco);
   sem_wait(&mutex);
   if (isPaper) {
      isPaper = false;
      sem_post(&matchSem);
   }

   else if (isMatch) {
      isMatch = false;
      sem


// Executed by the barber
void *cutHair() {
   int hairCutTime = 5;

   while(1) 
   {
      printf("BARBER: Waiting for customer\n");
      sem_wait(&customer);
      sem_post(&barber);
      printf("BARBER: Starting haircuit (%d seconds)\n", hairCutTime);

      sleep(hairCutTime);

      printf("BARBER: Hair cut done\n");

      printf("BARBER: waiting on customer done mutex\n");
      sem_wait(&customerDone); 
      sem_post(&barberDone);
      printf("BARBER: BarberDone mutex is done\n");
   }
}

void *getHairCut() {
   int walkTime = 0; // Time before the custome comes into the store
   while(1) {
      sleep((rand() % 19) + 1);
      printf("CUSTOMER: Customer enter shop\n");
      sem_wait(&mutex);
      if (customers == chairs) {
         sem_post(&mutex);
         printf("CUSTOMER: balking\n");
         balk();
      }
      else if (customers == 0) {
         printf("CUSTOMER: Waking up the barber\n");
      }

      customers++;
      sem_post(&mutex);

      sem_post(&customer);
      printf("CUSTOMER: Waiting on a hair cut\n");
      sem_wait(&barber);
      printf("CUSTOMER: getting hair cut\n");
      sleep(5); // Wait for hair to be cut
      printf("CUSTOMER: Hair cut is done\n");
      sem_post(&customerDone);
      sem_wait(&barberDone);

      sem_wait(&mutex);
      customers--;
      sem_post(&mutex);

      printf("CUSTOMER: Customer left shop\n");
   }
}

void balk() { 
   int r;
   while(r)
   { r = 4; }
}
