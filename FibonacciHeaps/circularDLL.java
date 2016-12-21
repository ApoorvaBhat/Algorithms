import java.util.Iterator;

public class circularDLL implements Iterable<FHNode>
{
	private FHNode first;
	private FHNode last;

	public circularDLL()
	{
		first = null;
		last = null;
	}

	private class dllIterator implements Iterator<FHNode>
	{
		private FHNode temp;
		private int count;


		public dllIterator()
		{
			temp = first;
			initCount();
		}

		private void initCount()
		{
			if(first == null)
			{
				count = 0;
			}

			else if(first == last)
			{
				count = 1;
			}
			else
			{
				FHNode x = first;

				while(x != last)
				{
					count++;
					x = x.getRight();
				}
				count = count + 1;
			}
		}

		public boolean hasNext()
		{
			return count > 0;
		}

		public FHNode next()
		{
			FHNode x = temp;
			temp = temp.getRight();
			count--;
			return x;
		}
	}

	public dllIterator iterator()
	{
		return new dllIterator();
	}


	public void insert(FHNode x)
	{
		if(first == null)
		{
			x.setLeft(x);
			x.setRight(x);
			first = x;
			last = x;
		}
		else
		{
			last.setRight(x);
			x.setLeft(last);
			x.setRight(first);
			last = x;
		}
	}

	public void remove(FHNode x)
	{
		FHNode temp = first;
		boolean found = false;
		while(temp.getRight() != first)
		{
			if(temp == x)
			{
				found = true;
				//System.out.println("found " + temp.getKey());
				break;
			}
			temp = temp.getRight();
		}

		if(!found && last == x)
		{
			found = true;
		}

		if(found)
		{
			if(temp == first)
			{
				//System.out.println("setting first to " + first.getRight().getKey());
				first = first.getRight();
				//System.out.println("setting last.right to " + first.getKey());
				last.setRight(first);
			}
			else if(temp == last)
			{
				last = last.getLeft();
				first.setLeft(last);
			}
			else
			{
				temp.getLeft().setRight(temp.getRight());
				temp.getRight().setLeft(temp.getLeft());
			}
		}
		else
		{
			System.out.println("Node " + x.getKey() +" not present");
		}
	}





	public void traverse()
	{
		FHNode temp = first;

		while(temp != last)
		{
			System.out.println(temp.getKey() + " ");
			temp = temp.getRight();
		}
		System.out.println(temp.getKey() + " ");
	}

}


















