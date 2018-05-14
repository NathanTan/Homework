#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

typedef struct LightSwitch
{
   int counter;
   sem_t lock;
} LightSwitch;

sem_t resources;
sem_t output;
sem_t super;
LightSwitch lightSwitch;

void *process();
void *checkSem();

/* Function Definitions */
void unlock(LightSwitch *ls, sem_t *sem);
void lock(LightSwitch *ls, sem_t *sem);

int main(int argc, char **argv)
{
   int numberOfThreads = 5;

   srand(3);

   /* Initalize Semaphors */
   if (sem_init(&resources, 0, 3) == -1)
      printf("Error initalizing semaphore\n");
   lightSwitch.counter = 0;
   if (sem_init(&lightSwitch.lock, 0, 1) == -1)
      printf("Error initalizing semaphore\n");
   if (sem_init(&output, 0, 1) == -1)
      printf("Error initalizing semaphore\n");
   if (sem_init(&super, 0, 1) == -1)
      printf("Error initalizing semaphore\n");

   pthread_t processors[numberOfThreads + 1];

   int i;
   //pthread_create(&processors[0], NULL, checkSem, NULL);
   for (i = 1; i < numberOfThreads; i++)
   {
      pthread_create(&processors[i], NULL, process, NULL);
   }

   for (i = 1; i < numberOfThreads; i++)
   {
      pthread_join(processors[i], NULL);
   }
   while (1)
   {
      printf("In main\n");
      sleep(3);
   }
}

void unlock(LightSwitch *ls, sem_t *sem)
{
   printf("\t\tWaiting on ls\n");
   sem_wait(&ls->lock);
   ls->counter--;
   if (ls->counter == 0)
   {
      sem_post(sem);
   }
   sem_post(&ls->lock);
   printf("\t\tGiving up ls\n");
}

void lock(LightSwitch *ls, sem_t *sem)
{
   sem_wait(&ls->lock);
   ls->counter++;
   if (ls->counter == 1)
   {
      sem_wait(sem);
   }
   sem_post(&ls->lock);
   return;
}

void *checkSem()
{
   int *val = malloc(sizeof(int));
   int *superVal = malloc(sizeof(int));

   while (1)
   {
      printf("in checkSem\n");
      sleep(1);
      sem_getvalue(&resources, val);
      sem_getvalue(&(lightSwitch.lock), superVal);

      if (*val == 0)
      {
         printf("\t\t\tBlocking on all new processes trying to access the resourcess\n");
         lock(&lightSwitch, &resources);
      }

      if (*val == 3)
      {
         printf("\t\t\tThe block has been lifted\n");
         unlock(&lightSwitch, &resources);
      }
      printf("\tSemVal: %d\n", *val);
   }
}

void *process()
{
   while (1)
   {
      int waitTime = rand() % 15;
      int processTime = (rand() % 8) + 2;
      //printf("in process\n");
      lock(&lightSwitch, &super);
      sem_wait(&resources);
      sem_wait(&output);

      printf("Thread (%lu) is using a resource for %d seconds\n", pthread_self(), processTime);

      //sleep(waitTime);

      sleep(processTime);
      printf("Process %lu finished\n", pthread_self());
      sem_post(&output);
      sem_post(&resources);
      unlock(&lightSwitch, &super);

      sleep((rand() % 3) + 1);
   }
}
