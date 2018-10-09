//HashMap<Integer, DoublyLinkedList<Block>> 
//Use a Queue if we didn't have to reorder
//I could see this breaking down as associativity factor increases
public class LRUCache {
	private final int size;
	private HashMap<Integer, DoublyLinkedList> cache; //Key: Index; Value: Set of blocks stored in a DoublyLinkedList
	public LRUCache(int cacheSize, int associativityFactor, int BlockSize) {

	}

	public Block retrieveBlock(int tag, int index,  int offset) {

	}


}

public class Block{
	int tag;
	Array<Integer> data;
	public Block prev;
	public Block next;
}

public class DoublyLinkedList{
	private final int size;
	private int currSize;
	public Block head;
	public Block tail;

	public void addBlock(Block toAdd) {

	}

	public Integer retrieveBlockFromList(int tag, int offset){
		//traverse list
	}

	public getLast() {
		return tail;
	}
}