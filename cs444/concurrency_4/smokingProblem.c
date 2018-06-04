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

typedef int bool;
#define false 0;
#define true 1;

/* Function Headers */
void *getHairCut();
void *cutHair();
void *administerA();
void *administerB();
void *administerC();
void *smoker_A();
void *smoker_B();
void *smoker_C();
void *pusherA();
void *pusherB();
void *pusherC();
void initalizeSemaphores();

/* Semaphores */
sem_t mutex;
sem_t agentSem;
sem_t tobaccoSem;
sem_t paperSem;
sem_t matchSem;
sem_t tobacco;
sem_t paper;
sem_t match;

/* Other Globals */
int customers;
int numOfSmokers;
bool isTobacco = false;
bool isPaper = false;
bool isMatch = false;
int numTobacco = 0;
int numPaper = 0;
int numMatch = 0;

int main(int argc, char **argv)
{
   int i = 0;
   numOfSmokers = 0;

   /* Semaphore Initalization */
   initalizeSemaphores();

   // Deal with command line arguments.
   if (argc == 0)
   {
      printf("\tUsage: %s [-s] [Sets of smokers]\n\n");
      exit(0);
   }

   for (i = 1; i < argc; i += 2)
   {
      if (strcmp(argv[i], "-s") == 0)
      {
         numOfSmokers = atoi(argv[i + 1]);
         if (numOfSmokers == 0)
         {
            printf("\t\t\tError: No smokers.\n");
            printf("\t\t\tExiting\n");
            exit(1);
         }
      }

      if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0)
      {
         printf("\tUsage: %s [-s] [Sets of smokers]\n\n");
         exit(0);
      }
   }

   /* Seed random number generator */
   srand(14);

   int threadCount = (numOfSmokers * 3) + 6;

   /* Create threads */
   pthread_t threads[threadCount];

   printf("thread count %d\n\n", threadCount);
   for (i = 6; i < numOfSmokers + 6; i++)
   {
      printf("Creating smoker set\n");
      pthread_create(&threads[i], NULL, smoker_A, NULL);
      pthread_create(&threads[i], NULL, smoker_B, NULL);
      pthread_create(&threads[i], NULL, smoker_C, NULL);
   }
   pthread_create(&threads[0], NULL, administerA, NULL);
   pthread_create(&threads[1], NULL, administerB, NULL);
   pthread_create(&threads[2], NULL, administerC, NULL);
   pthread_create(&threads[3], NULL, pusherA, NULL);
   pthread_create(&threads[4], NULL, pusherB, NULL);
   pthread_create(&threads[5], NULL, pusherC, NULL);

   for (i = 0; i < threadCount + 6; i++)
   {
      pthread_join(threads[i], NULL);
   }

   return 0;
}

void *administerA()
{
   while (1)
   {
#ifdef DEBUG
      printf("ADMIN_A: waiting on agent\n");
#endif
      sem_wait(&agentSem);
#ifdef DEBUG
      printf("ADMIN_A:\t\tPosting tobacco\n");
#endif
      sem_post(&tobacco);
#ifdef DEBUG
      printf("ADMIN_A:\t\tPosting paper\n");
#endif
      sem_post(&paper);
   }
}

void *administerB()
{
   while (1)
   {
#ifdef DEBUG
      printf("ADMIN_B: waiting on agent\n");
#endif
      sem_wait(&agentSem);
#ifdef DEBUG
      printf("ADMIN_B:\t\tPosting paper\n");
#endif
      sem_post(&paper);
#ifdef DEBUG
      printf("ADMIN_B:\t\tPosting match\n");
#endif
      sem_post(&match);
   }
}

void *administerC()
{
   while (1)
   {
#ifdef DEBUG
      printf("ADMIN_C: waiting on agent\n");
#endif
      sem_wait(&agentSem);
#ifdef DEBUG
      printf("ADMIN_C:\t\tPosting tobacco\n");
#endif
      sem_post(&tobacco);
#ifdef DEBUG
      printf("ADMIN_C:\t\tPosting match\n");
#endif
      sem_post(&match);
   }
}

