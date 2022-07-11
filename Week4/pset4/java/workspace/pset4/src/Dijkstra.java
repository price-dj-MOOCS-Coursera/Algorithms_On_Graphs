import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

import edu.princeton.cs.algs4.IndexMinPQ;

public class Dijkstra {
	
	private static int[] distTo;
	private static IndexMinPQ<Integer> pq;
	private static int[] prev;
	
    private static int distance(ArrayList<Integer>[] adj, ArrayList<Integer>[] cost, int s, int t) {
        
    	distTo = new int[adj.length];
    	prev = new int[adj.length];
    	
    	for (int v = 0; v < adj.length; v++)
            distTo[v] = Integer.MAX_VALUE;
        distTo[s] = 0;
    	
        pq = new IndexMinPQ<Integer>(adj.length);
        
        pq.insert(s, distTo[s]);
        
        while (!pq.isEmpty()) {
        	int u = pq.delMin();
        	for (int v : adj[u]) {
        		relax(cost, u, v);
        	}
        }
        
    	return -1;
    }
    
    private static void relax(ArrayList<Integer>[] cost, int u, int v) {
    	
    	
    }
    

    public static void main(String[] args) throws FileNotFoundException {
    	FileInputStream fs= new FileInputStream("D:/Documents/Dropbox/Coursera/Data_Structures_and_Algorithms/Algorithms_On_Graphs/Week4/pset4/java/workspace/pset4/src/01dijk.txt");
        Scanner scanner = new Scanner(fs);
    	//Scanner scanner = new Scanner("01dijk.txt");
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        ArrayList<Integer>[] adj = (ArrayList<Integer>[])new ArrayList[n];
        ArrayList<Integer>[] cost = (ArrayList<Integer>[])new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<Integer>();
            cost[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m; i++) {
            int x, y, w;
            x = scanner.nextInt();
            y = scanner.nextInt();
            w = scanner.nextInt();
            adj[x - 1].add(y - 1);
            cost[x - 1].add(w);
        }
        int x = scanner.nextInt() - 1;
        int y = scanner.nextInt() - 1;
        //System.out.println(adj);
        //System.out.println(cost);
        System.out.println(distance(adj, cost, x, y));
    }
}

