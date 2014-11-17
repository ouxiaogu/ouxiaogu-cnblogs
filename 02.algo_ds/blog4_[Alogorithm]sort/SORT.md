###摘要

本文主要讲几种最基本的排序算法，其伪代码，以及算法复杂度分析

下面算法分析注意点，以及伪代码和正常源码相比需要注意的地方

* 下面所有的排序都是从小到大按升序排列
* **while** **for** 循环的正常退出时，**while** **for** 这样的循环条件语句的执行次数比循环体要多1
* 伪代码的元素编号从1开始，而不是0

##PART 1#

###INSERTION-SORT##

+ 插入排序循环调动范围是A[position]<-A[j],排列完后，A[1:j]为正序
+ 插入排序对第一个元素无要求
+ 插入排序用key记录待插入的元素，而每次比较都是 A[i+1] 虚位以待，当满足条件 `A[i]>Key` 则令A[i]填充原虚位A[i+1]，完成后i减1，虚位前移为A[i]，内存中位置移动幅度都为1。

INSERTION-SORT(A)    

for j ← 2  to  length[A] do:
    key ← A[j]    
    // Insert A[j] into the sorted sequenceA[1..j-1]    
    i ← j – 1    
    while i > 0 and A[i] > key do:
        A[i+1] ← A[i]    
        i ← i – 1    
    A[i+1] ← key    

###BUBLE-SORT##

+ 冒泡排序循环调动范围是A[i]<-A[n],排列完后，A[1:i]为正序，且后面未排序部分有改善
+ 冒泡排序从最后一层开始，一层一层地与上一层相比较，泡沫内的数偏大则交换，内存中位置移动幅度都为1，

BUBLE-SORT(A)   
n ←  length[A] 
for i ← 1 to n 
    swapped ← false  
    for j ← n downto i+1  do:  
        if A[i-1]>A[i] then:  
            exchange A[i-1] ↔ A[i] 
            swaped ← true
    if  swapped = false then:   // stop swapping
        break  

###SELECTION-SORT##

SELECTION-SORT(A)  

n ← length[A]  
for j ← 1 to n − 1 do:
    smallest ← j
    for i ← j + 1 to n do:
        if A[i ] < A[smallest] then:
            smallest ← i
    exchange A[ j ] ↔ A[smallest]
   
##PART 2#

### MERGE-SORT #

MERGE(A, p, q, r)
n1 ← q - p + 1
n2 ← r - q
create arrays L[1 ‥ n1 + 1] and R[1 ‥ n2 + 1]
for i ← 1 to n1 do:
    L[i] ← A[p + i - 1]
for j ← 1 to n2 do:
    R[j] ← A[q + j]
L[n1 + 1] ← ∞
R[n2 + 1] ← ∞
i ← 1
j ← 1
for k ← p to r do:
    if L[i] ≤ R[j] then:
        A[k] ← L[i]
        i ← i + 1
    else A[k] ← R[j]
        j ← j + 1

MERGE-SORT(A, p, r)
if p < r then:
    q ← ⌊(p + r)/2⌋  
    MERGE-SORT(A, p, q)
    MERGE-SORT(A, q + 1, r)
    MERGE(A, p, q, r)

### HEAP-SORT #

PARENT(i)
   return ⌊i/2⌋

LEFT(i)
   return 2i

RIGHT(i)
   return 2i + 1

MAX-HEAPIFY(A, i)
    l ← LEFT(i)
    r ← RIGHT(i)
    if l ≤ heap-size[A] and A[l] > A[i] then:
        largest ← l
    else largest ← i
    if r ≤ heap-size[A] and A[r] > A[largest] then:
        largest ← r
        if largest ≠ i then:
            exchange A[i] ↔ A[largest]
        MAX-HEAPIFY(A, largest)

BUILD-MAX-HEAP(A)
    heap-size[A] ← length[A]
    for i ← ⌊length[A]/2⌋ downto 1 do:
        MAX-HEAPIFY(A, i)

HEAPSORT(A)
    BUILD-MAX-HEAP(A)
    for i ← length[A] downto 2 do:
        exchange A[1] ↔ A[i]
        heap-size[A] ← heap-size[A] - 1
        MAX-HEAPIFY(A, 1)

### QUICK-SORT #

QUICKSORT(A, p, r)
    if p < r then:
        q ← PARTITION(A, p, r)
        QUICKSORT(A, p, q - 1)
        QUICKSORT(A, q + 1, r)

PARTITION(A, p, r)
    x ← A[r]
    i ← p - 1
    for j ← p to r - 1 do:
        if A[j] ≤ x then:
            i ← i + 1
            exchange A[i] ↔ A[j]
    exchange A[i + 1] ↔ A[r]
    return i + 1

##PART 3. Linear Time Sort #

### RADIX-SORT #
LSD（Least significant digital）
MSD（Most significant digital）
LSB（Least significant bit）
MSB（Most significant bit）
T ≥ logB(n)·n·log2(B) = log2(n)·logB(2)·n·log2(B) = log2(n)·n·logB(2)·log2(B) = n·log2(n)
  
### pigeonhole-sort#
pigeonhole_sort(array A[n])  
    zero_var (B)      (* Zero out array B *)
    // count A[i]'s frequency
    for i in [0...length(A)-1]
        B[A[i]] := B[A[i]]+1
    // 把结果复制回数组A, B的索引为A的值，eg.i=0,B[0]=4，即A的最小值0出现过四次，这四个排在A[0]~A[3] 
    j := 0
    for i in [0...length(B)-1]
        repeat B[i] times
            A[j] := i
            j := j+1

### bucket-sort 桶排序或箱排序 #

Bucket sort works as follows:

- Set up an array of initially empty "buckets".
- Scatter: Go over the original array, putting each object in its bucket.
- Sort each non-empty bucket.
- Gather: Visit the buckets in order and put all elements back into the original array.

bucket-sort(array A)
    n ← length(A)
    buckets ← new array of n empty lists
    // 将A[i]插入到A[i]的最高位所在的桶中，如12,15都归于桶1
    for i = 0 to n-1 do: 
        insert A[i] into buckets[msbits(A[i], k)]
    for i = 0 to n - 1 do: 
        next-sort(buckets[i])
    return the concatenation of buckets[0], ..., buckets[n-1]