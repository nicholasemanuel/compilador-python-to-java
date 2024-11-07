import java.util.ArrayList;
import java.util.Scanner;

class Tarefa {
    private String descricao;
    private boolean concluida;

    public Tarefa(String descricao) {
        this.descricao = descricao;
        this.concluida = false;
    }

    public void marcarConcluida() {
        this.concluida = true;
    }

    public String getDescricao() {
        return descricao;
    }

    public boolean isConcluida() {
        return concluida;
    }

    @Override
    public String toString() {
        return "Tarefa: " + descricao + " | Concluída: " + (concluida ? "Sim" : "Não");
    }
}

public class GerenciadorDeTarefas {
    private ArrayList<Tarefa> tarefas;
    private Scanner scanner;

    public GerenciadorDeTarefas() {
        tarefas = new ArrayList<>();
        scanner = new Scanner(System.in);
    }

    public void adicionarTarefa() {
        System.out.print("Digite a descrição da tarefa: ");
        String descricao = scanner.nextLine();
        tarefas.add(new Tarefa(descricao));
        System.out.println("Tarefa adicionada com sucesso!");
    }

    public void listarTarefas() {
        if (tarefas.isEmpty()) {
            System.out.println("Nenhuma tarefa encontrada.");
        } else {
            for (int i = 0; i < tarefas.size(); i++) {
                System.out.println((i + 1) + ". " + tarefas.get(i));
            }
        }
    }

    public void removerTarefa() {
        listarTarefas();
        System.out.print("Digite o número da tarefa a ser removida: ");
        int index = scanner.nextInt() - 1;
        scanner.nextLine(); // Limpa o buffer
        if (index >= 0 && index < tarefas.size()) {
            tarefas.remove(index);
            System.out.println("Tarefa removida com sucesso!");
        } else {
            System.out.println("Número de tarefa inválido.");
        }
    }

    public void marcarTarefaConcluida() {
        listarTarefas();
        System.out.print("Digite o número da tarefa a ser marcada como concluída: ");
        int index = scanner.nextInt() - 1;
        scanner.nextLine(); // Limpa o buffer
        if (index >= 0 && index < tarefas.size()) {
            tarefas.get(index).marcarConcluida();
            System.out.println("Tarefa marcada como concluída!");
        } else {
            System.out.println("Número de tarefa inválido.");
        }
    }

    public void menu() {
        while (true) {
            System.out.println("\n--- Gerenciador de Tarefas ---");
            System.out.println("1. Adicionar Tarefa");
            System.out.println("2. Listar Tarefas");
            System.out.println("3. Remover Tarefa");
            System.out.println("4. Marcar Tarefa como Concluída");
            System.out.println("5. Sair");
            System.out.print("Escolha uma opção: ");
            int opcao = scanner.nextInt();
            scanner.nextLine(); // Limpa o buffer

            switch (opcao) {
                case 1:
                    adicionarTarefa();
                    break;
                case 2:
                    listarTarefas();
                    break;
                case 3:
                    removerTarefa();
                    break;
                case 4:
                    marcarTarefaConcluida();
                    break;
                case 5:
                    System.out.println("Saindo do gerenciador de tarefas...");
                    return;
                default:
                    System.out.println("Opção inválida.");
            }
        }
    }

    public static void main(String[] args) {
        GerenciadorDeTarefas gerenciador = new GerenciadorDeTarefas();
        gerenciador.menu();
    }
}
