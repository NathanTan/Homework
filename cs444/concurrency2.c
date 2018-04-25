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
void initalizePhilosophers();

char *names = {"Sherk", "COnfusious", "Nicehs", "The Scientist Formally Known As Rick", "Wall-E"};

sem_t forks[FORK_COUNT];
Philosopher philosophers[PHILOSOPHER_COUNT];

int main()
{
    // Initalize semaphores
    initalizeForks();

    /* Initalize the philosophers */
    initalizePhilosophers();

    // Seed the random value generator
    srand(4);

    while (1)
    {
        printf("salsa\n");
        sleep(2);
        printf("\033[2J"); // Clears the screen
        printf("banana\n");
        sleep(2);
        printf("\033[2J"); // Clears the screen
    }
    return 0;
}

void *Philose(Philosopher p)
{
    while (1)
    {
        int eat_time = rand();
        int think_time = rand();

        //Wait for the forks
        sem_wait(&forks[p.seat]); // Wait for the fork to their right.

        // Wait for the fork to their left.
        if (p.seat == 0)
            sem_wait(&forks[FORK_COUNT - 1]);
        else
            sem_wait(&forks[p.seat - 1]);

        //eat
        sleep(eat_time);

        //put the chopsticks back
        sem_post(&forks[p.seat]); // Wait for the fork to their right.

        // Wait for the fork to their left.
        if (p.seat == 0)
            sem_post(&forks[FORK_COUNT - 1]);
        else
            sem_post(&forks[p.seat - 1]);

        //think
        sleep(think_time);
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
}

void initalizePhilosophers()
{
    int i = 0;
    for (i = 0; i < PHILOSOPHER_COUNT; i++)
    {
        strcpy(philosophers[i].name, names[i]);
        philosophers[i].activity = WAITING;
        philosophers[i].seat = i;
    }
}
