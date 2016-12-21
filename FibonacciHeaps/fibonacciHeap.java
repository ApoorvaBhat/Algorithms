import java.util.*;

public class fibonacciHeap
{

	private circularDLL rootList;
	private FHNode min;
	private int n;


	public fibonacciHeap()
	{
		rootList = new circularDLL();
		min = null;
		n = 0;
	}

	public int getN()
	{
	    return this.n;
	}

	public void setN(int n)
	{
	    this.n = n;
	}

	public FHNode getMin()
	{
	    return this.min;
	}

	public void setMin(FHNode min)
	{
	    this.min = min;
	}

	public circularDLL getrootList()
	{
	    return this.rootList;
	}


	public void fibHeapInsert(int key)
	{
		FHNode x = new FHNode(key);

		rootList.insert(x);
		if(min == null || key < min.getKey())
		{
			min = x;
		}
		n = n + 1;
	}

	public FHNode extractMin()
	{
		FHNode z = min;

		if(z != null)
		{
			circularDLL children = z.getChildren();
			for(FHNode x : children)
			{
				rootList.insert(x);
				//System.out.println("Adding " + x.getKey() + " to rootlist");
				x.setParent(null);
			}
			//System.out.println("removing " + z.getKey() + " from rootlist");
			rootList.remove(z);
			//traverseRootList();
			if(z == z.getRight())
			{
				//System.out.println(z.getKey() + " was only node in rootlist and had no children, setting min to null");
				min = null;
			}
			else
			{
				min = z.getRight();
				//System.out.println("setting min to " + min.getKey() + "\n\n calling consolidate\n\n");
				consolidate();
			}
			n = n - 1;
		}
		return z;
	}

	private void consolidate()
	{
		double GOLDEN_RATIO = 1.6180339;
		int maxDegree = (int)Math.floor(logBaseN(n, GOLDEN_RATIO));

		//System.out.println("maxdegree:" + maxDegree);

		FHNode []A = new FHNode[maxDegree];

		for(int i = 0; i < maxDegree; i++)
		{
			A[i] = null;
		}
		//int count = 0;

		for(FHNode w : rootList)
		{
			//System.out.println("Iteration " + count + " w = " + w.getKey());
			FHNode x = w;
			//System.out.println("x= " + x.getKey());
			int d = x.getDegree();
			//System.out.println("x's degree " + x.getDegree());
			while(A[d] != null)
			{
				FHNode y = A[d];
				//System.out.println("x: " + x.getKey());
				//System.out.println("A[d]: " + y.getKey());
				if(x.getKey() > y.getKey())
				{
					FHNode temp = x;
					x = y;
					y = temp;
				}
				//System.out.println("After exchanging:\n");
				//System.out.println("x: " + x.getKey());
				//System.out.println("A[d]: " + y.getKey());
				fibHeapLink(y, x);
				A[d] = null;
				d = d + 1;
			}
			A[d] = x;
			//System.out.println("Adding " + x.getKey() + " to A[]");
			//count++;
		}
		min = null;

		for(int i = 0; i < maxDegree; i++)
		{
			if(A[i] != null)
			{
				if(min == null)
				{
					rootList = new circularDLL();
					rootList.insert(A[i]);
					min = A[i];
				}
				else
				{
					rootList.insert(A[i]);
					if(A[i].getKey() < min.getKey())
					{
						min = A[i];
					}
				}
			}
		}
	}

	private void fibHeapLink(FHNode y, FHNode x)
	{

		//System.out.println("Removing " + y.getKey());
		rootList.remove(y);
		x.addChild(y);
		x.setDegree(x.getDegree() + 1);
		y.setMark(false);
	}

	public void decreaseKey(int n, int k)
	{
		boolean found = false;
		for(FHNode root : rootList)
		{
			FHNode x = DFS(root, n);
			if(x != null)
			{
				found = true;
				fibHeapDecreaseKey(x, k);
				break;
			}
		}
		if(!found)
		{
			System.out.println("ERROR - Node not found");
		}

	}

	private FHNode DFS(FHNode root, int n)
	{
		if(root.getKey() == n)
		{
			return root;
		}
		circularDLL children = root.getChildren();
		for(FHNode child : children)
		{
			return DFS(child, n);
		}
		return null;
	}

	private void fibHeapDecreaseKey(FHNode x, int k)
	{
		if(k > x.getKey())
		{
			System.out.println("ERROR - New key greater than current key");
		}
		else
		{
			x.setKey(k);
			FHNode y = x.getParent();

			if(y != null && (x.getKey() < y.getKey()))
			{
				cut(x, y);
				cascadingCut(y);
			}
			if(x.getKey() < min.getKey())
			{
				min = x;
			}
		}
	}

	private void cut(FHNode x, FHNode y)
	{
		y.removeChild(x);
		y.setDegree(y.getDegree() - 1);
		rootList.insert(x);
		x.setParent(null);
		x.setMark(false);
	}

	private void cascadingCut(FHNode y)
	{
		FHNode z = y.getParent();
		if(z != null)
		{
			if(y.getMark() == false)
			{
				y.setMark(true);
			}
			else
			{
				cut(y, z);
				cascadingCut(z);
			}
		}
	}

	private double logBaseN(int x, double n)
	{
		return Math.log(x) / Math.log(n);
	}

	public void delete(int x)
	{
	    decreaseKey(x,-99999);
	    extractMin();
    }

	public void traverseRootList()
	{

		for(FHNode x : rootList)
		{
			System.out.println(x.getKey() + " ");

			if(x.getDegree() > 0)
			{
				circularDLL d = x.getChildren();
				System.out.println("Children of " + x.getKey() + ":");
				for(FHNode y : d)
				{
					System.out.println(y.getKey());
				}
			}
			System.out.println();

		}
		System.out.println("min's key: " + min.getKey() + "\nn: " + n);
	}

	public static fibonacciHeap union(fibonacciHeap h1,fibonacciHeap h2)
	{
	    fibonacciHeap h = new fibonacciHeap();
	    for(FHNode x : h1.getrootList())
        {
            h.getrootList().insert(x);
        }
        for(FHNode y : h2.getrootList())
        {
            h.getrootList().insert(y);
        }
        h.setMin(h1.getMin());
        if((h1.getMin()==null) || (h2.getMin() != null && h2.getMin().getKey() < h1.getMin().getKey()))
        {
            h.setMin(h2.getMin());
        }
        h.setN(h1.getN() + h2.getN());

    return h;
	}
}

















