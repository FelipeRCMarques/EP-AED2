import java.util.Scanner;

public class Main {

	public static void main(String[] args) {		
		Scanner sc = new Scanner(System.in);
		System.out.print("Digite o caminho do arquivo a ser lido: ");
		String arquivo = sc.nextLine();
		
		//long start = System.currentTimeMillis();		
		GeradorGrafo.gerar_lista_de_adjacencia(arquivo);
		//long check1 = System.currentTimeMillis();
		
		System.out.println();
		System.out.print("Digite o caminho do arquivo de saída: ");		
		String saida = sc.nextLine();
		
		//long check2 = System.currentTimeMillis();
		GeradorGrafo.gerar_dados_do_histograma(saida);		
		long arestas = GeradorGrafo.numero_de_arestas();
		System.out.println("Número de arestas = " + arestas);	
		//long end = System.currentTimeMillis();
		
		
		sc.close();		
	}

}
