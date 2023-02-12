#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *next;
} Node;

// função para inserir um número inteiro na lista
Node *insert(int num, Node *head)
{
    Node *temp = head;
    while (temp != NULL)
    {
        if (temp->data == num)
        {
            printf("Número %d já existe na lista\n", num);
            return NULL;
        }
        temp = temp->next;
    }

    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->data = num;
    new_node->next = head;
    head = new_node;
    return head;
}

// função para verificar se um número está na lista
void search(int num, Node *head)
{
    struct node *temp = head;
    while (temp != NULL)
    {
        if (temp->data == num)
        {
            printf("Número existe na lista\n");
            return;
        }
        temp = temp->next;
    }
    printf("Número não existe na lista\n");
}

// função para mostrar todos os elementos da lista
void printList(Node *head)
{
    Node *temp = head;
    printf("Lista: ");
    while (temp != NULL)
    {
        printf("[%d] ->", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

// função para ordenar a lista em ordem crescente
Node *sortAscending(Node *head)
{
    struct node *i, *j;
    int temp;
    for (i = head; i->next != NULL; i = i->next)
    {
        for (j = i->next; j != NULL; j = j->next)
        {
            if (i->data > j->data)
            {
                temp = i->data;
                i->data = j->data;
                j->data = temp;
            }
        }
    }
    return head;
}

// função para ordenar a lista em ordem decrescente
Node  *sortDescending(Node *head)
{
    struct node *i, *j;
    int temp;
    for (i = head; i->next != NULL; i = i->next)
    {
        for (j = i->next; j != NULL; j = j->next)
        {
            if (i->data < j->data)
            {
                temp = i->data;
                i->data = j->data;
                j->data = temp;
            }
        }
    }
    return head;
}

void menu()
{
    printf("1. Inserir elemento\n");
    printf("2. Buscar elemento\n");
    printf("3. Mostrar elementos\n");
    printf("4. Ordem crescente\n");
    printf("5. Ordem decrescente\n");
    printf("6. SAIR\n");
    printf("Qual a sua opção? ");
}

int main()
{
    printf("Teste Manipulando Listas numéricas\n");
    char opcao;
    int numero=0;

    Node *lista_original = NULL;
    Node *lista_aux = NULL;

    menu();
    opcao = getchar();
    while (opcao != '6')
    {
        switch (opcao)
        {
        case '1':
            /* code */
            printf("--- Insere elemento ---\n");
            printf("Qual o numero? ");
            scanf("%d", &numero);
            if (insert(numero, lista_original)){
                lista_original = insert(numero, lista_original);
            }            
            menu();
            break;
        case '2':
            /* code */
            printf("--- Busca elemento ---\n");
            printf("Qual o numero? ");
            scanf("%d", &numero);
            search(numero, lista_original);        
            menu();
            break;
        case '3':
            /* code */
            printf("--- Mostra elementos ---\n");
            if (lista_original != NULL){
                printList(lista_original);
            }else{
                printf("Lista vazia!\n");
            }
            menu();
            break;
        case '4':
            /* code */
            printf("--- Ordem crescente ---\n");
            lista_aux = lista_original;
            lista_aux = sortAscending(lista_aux);
            printList(lista_aux);
            menu();
            break;
        case '5':
            /* code */
            printf("--- Ordem decrescente ---\n");
            lista_aux = lista_original;
            lista_aux = sortDescending(lista_aux);
            printList(lista_aux);
            menu();
            break;
        }
        opcao = getchar();
    }

    return 0;
}
