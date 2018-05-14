#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

#define NUM_THREADS 6
#define BUFFER_SIZE 32
#define DATA_MAX_SIZE 10

typedef struct Thread_Params
{
    int random_value;
    int buffer_pos;
    int consumer_sleep_time;
} Thread_Params;

typedef struct node
{
   int data;
   struct node * next;
} node;

typedef struct head
{
   node *next;
} head;


/* Global Linked List */
node * list;

/* Function Headers */
void *searcher();
void *inserter();
void *deleter();
void search(node *h, int data);
void insert(node *h, int data);
void delete(node *h, int data);
void append_node(node *h, int data);
void delete_node(node *h, int data);
void find_node(node *h, int data);

/* Semaphores */
sem_t noDeleter;
sem_t noSearcher;
sem_t noInserter;

sem_t searchSwitch;
sem_t insertSwitch;

/* Counters */
int searchSafety = 0;
int insertSafety = 0;

int main(int argc, char **argv)
{
   list = malloc(sizeof(head));


   char vendor[13];

   /* Semaphore Initalization */

   if (sem_init(&noDeleter, 0, 1) == -1)
      printf("Error\n");
   if (sem_init(&noSearcher, 0, 1) == -1)
      printf("Error\n");
   if (sem_init(&noInserter, 0, 1) == -1)
      printf("Error\n");
   if (sem_init(&searchSwitch, 0, 1) == -1)
      printf("Error\n");
   if (sem_init(&insertSwitch, 0, 1) == -1)
      printf("Error\n");

   /* Algorithm taken from the little book of semaphores */

   pthread_t threads[NUM_THREADS];
   int i;
   for (i = 0; i < NUM_THREADS; i += 3)
   {
      pthread_create(&threads[i], NULL, searcher, NULL);
      pthread_create(&threads[i + 1], NULL, inserter, NULL);
      pthread_create(&threads[i + 2], NULL, deleter, NULL);
   }

   for (i = 0; i < NUM_THREADS; i++)
   {
      pthread_join(threads[i], NULL);
   }

   return 0;
}


void *searcher() {
   int d; // Data
   while(1) {
      d = rand() % DATA_MAX_SIZE;
      search(list, d);
      sleep(rand() % 5);
   }
}

void *inserter() {
   int d; // Data
   while(1) {
      d = rand() % DATA_MAX_SIZE;
      insert(list, d);
      sleep(rand() % 5);
   }
}

void *deleter () {
   int d; // Data
   while(1) {
      d = rand() % DATA_MAX_SIZE;
      delete(list, d);
      sleep(rand() % 5);
   }
}

void search(node *h, int data) {

   // If error on trywait
   if (sem_trywait(&searchSwitch) < 0) {
      printf("Searcher: %lu is blocked\n", pthread_self());
      sem_wait(&searchSwitch);
   }

   searchSafety++;
   if (searchSafety == 1 && sem_trywait(&noSearcher) < 0) {
      printf("Searcher: %lu is blocked\n", pthread_self());
      sem_wait(&noSearcher);
   }

   sem_post(&searchSwitch);
   find_node(h, data);
   sem_wait(&searchSwitch);
   searchSafety--;
   if (searchSafety == 0) {
      sem_post(&noSearcher);
   }
   sem_post(&searchSwitch);
   return;
}

void insert(node *h, int data) {
   // If error on trywait
   if (sem_trywait(&insertSwitch) < 0) {
      printf("\tInserter:\t%lu is blocked\n", pthread_self());
      sem_wait(&insertSwitch);
   }

   insertSafety++;
   if (insertSafety == 1 && sem_trywait(&noInserter) < 0) {
      printf("\tInserter:\t%lu is blocked\n", pthread_self());
      sem_wait(&noInserter);
   }

   sem_post(&insertSwitch);
   append_node(h, data);
   sem_wait(&insertSwitch);
   insertSafety--;
   if (insertSafety == 0) {
      sem_post(&noInserter);
   }
   sem_post(&insertSwitch);
   return;

}

void delete(node *h, int data) {
   if (sem_trywait(&noSearcher) < 0) {
      printf("\t\tDeleter: %lu is blocked\n", pthread_self());
      sem_wait(&noSearcher);
   }
   if (sem_trywait(&noInserter) < 0) {
      printf("\t\tDeleter: %lu is blocked\n", pthread_self());
      sem_wait(&noInserter);
   }
   if (sem_trywait(&noDeleter) < 0) {
      printf("\t\tDeleter: %lu is blocked\n", pthread_self());
      sem_wait(&noDeleter);
   }

   delete_node(h, data);

   sem_post(&noSearcher);
   sem_post(&noInserter);
   sem_post(&noDeleter);

}

void find_node(node *h, int data) {
   int pos = -1;
   node *iter;

   if (h->next == NULL) {
      printf("Searcher [%lu]: List is empty\n", pthread_self());
   }

   else {
      iter = h->next;
      while (iter != NULL) {
         pos++;
         if (iter->data == data) {
            printf("Searcher [%lu]: Data '%d' located at [%d]\n", pthread_self(), data, pos);
         }
         iter = iter->next;
      }
   }

   printf("Searcher [%lu]: Data '%d' not found\n", pthread_self(), data);
}

void append_node(node *h, int data) {
   int pos = 0;
   
   // New node
   node *n = malloc(sizeof(node)); 
   n->data = data;
   n->next = NULL;

   node *iter;
   if (h->next == NULL) {
      h->next = n;
   }

   else {
      iter = h->next;
      while(iter->next != NULL) {
         iter = iter->next;
         pos++;
      }
      iter->next = n;
   }
   printf("\tInserter: %d was added to the list.\n", data);
}

/* Deletes the first node containing the matching data */
void delete_node(node *h, int data) {
   node *iter;
   node *temp = malloc(sizeof(node));

   if (h->next == NULL) {
      printf("Deleter: list is empty\n");
      return;
   }

   // If we are removing the first element
   else if (h->next->data == data) {

      // If there is only element in the list
      if (h->next->next == NULL) {
         free(h->next);
         h->next = NULL;
      }

      // If there is more than one element in the list
      else {
         temp = h->next->next;
         free(h->next);
         h->next = temp;
      }
   }

   else {
      iter = h->next;
      while (iter->next != NULL) {
         if (iter->next->data == data) {
            temp = iter->next;

            // If we are at the end of the list
            if (iter->next == NULL) {
               free(iter);
               break;
            }

            else {
               iter->next = temp->next;
               free(temp);
               break;
            }
         }
         iter = iter->next;
      }
   }
}
