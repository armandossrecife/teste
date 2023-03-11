#include <stdio.h>
#include <stdlib.h>

#define LIN 3
#define COL 3

// Função para ler uma matriz a partir do console
void lerMatriz(float matriz[][COL], char nomeMatriz) {
    printf("Digite os elementos da matriz %c:\n", nomeMatriz);
    for (int i = 0; i < LIN; i++) {
        for (int j = 0; j < COL; j++) {
            printf("Elemento [%d][%d]: ", i+1, j+1);
            scanf("%f", &matriz[i][j]);
        }
    }
}

// Função para imprimir uma matriz
void imprimirMatriz(float matriz[][COL]) {
    for (int i = 0; i < LIN; i++) {
        for (int j = 0; j < COL; j++) {
            printf("%.2f\t", matriz[i][j]);
        }
        printf("\n");
    }
}

// Função para salvar uma matriz em um arquivo texto
void salvarMatriz(float matriz[][COL], char nomeArquivo[]) {
    FILE *arquivo = fopen(nomeArquivo, "w");
    if (arquivo == NULL){
      printf("Erro ao abrir o arquivo");
      exit(1);
    }
    for (int i = 0; i < LIN; i++) {
        for (int j = 0; j < COL; j++) {
            fprintf(arquivo, "%.2f\t", matriz[i][j]);
        }
        fprintf(arquivo, "\n");
    }
    fclose(arquivo);
}

int main() {
    float matrizA[LIN][COL];
    float matrizB[LIN][COL];
    float matrizSoma[LIN][COL];
    float matrizSubtracao[LIN][COL];
    float matrizProduto[LIN][COL];

    lerMatriz(matrizA, 'A');
    salvarMatriz(matrizA, "matriz_a.txt");

    lerMatriz(matrizB, 'B');
    salvarMatriz(matrizB, "matriz_b.txt");

    // Soma das matrizes A e B
    for (int i = 0; i < LIN; i++) {
        for (int j = 0; j < COL; j++) {
            matrizSoma[i][j] = matrizA[i][j] + matrizB[i][j];
        }
    }
    salvarMatriz(matrizSoma, "resultado_soma.txt");

    // Subtração das matrizes A e B
    for (int i = 0; i < LIN; i++) {
        for (int j = 0; j < COL; j++) {
            matrizSubtracao[i][j] = matrizA[i][j] - matrizB[i][j];
        }
    }
    salvarMatriz(matrizSubtracao, "resultado_subtracao.txt");

    // Produto das matrizes A e B
    for (int i = 0; i < LIN; i++) {
        for (int j = 0; j < COL; j++) {
            matrizProduto[i][j] = 0;
            for (int k = 0; k < COL; k++) {
                matrizProduto[i][j] += matrizA[i][k] * matrizB[k][j];
            }
        }
    }
    salvarMatriz(matrizProduto, "resultado_produto.txt");

    return 0;
}
