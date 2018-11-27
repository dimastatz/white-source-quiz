# white-source-quiz

Question 1

For a sequence of n integers a1, a2, ..., an, an SBM sequence
is a subsequence ai, aj, ak such that i < j < k and ai < ak <
aj.
Example 1:
Input: [1, 2, 3, 7]
Output: False
Explanation: There is no SBM sequence in the
sequence.
Example 2:
Input: [4, 1, 7, 8, 7, 2]
Output: True
Explanation: There is an SBM sequence in the
sequence [1, 7, 2] or [1, 8 ,2] or [1, 8, 7].

Implement a Java server that gets a sequence of n integers
as an input in JSON format and checks whether there is a SBM
sequence in the
list.
e.g.

$ curl -X POST http://localhost:10000/server -H "content-
type:application/json" -d '{"seq":[1,2,3]}'

Result:false

$ curl -X POST http://localhost:10000/server -H "content-
type:application/json" -d '{"seq":[1,3,2]}'

Result:true



Question 2
For a given Node.js module folder,
write a Java program that discovers all the local modules used
by this library from a user perspective.
For example, if the following file is the only file of the
library, the program should print './a' './b' and not ‘fs’.
------ module -------
var fs = require('fs');
var a = require('./a');
function f(x) {
var a = require('./b');
}
---------------------

Hint
You can use JavaScript parser for building a graph
representation for the file.