/* Smoker with tobacco */
void *smoker_A()
{
   while (1)
   {
      printf("SMOKER_A: waiting on tobacco\n");
      sem_wait(&tobaccoSem);
      printf("SMOKER_A: Rolling a cig\n");
      sleep(3); //makeCigarette();
      sem_post(&agentSem);
      printf("SMOKER_A: Smoking the cig\n");
      sleep(10);
   }
}

/* Smoker with paper */
void *smoker_B()
{
   while (1)
   {
      printf("SMOKER_B: waiting on paper\n");
      sem_wait(&paperSem);
      printf("SMOKER_B: Rolling a cig\n");
      sleep(3); //makeCigarette();
      sem_post(&agentSem);
      printf("SMOKER_B: Smoking the cig\n");
      sleep(10);
   }
}

/* Smoker with matches */
void *smoker_C()
{
   while (1)
   {
      printf("SMOKER_C: waiting on tobacco\n");
      sem_wait(&matchSem);
      printf("SMOKER_C: Rolling a cig\n");
      sleep(3); //makeCigarette();
      sem_post(&agentSem);
      printf("SMOKER_C: Smoking the cig\n");
      sleep(10);
   }
}

void *pusherA()
{
   while (1)
   {
#ifdef DEBUG
      printf("PUSHER_A: Waiting on tobacco\n");
#endif
      sem_wait(&tobacco);
      sem_wait(&mutex);
      if (numPaper)
      {
         numPaper--;
         sem_post(&matchSem);
      }

      else if (numMatch)
      {
         numMatch--;
         sem_post(&paperSem);
      }

      else
      {
         numTobacco++;
      }
      sem_post(&mutex);
   }
}

void *pusherB()
{
   while (1)
   {
#ifdef DEBUG
      printf("PUSHER_B: Waiting on paper\n");
#endif
      sem_wait(&paper);
      #ifdef DEBUG
      printf("PUSHER_B: Waiting on MUTEX\n");
#endif
      sem_wait(&mutex);
      if (numTobacco)
      {
         numTobacco--;
         #ifdef DEBUG
      printf("PUSHER_B:\t\tPosting matchSem\n");
#endif
         sem_post(&matchSem);
      }

      else if (numMatch)
      {
         numMatch--;
         #ifdef DEBUG
      printf("PUSHER_B:\t\tPosting tobaccoSem\n");
#endif
         sem_post(&tobaccoSem);
      }

      else
      {
         numPaper++;
      }
      sem_post(&mutex);
   }
}

void *pusherC()
{
   while (1)
   {
#ifdef DEBUG
      printf("PUSHER_C: Waiting on match\n");
#endif
      sem_wait(&match);
      sem_wait(&mutex);
      if (numPaper)
      {
         numPaper--;
         sem_post(&tobaccoSem);
      }

      else if (numTobacco)
      {
         numTobacco--;
         sem_post(&paperSem);
      }

      else
      {
         numTobacco++;
      }
      sem_post(&mutex);
   }
}

void initalizeSemaphores()
{

   if (sem_init(&mutex, 0, 1) == -1)
   {
      printf("Error\n");
      exit(1);
   }

   if (sem_init(&agentSem, 0, 1) == -1)
   {
      printf("Error\n");
      exit(1);
   }

   if (sem_init(&tobacco, 0, 1) == -1)
   {
      printf("Error\n");
      exit(1);
   }

   if (sem_init(&paper, 0, 0) == -1)
   {
      printf("Error\n");
      exit(1);
   }

   if (sem_init(&match, 0, 0) == -1)
   {
      printf("Error\n");
      exit(1);
   }

   if (sem_init(&tobaccoSem, 0, 0) == -1)
   {
      printf("Error\n");
      exit(1);
   }

   if (sem_init(&paperSem, 0, 0) == -1)
   {
      printf("Error\n");
      exit(1);
   }

   if (sem_init(&matchSem, 0, 0) == -1)
   {
      printf("Error\n");
      exit(1);
   }
}