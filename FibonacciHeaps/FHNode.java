public class FHNode
{
	private FHNode parent;
	private FHNode child;
	private circularDLL childList;
	private FHNode left, right;
	
	private int degree;
	private boolean mark;
	private int key;
	
	public FHNode(int k)
	{
		parent = null;
		child = null;
		childList = new circularDLL();
		left = null;
		right = null;
		degree = 0;
		mark = false;
		key = k;
	}
	
	
	public int getKey()
	{
		return key;
	}
	public FHNode getLeft()
	{
		return left;
	}
	public FHNode getRight()
	{
		return right;
	}
	public FHNode getParent()
	{
		return parent;
	}
	public circularDLL getChildren()
	{
		return childList;
	}
	public int getDegree()
	{
		return degree;
	}
	public boolean getMark()
	{
		return mark;
	}
	
	public void setLeft(FHNode x)
	{
		left = x;
	}
	public void setRight(FHNode x)
	{
		right = x;
	}
	public void setParent(FHNode p)
	{
		parent = p;
	}
	public void setDegree(int d)
	{
		degree = d;
	}
	public void setMark(boolean m)
	{
		mark = m;
	}
	public void setKey(int k)
	{
		key = k;
	}
	
	public void addChild(FHNode c)
	{
		child = c;
		childList.insert(c);
	}
	
	public void removeChild(FHNode c)
	{
		if(child == c)
		{
			child = c.getRight();
		}
		childList.remove(c);
	}
		
}














