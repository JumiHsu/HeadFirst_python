題目：https://leetcode.com/problems/squares-of-a-sorted-array/
答案：https://leetcode.com/articles/squares-of-a-sorted-array/

Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number,
also in sorted non-decreasing order.
 
Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

【C#】------------------------------

public class Solution 
{
	// 寫法1
	/*
	Runtime: 328 ms, faster than 55.44% of C# online submissions for Squares of a Sorted Array.
	Memory Usage: 40.6 MB, less than 27.14% of C# online submissions for Squares of a Sorted Array.
	*/
    public int[] SortedSquares(int[] A) 
    {       
        int N = A.Length;
        int[] ans = new int[N];
        for (int i =0; i < N; i++)
        {
            //Console.WriteLine(i);  // WriteLine會換行
            
            ans[i] = A[i]*A[i];
        }
        Array.Sort(ans);
        return ans;
    }
}


public class Solution 
{
	// 寫法2
	// 參考資料：https://stackoverflow.com/questions/202813/adding-values-to-a-c-sharp-array
	// Add/AddRange：https://blog.csdn.net/qq_36006719/article/details/77067700
	/*
	Runtime: 336 ms, faster than 48.21% of C# online submissions for Squares of a Sorted Array.
	Memory Usage: 42.5 MB, less than 5.71% of C# online submissions for Squares of a Sorted Array.
	*/
	
    public int[] SortedSquares(int[] A) 
    {       
        int N = A.Length;
        int[] ans = new int[N];
        List<int> termsList = new List<int>();
        
        foreach (int element in A)
        {            
            termsList.Add(element*element);
        }
        
		termsList.Sort(); //其實你也可以對list去排序，但他答案要的是array
		
        ans = termsList.ToArray();
        Array.Sort(ans);
        return ans;
    }

}



