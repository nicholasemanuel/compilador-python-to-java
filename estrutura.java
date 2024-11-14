public class estrutura {
    // Definição de variáveis de diferentes tipos de dados
    private int inteiro;
    private double decimal;
    private String texto;
    private boolean logico;

    // Construtor da classe
    public EstruturaDados(int inteiro, double decimal, String texto, boolean logico) {
        this.inteiro = inteiro;
        this.decimal = decimal;
        this.texto = texto;
        this.logico = logico;
    }

    // Método que realiza uma operação aritmética
    public int somar(int a, int b) {
        int resultado = a + b;
        return resultado;
    }

    // Método que verifica se um número é positivo
    public boolean ehPositivo(int numero) {
        return numero > 0;
    }

    // Método que concatena strings
    public String concatenarTexto(String outroTexto) {
        return this.texto + outroTexto;
    }

    // Método para exibir os valores armazenados
    public void exibirValores() {
        System.out.println("Inteiro: " + inteiro);
        System.out.println("Decimal: " + decimal);
        System.out.println("Texto: " + texto);
        System.out.println("Lógico: " + logico);
    }

    public static void main(String[] args) {
        // Instanciando a classe e chamando os métodos
        EstruturaDados exemplo = new EstruturaDados(10, 20.5, "Olá, mundo!", true);

        // Chamando métodos
        int soma = exemplo.somar(3, 7);
        boolean positivo = exemplo.ehPositivo(soma);
        String novaTexto = exemplo.concatenarTexto(" - Bem-vindo!");

        // Exibindo resultados
        exemplo.exibirValores();
        System.out.println("Soma: " + soma);
        System.out.println("É positivo? " + positivo);
        System.out.println("Texto concatenado: " + novaTexto);
    }
}
