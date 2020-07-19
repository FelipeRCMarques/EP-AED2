import java.io.*;
import java.util.*;


//===================================================================================================================================================================================//
public class buscaEmProfundidade {

    private static LinkedList<LinkedList<Integer>> ListaAdj() throws IOException {

        String URL = "cenario1.txt"; 

        File grafoCenario1 = new File(URL);
        Scanner scanner = new Scanner(grafoCenario1);
                
        LinkedList<LinkedList<Integer>> listaAdj = new LinkedList<LinkedList<Integer>>();
        
        for(int i = 0; i < 86319; i++){
			
		listaAdj.add(new LinkedList<Integer>());	
		
		} 
                
        scanner.nextLine();
        scanner.nextLine();
    
        while(scanner.hasNext()){
    
            String verticeG = scanner.nextLine(); 
            String [] arestaG= verticeG.split(" ");
            
            int adicionaAresta = Integer.parseInt(arestaG[1]); 
            
            listaAdj.get(adicionaAresta).add(Integer.parseInt(arestaG[0])); 
        }
		
        scanner.close();

        return listaAdj;  
    }   


//===================================================================================================================================================================================//


	private static void BuscaProfundidade(LinkedList<LinkedList<Integer>> Grafo, Collection<Integer> percorridos, int nAtual){
		
		
    
       percorridos.add(nAtual);

        for(int i : Grafo.get(nAtual)) {

            if(!percorridos.contains(i)){
                BuscaProfundidade(Grafo, percorridos, i);
            }
        }
    }


//===================================================================================================================================================================================//

	
	public static void CalculaComponentes ( LinkedList<LinkedList<Integer>> Grafo, List<Integer> componentesGrafo, Collection<Integer> percorridosGrafo) {
		
		int comecoG = 0;
		int finalG = 0;
		int componente = 0;
		
		for(int i = 1; i < 86319; i++){
            if(!percorridosGrafo.contains(i)){
                comecoG = percorridosGrafo.size();
				
                BuscaProfundidade(Grafo, percorridosGrafo, i);
				
                finalG = percorridosGrafo.size();
				
                componente = finalG - comecoG;
				
                componentesGrafo.add(componente);
				
            }
        }  
        
		
		
	}
	
	
//===================================================================================================================================================================================//


    public static void main(String[] args) throws IOException {
        
        LinkedList<LinkedList<Integer>> Grafo = ListaAdj();
        List<Integer> componentes = new LinkedList<>();
        Collection<Integer> percorridos = new HashSet<>();
		
		CalculaComponentes(Grafo, componentes, percorridos);

		FileWriter arquivo = new FileWriter("ComponentesCenario1.txt");
        PrintWriter saidaArquivo = new PrintWriter(arquivo);
		
		for(int i : componentes) saidaArquivo.println(i);
		
        saidaArquivo.close();
		
    }
}
//===================================================================================================================================================================================//