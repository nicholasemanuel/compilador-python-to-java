import java.util.Arrays;

class MergeSortParalelo implements Runnable {
    private int[] array;
    private int inicio, fim;

    public MergeSortParalelo(int[] array, int inicio, int fim) {
        this.array = array;
        this.inicio = inicio;
        this.fim = fim;
    }

    @Override
    public void run() {
        mergeSort(array, inicio, fim);
    }

    private void mergeSort(int[] array, int inicio, int fim) {
        if (inicio < fim) {
            int meio = (inicio + fim) / 2;

            Thread esquerda = new Thread(new MergeSortParalelo(array, inicio, meio));
            Thread direita = new Thread(new MergeSortParalelo(array, meio + 1, fim));

            esquerda.start();
            direita.start();

            try {
                esquerda.join();
                direita.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            merge(array, inicio, meio, fim);
        }
    }

    private void merge(int[] array, int inicio, int meio, int fim) {
        int n1 = meio - inicio + 1;
        int n2 = fim - meio;

        int[] esquerda = new int[n1];
        int[] direita = new int[n2];

        System.arraycopy(array, inicio, esquerda, 0, n1);
        System.arraycopy(array, meio + 1, direita, 0, n2);

        int i = 0, j = 0, k = inicio;
        while (i < n1 && j < n2) {
            if (esquerda[i] <= direita[j]) {
                array[k++] = esquerda[i++];
            } else {
                array[k++] = direita[j++];
            }
        }

        while (i < n1) {
            array[k++] = esquerda[i++];
        }

        while (j < n2) {
            array[k++] = direita[j++];
        }
    }

    public static void main(String[] args) {
        int[] array = {38, 27, 43, 3, 9, 82, 10};
        System.out.println("Array original: " + Arrays.toString(array));

        Thread principal = new Thread(new MergeSortParalelo(array, 0, array.length - 1));
        principal.start();
        try {
            principal.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Array ordenado: " + Arrays.toString(array));
    }
}
