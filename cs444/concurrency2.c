#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

// These should be the same value
#define FORK_COUNT 5
#define PHILOSOPHER_COUNT 5

typedef enum phil_state {
    EATING,
    THINKING,
    WAITING
} phil_state;

typedef struct Philosopher
{
    char *name;
    phil_state activity;
    int chopsticks[2];
    int seat;
} Philosopher;

/* Fuction Headers */
void initalizeForks();
void *Philose(void *ph);
void initalizePhilosophers(pthread_t *threads);

//const char* const names[] = {"Sherk", "COnfusious", "Nicehs", "The Scientist Formally Known As Rick", "Wall-E"};

sem_t forks[FORK_COUNT];
Philosopher philosophers[PHILOSOPHER_COUNT];

void printState()
{
    int i = 0;
    for (i = 0; i < PHILOSOPHER_COUNT; i++)
    {
        printf("%s:\n   %d\n   Chopsticks: (%d, %d)\n   Seat: %d\n\n", philosophers[i].name, philosophers[i].activity, philosophers[i].chopsticks[0], philosophers[i].chopsticks[1], philosophers[i].seat);
    }
    return;
}

int main()
{
    int i;
    pthread_t threads[PHILOSOPHER_COUNT];

    // Initalize semaphores
    initalizeForks();

    /* Initalize the philosophers */
    initalizePhilosophers(threads);

    // Seed the random value generator
    srand(4);

    for (i = 0; i < PHILOSOPHER_COUNT; i++)
    {
        printf(":p %d\n", i);
        pthread_create(&threads[i], NULL, Philose, (void *)(philosophers + i));
    }

    for (i = 0; i < PHILOSOPHER_COUNT; i++)
    {
        printf(":p %d\n", i);
        pthread_join(threads[i], NULL);
    }

    while (1)
    {
        printf("here\n");
        printState();
        sleep(1);
        printf("\033[2J"); // Clears the screen
    }
    return 0;
}

void *Philose(void *ph)
{
    Philosopher *p = (Philosopher *)(ph);
    int leftFork = p->seat;
    int rightFork = (p->seat + 1) % 5;

    while (1)
    {
        printf("PHILOSOPHER: %s\n", p->name);
        int eat_time = (rand() % 7) + 2;
        int think_time = (rand() % 19) + 1;

        //think
        printf("%s is thinking for %d seconds\n", p->name, think_time);
        sleep(think_time);

        //Wait for the forks
        sem_wait(&forks[leftFork]);  // Wait for the fork to their left.
        sem_wait(&forks[rightFork]); // Wait for the fork to their right.

        //eat
        printf("PHILOSOPHER: %s is going to spend %d seconds EATING\n", p->name, eat_time);
        sleep(eat_time);

        // Set the forks down.
        sem_post(&forks[leftFork]);  // Set the left fork down.
        sem_post(&forks[rightFork]); // Set the right fork down.
    }
}

/* A function for inializing the fork semaphores */
void initalizeForks()
{
    int i = 0;
    for (i = 0; i < 5; i++)
    {
        if (sem_init(&forks[i], 0, i) == -1)
            printf("Error\n");
    }
    printf("Forks initalized\n");
}

void initalizePhilosophers(pthread_t *threads)
{
    int i = 0;
    //    for (i = 0; i < PHILOSOPHER_COUNT; i++)
    //    {
    philosophers[i].name = "1";
    philosophers[i].activity = WAITING;
    philosophers[i].seat = i;
    i++;
    philosophers[i].name = "p2";
    philosophers[i].activity = WAITING;
    philosophers[i].seat = i;
    //    }
    i++;
    philosophers[i].name = "p3";
    philosophers[i].activity = WAITING;
    philosophers[i].seat = i;
    //    }
    i++;
    philosophers[i].name = "p4";
    philosophers[i].activity = WAITING;
    philosophers[i].seat = i;
    //    }
    i++;
    philosophers[i].name = "p5";
    philosophers[i].activity = WAITING;
    philosophers[i].seat = i;
    //    }
    //

    printf("Threads mergered\n");

    return;
}
