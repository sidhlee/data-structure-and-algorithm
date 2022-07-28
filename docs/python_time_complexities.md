# Python Time Complexity

Source: [python wiki](https://wiki.python.org/moin/TimeComplexity)

## List

Worst cost:

- growing sizse (everything has to move!)
- inserting/deleting near the beginning

Use `collections.deque` if you need to add/remove at both ends.

<table style="width:">
   <tbody>
      <tr>
         <td>
            <p class="line891"><strong>Operation</strong> </p>
         </td>
         <td>
            <p class="line891"><strong>Average Case</strong> </p>
         </td>
         <td>
            <p class="line891"><strong><a class="http" href="http://en.wikipedia.org/wiki/Amortized_analysis">Amortized Worst Case</a></strong> </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-10"></span>
            <p class="line862">Copy </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-11"></span>
            <p class="line862">Append[1] </p>
         </td>
         <td>
            <p class="line862">O(1) </p>
         </td>
         <td>
            <p class="line862">O(1) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-12"></span>
            <p class="line862">Pop last </p>
         </td>
         <td>
            <p class="line862">O(1) </p>
         </td>
         <td>
            <p class="line862">O(1) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-13"></span>
            <p class="line862">Pop intermediate[2] </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-14"></span>
            <p class="line862">Insert </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-15"></span>
            <p class="line862">Get Item </p>
         </td>
         <td>
            <p class="line862">O(1) </p>
         </td>
         <td>
            <p class="line862">O(1) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-16"></span>
            <p class="line862">Set Item </p>
         </td>
         <td>
            <p class="line862">O(1) </p>
         </td>
         <td>
            <p class="line862">O(1) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-17"></span>
            <p class="line862">Delete Item </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-18"></span>
            <p class="line862">Iteration </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-19"></span>
            <p class="line862">Get Slice </p>
         </td>
         <td>
            <p class="line862">O(k) </p>
         </td>
         <td>
            <p class="line862">O(k) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-20"></span>
            <p class="line862">Del Slice </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-21"></span>
            <p class="line862">Set Slice </p>
         </td>
         <td>
            <p class="line862">O(k+n) </p>
         </td>
         <td>
            <p class="line862">O(k+n) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-22"></span>
            <p class="line862">Extend[1] </p>
         </td>
         <td>
            <p class="line862">O(k) </p>
         </td>
         <td>
            <p class="line862">O(k) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-23"></span>
            <p class="line891"><a class="http" href="http://svn.python.org/projects/python/trunk/Objects/listsort.txt">Sort</a> </p>
         </td>
         <td>
            <p class="line862">O(n log n) </p>
         </td>
         <td>
            <p class="line862">O(n log n) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-24"></span>
            <p class="line862">Multiply </p>
         </td>
         <td>
            <p class="line862">O(nk) </p>
         </td>
         <td>
            <p class="line862">O(nk) </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-25"></span>
            <p class="line862">x in s </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
         <td>
            <p class="line862"> </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-26"></span>
            <p class="line862">min(s), max(s) </p>
         </td>
         <td>
            <p class="line862">O(n) </p>
         </td>
         <td>
            <p class="line862"> </p>
         </td>
      </tr>
      <tr>
         <td>
            <span class="anchor" id="line-27"></span>
            <p class="line862">Get Length </p>
         </td>
         <td>
            <p class="line862">O(1) </p>
         </td>
         <td>
            <p class="line862">O(1) </p>
         </td>
      </tr>
   </tbody>
</table>

## Collections.deque

A deque (double-ended queue) is a doubly linked list implemented with a list of arrays.

<table style="width:"><tbody><tr>  <td><p class="line891"><strong>Operation</strong> </p></td>
  <td><p class="line891"><strong>Average Case</strong> </p></td>
  <td><p class="line891"><strong>Amortized Worst Case</strong> </p></td>
</tr>
<tr>  <td><span class="anchor" id="line-35"></span><p class="line862">Copy </p></td>
  <td><p class="line862">O(n) </p></td>
  <td><p class="line862">O(n) </p></td>
</tr>
<tr>  <td><span class="anchor" id="line-36"></span><p class="line862">append </p></td>
  <td><p class="line862">O(1) </p></td>
  <td><p class="line862">O(1) </p></td>
</tr>
<tr>  <td><span class="anchor" id="line-37"></span><p class="line862">appendleft </p></td>
  <td><p class="line862">O(1) </p></td>
  <td><p class="line862">O(1) </p></td>
</tr>
<tr>  <td><span class="anchor" id="line-38"></span><p class="line862">pop </p></td>
  <td><p class="line862">O(1) </p></td>
  <td><p class="line862">O(1) </p></td>
</tr>
<tr>  <td><span class="anchor" id="line-39"></span><p class="line862">popleft </p></td>
  <td><p class="line862">O(1) </p></td>
  <td><p class="line862">O(1) </p></td>
</tr>
<tr>  <td><span class="anchor" id="line-40"></span><p class="line862">extend </p></td>
  <td><p class="line862">O(k) </p></td>
  <td><p class="line862">O(k) </p></td>
</tr>
<tr>  <td><span class="anchor" id="line-41"></span><p class="line862">extendleft </p></td>
  <td><p class="line862">O(k) </p></td>
  <td><p class="line862">O(k) </p></td>
</tr>
<tr>  <td><span class="anchor" id="line-42"></span><p class="line862">rotate </p></td>
  <td><p class="line862">O(k) </p></td>
  <td><p class="line862">O(k) </p></td>
</tr>
<tr>  <td><span class="anchor" id="line-43"></span><p class="line862">remove </p></td>
  <td><p class="line862">O(n) </p></td>
  <td><p class="line862">O(n) </p></td>
</tr>
</tbody></table>

## Set

Set is implemented very similarly as dict.
