import java.util.*;
public class client extends fibonacciHeap
{
	public static void main(String []args)
	{
		//fibonacciHeap h1 = new fibonacciHeap();
        Scanner sc = new Scanner(System.in);
		/*h1.fibHeapInsert(10);
		h1.fibHeapInsert(20);
		h1.fibHeapInsert(30);
		//FHNode min = h1.extractMin();
		//System.out.println("extracted: " + min.getKey());
		h1.decreaseKey(30, 5);
		//h1.traverseRootList();
		fibonacciHeap h2 = new fibonacciHeap();
		h2.fibHeapInsert(100);
		h2.fibHeapInsert(200);
		h2.fibHeapInsert(300);
		h2.decreaseKey(200,3);
		fibonacciHeap h3 = union(h1,h2);
		h3.delete(3);
		h3.traverseRootList(); */
        fibonacciHeap h[] = new fibonacciHeap[10];
        int count =0;
		while(true)
        {
            System.out.println("1. Create new heap\n2. Insert into the heap\n3. Extract Minimum\n4. Decrease Key\n5. Delete a Node\n6. Union 2 heaps\n7. Traverse the Heap\n");
            int n = sc.nextInt(); int kk = 1;
            if(n==1)
            {
                h[count++]=new fibonacciHeap();
                System.out.println("Heap h"+count+" created");
            }

            else if(n==2)
            {   System.out.println("Enter the heap Number\n");
                int c = sc.nextInt();
                System.out.println("Enter the value to be inserted\n");
                int v = sc.nextInt();
                h[c-1].fibHeapInsert(v);

            }

            else if(n==3)
            {
                System.out.println("Enter the heap Number\n");
                int c = sc.nextInt();
                FHNode min = h[c-1].extractMin();
                System.out.println("extracted: " + min.getKey());
            }

            else if(n==4)
            {
                System.out.println("Enter the heap Number\n");
                int c = sc.nextInt();
                System.out.println("Enter the value to be decreased\n");
                int v = sc.nextInt();
                System.out.println("Enter the new value\n");
                int g = sc.nextInt();
                h[c-1].decreaseKey(v,g);
            }

            else if(n==5)
            {
                System.out.println("Enter the heap Number\n");
                int c = sc.nextInt();
                System.out.println("Enter the value to be deleted\n");
                int v = sc.nextInt();
                h[c-1].delete(v);
            }

            else if(n==6)
            {
                System.out.println("Enter the first heap Number\n");
                int c = sc.nextInt();
                System.out.println("Enter the second heap Number\n");
                int ca = sc.nextInt();
                h[0] = union(h[c-1],h[ca-1]);
                kk++;
            }

            else if(n==7)
            {
                System.out.println("Enter the heap Number\n");
                int c = sc.nextInt();
                h[c-1].traverseRootList();
            }
        }
	}
}
